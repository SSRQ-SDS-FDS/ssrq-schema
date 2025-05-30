from glob import glob

import requests
from lxml import etree
from saxonche import PySaxonProcessor
from ssrq_cli.validate.rng import validate_with_rng
from ssrq_cli.validate.types import RNGValidationError

from utils.commons.config import COMMONS_DIR, ELEMENTS_DIR, SCHEMA_DIR
from utils.docs.helpers.node_to_text import is_not_link_to_md_file
from utils.docs.specs.namespaces import NS_MAP

ODD_ENTRY_FILES = glob(str(SCHEMA_DIR / "*.xml"))
COMMON_FILES = glob(str(COMMONS_DIR / "*.xml"))
ELEMENT_FILES = glob(str(ELEMENTS_DIR / "*.xml"))
TEI_ODD_RNG = "http://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5odds.rng"
FILTER_MSGS = [
    'element "exemplum" missing required attribute "xml:lang"',
    'value of attribute "module" is invalid',
    'element "xi:include" not allowed here',
]


class WellFormedException(Exception):
    """Exception raised when some files are not well-formed."""

    def __init__(self, files: list[str]):
        self.files = files
        super().__init__(
            "Some files are not well-formed:\n\t{}".format("\n\t".join(files))
        )


class InvalidSpecException(Exception):
    """Exception raised when some files are not valid."""

    def __init__(self, file: str, msg: str):
        self.file = file
        self.msg = msg
        super().__init__(f"{file}:\n{msg}")


class InvalidRefTargetException(Exception):
    """Exception raised when some files are not valid."""

    def __init__(self, file: str, msg: str):
        self.file = file
        self.msg = msg
        super().__init__(f"{file}:\n{msg}")


def check_well_formed(files: list[str]) -> None:
    """Check if the given files are well-formed.

    Args:
        files (list[str]): List of files to check.

    Raises:
        Exception: If some files are not well-formed."""
    with PySaxonProcessor(license=False) as proc:
        non_well_formed_files: list[str] = []

        for file in files:
            try:
                proc.parse_xml(xml_file_name=file)
            except Exception:
                """We can continue here because the error is already printed to the console."""
                non_well_formed_files.append(file)
                continue

        if len(non_well_formed_files) > 0:
            raise WellFormedException(non_well_formed_files)


def parse_files(files: list[str]):
    """Helper function to parse xml file with the given parser.

    Args:
        files (list[str]): List of files to parse.

    Returns:
        list[tuple[str, ext_etree._ElementTree]]: List of tuples of the form (file, parsed_file).
    """
    parser = etree.XMLParser(recover=True)
    parsed_files: list[tuple[str, etree._ElementTree]] = [
        (file, etree.parse(file, parser=parser)) for file in files
    ]
    return parsed_files


def filter_errors(
    list_errors: list[RNGValidationError], list_filter_msgs: list[str] = FILTER_MSGS
) -> list[RNGValidationError]:
    """Filter the list of errors to remove the ones that are expected."""
    return [
        error
        for error in list_errors
        if not any(msg in error.message for msg in list_filter_msgs)
    ]


def check_ref_targets(
    files: list[tuple[str, etree._ElementTree]],
) -> list[InvalidRefTargetException] | None:
    from urllib.parse import urlparse

    errors: list[InvalidRefTargetException] = []

    for file, tree in files:
        for ref in tree.findall(".//tei:ref", namespaces=NS_MAP):
            target = ref.get("target")

            if target is None:
                errors.append(
                    InvalidRefTargetException(
                        file, f"Line {ref.sourceline}: Ref is missing target-attribute."
                    )
                )
                continue

            parsed_target = urlparse(target)

            if is_not_link_to_md_file(parsed_target) and len(parsed_target.scheme) == 0:
                errors.append(
                    InvalidRefTargetException(
                        file,
                        f"Line {ref.sourceline}: {target} is not a valid external URL and does not point to a static '.md'-documentation-file.",
                    )
                )
    return errors if len(errors) > 0 else None


def validate_odd_with_odd(
    sources: list[tuple[list[str], str, str]], odd_url: str = TEI_ODD_RNG
) -> None:
    """Validate the ODD files with the ODD schema.

    Args:
        sources (list[tuple[list[str], str]]): List of tuples of the form (files, pattern, dir_path).

    Raises:
        ExceptionGroup: If some files are not valid.
    """
    schema = requests.get(odd_url).text

    exceptions: list[Exception] = []

    for files, pattern, dir_path in sources:
        file_sources = parse_files(files)
        validation = validate_with_rng(pattern=pattern, schema=schema)

        if validation.is_err():
            raise Exception(f"Could not validate the schema: {validation.unwrap_err()}")

        for info in validation.unwrap():
            if info.report and len(msgs := filter_errors(info.report)) > 0:
                exceptions.append(
                    InvalidSpecException(
                        f"{dir_path}/{info.source}",
                        msg="\n".join(
                            [
                                f"Line {msg.line}; Column {msg.column}: {msg.message}"
                                for msg in msgs
                            ]
                        ),
                    )
                )

        for error in check_ref_targets(file_sources) or []:
            exceptions.append(error)

    if len(exceptions) > 0:
        raise ExceptionGroup("Some files are not valid.", exceptions)


if __name__ == "__main__":
    check_well_formed(ODD_ENTRY_FILES + COMMON_FILES + ELEMENT_FILES)
    validate_odd_with_odd(
        sources=[
            (ODD_ENTRY_FILES, str(SCHEMA_DIR / "*.xml"), str(SCHEMA_DIR)),
            (COMMON_FILES, str(COMMONS_DIR / "*.xml"), str(COMMONS_DIR)),
            (ELEMENT_FILES, str(ELEMENTS_DIR / "*.xml"), str(ELEMENTS_DIR)),
        ]
    )
