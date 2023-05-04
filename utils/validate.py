from glob import glob

import requests
from main import COMMON_DIR, ELEMENTS_DIR, SRC_DIR
from saxonche import PySaxonProcessor
from ssrq_cli.validate import RNGJingValidator
from ssrq_cli.validate.xml import ValidationError
from ssrq_cli.xml_utils import ext_etree

ODD_ENTRY_FILES = glob(str(SRC_DIR / "*.xml"))
COMMON_FILES = glob(str(COMMON_DIR / "*.xml"))
ELEMENT_FILES = glob(str(ELEMENTS_DIR / "*.xml"))
TEI_ODD_RNG = "http://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5odds.rng"
FILTER_MSGS = [
    'element "exemplum" missing required attribute "xml:lang"',
    'value of attribute "module" is invalid',
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
    parser = ext_etree.XMLParser(recover=True)
    parsed_files: list[tuple[str, ext_etree._ElementTree]] = [
        (file, ext_etree.parse(file, parser=parser)) for file in files
    ]
    return parsed_files


def filter_errors(
    list_errors: list[ValidationError], list_filter_msgs: list[str] = FILTER_MSGS
) -> list[ValidationError]:
    """Filter the list of errors to remove the ones that are expected."""
    return [
        error
        for error in list_errors
        if not any(msg in error.message for msg in list_filter_msgs)
    ]


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
        rng_validator = RNGJingValidator()
        file_sources = parse_files(files)
        rng_validator.validate(
            sources=file_sources, schema=schema, file_pattern=pattern
        )

        for error in rng_validator.get_invalid():
            if (
                error.report is not None
                and len((msgs := filter_errors(error.report))) > 0
            ):
                exceptions.append(
                    InvalidSpecException(
                        f"{dir_path}/{error.file}",
                        msg="\n".join(
                            [
                                f"Line {msg.line}; Column {msg.column}: {msg.message}"
                                for msg in msgs
                            ]
                        ),
                    )
                )

    if len(exceptions) > 0:
        raise ExceptionGroup("Some files are not valid.", exceptions)


if __name__ == "__main__":
    check_well_formed(ODD_ENTRY_FILES + COMMON_FILES + ELEMENT_FILES)
    validate_odd_with_odd(
        sources=[
            (COMMON_FILES, str(COMMON_DIR / "*.xml"), str(COMMON_DIR)),
            (ELEMENT_FILES, str(ELEMENTS_DIR / "*.xml"), str(ELEMENTS_DIR)),
        ]
    )
