import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias

import pytest
from lxml import etree
from pyschval.schematron.create import create_schematron_stylesheet
from pyschval.schematron.extract import extract_schematron_from_relaxng
from result import Err, Ok
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable
from ssrq_cli.validate.rng import validate_with_rng
from ssrq_cli.validate.types import RNGValidationInfos

from utils.commons import filehandler as io
from utils.commons.config import SCHEMA_DIR, XSLTS
from utils.schema import SPECIFIED_ELEMENTS
from utils.schema.compile import (
    Schema,
    SSRQSchemaType,
    load_config,
    odd_factory,
)

TEST_EXAMPLE_DIR = Path(__file__).parent.absolute() / "examples"

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
        io.FileHandler.write(
            directory=self.path, file_name=f"{name}.xml", content=content
        )

    def list(self) -> list[str]:
        return [str(file.absolute()) for file in self.path.glob("*.xml")]

    def parse_files(self):
        parser = etree.XMLParser(recover=True)
        parsed_files: list[tuple[str, etree._ElementTree]] = [  # type: ignore
            (file, etree.parse(file, parser=parser)) for file in self.list()
        ]
        return parsed_files

    def construct_file_pattern(self) -> str:
        return str(self.path.absolute() / "*.xml")


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

        result: str | None = xsl.transform_to_string(xdm_node=document)

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
    schema_content = io.FileHandler.read(
        directory=SCHEMA_DIR, file_name=schema["entry"]
    )

    return re.findall(SPECIFIED_ELEMENTS, schema_content)


@pytest.fixture(scope="session")
def odds() -> list[tuple[Schema, list[ElName]]]:
    """Compile all odds found in the pyproject.toml to odds and RelaxNG files. Return as a list of Schema objects."""
    config = load_config()

    if config is None:
        raise ValueError("No config file found")

    return [
        (
            odd_factory(schema, authors=config.authors),
            extract_specified_elements_for_rng(schema),
        )
        for schema in config.schemas
    ]


@pytest.fixture(scope="session")
def change_rng_start_per_odd(
    odds: list[tuple[Schema, list[ElName]]],
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
def find_schema_by_name(
    odds: list[tuple[Schema, list[ElName]]],
) -> Callable[[str], Schema]:
    """A fixture, which returns the main ssrq schema."""
    try:
        return lambda name: [odd for odd, _ in odds if odd.name == name][0]
    except IndexError:
        raise ValueError("No schema with this name found")


@pytest.fixture(scope="session")
def main_constraints(find_schema_by_name: Callable[[str], Schema]) -> str:
    """A fixture, which returns the schematron rules from the main schema."""
    extracted_rules = extract_schematron_from_relaxng(
        find_schema_by_name("TEI_Schema").rng
    )

    return create_schematron_stylesheet(extracted_rules)


@pytest.fixture(scope="session")
def lit_constraints(find_schema_by_name: Callable[[str], Schema]) -> str:
    """A fixture, which returns the schematron rules from the Lit schema."""
    extracted_rules = extract_schematron_from_relaxng(
        find_schema_by_name("TEI_Lit").rng
    )

    return create_schematron_stylesheet(extracted_rules)


@pytest.fixture(scope="session")
def intro_constraints(find_schema_by_name: Callable[[str], Schema]) -> str:
    """A fixture, which returns the schematron rules from the Intro schema."""
    extracted_rules = extract_schematron_from_relaxng(
        find_schema_by_name("TEI_Intro").rng
    )

    return create_schematron_stylesheet(extracted_rules)


RNG_test_function: TypeAlias = Callable[
    [str, str, str, bool, bool],
    list[RNGValidationInfos] | None,
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
            element_name (str): The name (without namespace) of the element to test.
            name (str): The name of the file to write / the name of the testcase.
            markup (str): The markup to write to the file.
            result (bool): The expected result of the validation.
            return_validator (bool, optional): If True, the validator object is returned. Defaults to False.

        Returns:
            None: The test passes if the validation result matches the expected result.
        """

        writer.write(name, add_tei_namespace(markup))

        match validate_with_rng(
            writer.construct_file_pattern(), element_schema[element_name]
        ):
            case Ok(validation_infos):
                assert (
                    len(validation_infos) == 0 if result else len(validation_infos) > 0
                )
                return validation_infos if return_validator else None
            case Err(error):
                pytest.fail(
                    f"An error occurred while validating »{element_name}«: {error}"
                )

    return test_element


@pytest.fixture(scope="function")
def test_intro_with_rng(
    intro_schema: dict[str, str],
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
            element_name (str): The name (without namespace) of the element to test.
            name (str): The name of the file to write / the name of the testcase.
            markup (str): The markup to write to the file.
            result (bool): The expected result of the validation.
            return_validator (bool, optional): If True, the validator object is returned. Defaults to False.

        Returns:
            None: The test passes if the validation result matches the expected result.
        """
        writer.write(name, add_tei_namespace(markup))

        match validate_with_rng(
            writer.construct_file_pattern(), intro_schema[element_name]
        ):
            case Ok(validation_infos):
                assert (
                    len(validation_infos) == 0 if result else len(validation_infos) > 0
                )
                return validation_infos if return_validator else None
            case Err(error):
                pytest.fail(
                    f"An error occurred while validating »{element_name}«: {error}"
                )

    return test_element


@pytest.fixture(scope="function")
def test_lit_with_rng(
    lit_schema: dict[str, str],
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
            element_name (str): The name (without namespace) of the element to test.
            name (str): The name of the file to write / the name of the testcase.
            markup (str): The markup to write to the file.
            result (bool): The expected result of the validation.
            return_validator (bool, optional): If True, the validator object is returned. Defaults to False.

        Returns:
            None: The test passes if the validation result matches the expected result.
        """
        writer.write(name, add_tei_namespace(markup))

        match validate_with_rng(
            writer.construct_file_pattern(), lit_schema[element_name]
        ):
            case Ok(validation_infos):
                assert (
                    len(validation_infos) == 0 if result else len(validation_infos) > 0
                )
                return validation_infos if return_validator else None
            case Err(error):
                pytest.fail(
                    f"An error occurred while validating »{element_name}«: {error}"
                )

    return test_element


@pytest.fixture
def element_schema(
    change_rng_start_per_odd: dict[str, dict[str, str]],
) -> dict[str, str]:
    """A fixture, which returns the main ssrq schema with a modified start element."""
    return change_rng_start_per_odd["TEI_Schema"]


@pytest.fixture
def intro_schema(
    change_rng_start_per_odd: dict[str, dict[str, str]],
) -> dict[str, str]:
    """A fixture, which returns the ssrq intro schema with a modified start element."""
    return change_rng_start_per_odd["TEI_Intro"]


@pytest.fixture
def lit_schema(
    change_rng_start_per_odd: dict[str, dict[str, str]],
) -> dict[str, str]:
    """A fixture, which returns the ssrq intro schema with a modified start element."""
    return change_rng_start_per_odd["TEI_Lit"]
