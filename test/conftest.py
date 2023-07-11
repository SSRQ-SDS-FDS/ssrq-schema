import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, TypeAlias

import pytest
from pyschval.main import (
    XSLT_FILES,
    create_schematron_stylesheet,
    extract_schematron_from_relaxng,
)
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable
from ssrq_cli.validate import RNGJingValidator
from ssrq_cli.xml_utils import ext_etree

from utils.constants import SPECIFIED_ELEMENTS, SRC_DIR, XSLTS
from utils.main import COMPILE_ODD_STEPS, RNG_STEP, load_config
from utils.oddfactory import ODDFactory
from utils.ssrqschema import SSRQSchema
from utils.ssrqschematype import SSRQSchemaType

ElName = str

el_start_re = re.compile(r"(<\w+)([\s>\/])")


@dataclass
class FileConstraints:
    odd_name: str
    rules: str


class SimpleTEIWriter:
    path: Path

    def __init__(self, dir: Path):
        self.path = dir

    def write(self, name: str, content: str) -> None:
        with open(self.path / f"{name}.xml", "w", encoding="utf-8") as f:
            f.write(content)

    def list(self) -> list[str]:
        return [str(file.absolute()) for file in self.path.glob("*.xml")]

    def parse_files(self):
        parser = ext_etree.XMLParser(recover=True)
        parsed_files: list[tuple[str, ext_etree._ElementTree]] = [
            (file, ext_etree.parse(file, parser=parser)) for file in self.list()
        ]
        return parsed_files

    def construct_file_pattern(self) -> str:
        return str(self.path.absolute() / "*.xml")


def load_example(name: str) -> str:
    """Load the example file with the given name."""
    with open(
        Path(__file__).parent / "examples" / f"{name}", "r", encoding="utf-8"
    ) as f:
        return f.read()


def change_rng_start(rng: str, name: str) -> str:
    """Change the start element of the RNG file to the given name."""
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")  # type: ignore
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=rng)
        xsltproc.set_parameter("start-el-name", proc.make_string_value(name))  # type: ignore

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(XSLTS["change-start"])
        )

        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to resolve relative paths")

    return result


def add_tei_namespace(markup: str) -> str:
    """Add the TEI namespace to the given markup."""
    return (
        re.sub(
            el_start_re, r"\1 xmlns='http://www.tei-c.org/ns/1.0'\2", markup, count=1
        )
        if "http://www.tei-c.org/ns/1.0" not in markup
        else markup
    )


def extract_specified_elements_for_rng(schema: SSRQSchemaType) -> list[ElName]:
    """Extract the specified elements from the given schema –
    this list can be used to change the specified RNG start-Element.

    Args:
        schema (SSRQSchemaType): The schema to extract the elements from.

    Returns:
        list[str]: A list of all specified elements – based on includes by specGrpRef.
    """
    with open(SRC_DIR / schema["entry"], "r") as sf:
        sf = sf.read()
        specs: list[str] = re.findall(SPECIFIED_ELEMENTS, sf)

    return specs


@pytest.fixture(scope="session")
def odds() -> list[tuple[SSRQSchema, list[ElName]]]:
    """Compile all odds found in the pyproject.toml to odds and RelaxNG files. Return as a list of Schema objects."""
    config = load_config()

    if config is None:
        raise ValueError("No config file found")

    odds = [
        (
            ODDFactory(authors=config.authors, schema_config=schema).create(
                compile_odd_steps=COMPILE_ODD_STEPS, create_rng=RNG_STEP
            ),
            extract_specified_elements_for_rng(schema),
        )
        for schema in config.schemas
    ]

    return odds


@pytest.fixture(scope="session")
def change_rng_start_per_odd(
    odds: list[tuple[SSRQSchema, list[ElName]]]
) -> dict[str, dict[str, str]]:
    """Change the start element of the RNG file to the given name."""
    return {
        odd.name: {el: change_rng_start(odd.rng, el) for el in el_names}
        for odd, el_names in odds
    }


@pytest.fixture(scope="function")
def writer(tmp_path: Path) -> SimpleTEIWriter:
    """A fixture, which returns a SimpleTEIWriter object, which can be used to write TEI files to a temporary directory."""
    return SimpleTEIWriter(tmp_path)


@pytest.fixture(scope="session")
def main_schema(odds: list[tuple[SSRQSchema, list[ElName]]]) -> SSRQSchema:
    """A fixture, which returns the main ssrq schema."""
    try:
        return [odd for odd, _ in odds if odd.name == "TEI_Schema"][0]
    except IndexError:
        raise ValueError("No main schema found")


@pytest.fixture(scope="session")
def main_constraints(main_schema: SSRQSchema) -> str:
    """A fixture, which returns the schematron rules from the main schema."""
    extracted_rules = extract_schematron_from_relaxng(
        main_schema.rng, XSLT_FILES["extract-sch"]
    )

    return create_schematron_stylesheet(extracted_rules, XSLT_FILES["schxslt"])


RNG_test_function: TypeAlias = Callable[
    [str, str, str, bool, bool], Optional[RNGJingValidator]
]


@pytest.fixture(scope="function")
def test_element_with_rng(
    element_schema: dict[str, str],
    writer: SimpleTEIWriter,
) -> RNG_test_function:
    def test_element(
        element_name: str,
        name: str,
        markup: str,
        result: bool,
        return_validator: bool = False,
    ):
        """A generic function, which can be used to test a single element against the defined RelaxNG rules.

        Args:
            element_name (str): The name (without namespace) of the element to test.e
            name (str): The name of the file to write / the name of the testcase.
            markup (str): The markup to write to the file.
            result (bool): The expected result of the validation.
            return_validator (bool, optional): If True, the validator object is returned. Defaults to False.

        Returns:
            None: The test passes if the validation result matches the expected result.
        """

        validator = RNGJingValidator()
        writer.write(name, add_tei_namespace(markup))

        validator.validate(
            sources=writer.parse_files(),
            schema=element_schema[element_name],
            file_pattern=writer.construct_file_pattern(),
        )

        assert len(validator.get_invalid()) == (0 if result else 1)

        if return_validator:
            return validator

    return test_element
