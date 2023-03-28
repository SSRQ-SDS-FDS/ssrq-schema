from dataclasses import dataclass
from pathlib import Path

import pytest
from pyschval.main import (
    XSLT_FILES,
    create_schematron_stylesheet,
    extract_schematron_from_relaxng,
)
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable
from ssrq_cli.xml_utils import ext_etree

from main import XSLTS, Schema, load_config, odd_factory

ELEMENTS = [
    "cell",
    "graphic",
    "handShift",
    "height",
    "idno",
    "measure",
    "measureGrp",
    "orgName",
    "width",
]


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


def change_rng_start(rng: str, name: str) -> str:
    """Change the start element of the RNG file to the given name."""
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=rng)
        xsltproc.set_parameter("start-el-name", proc.make_string_value(name))

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(
            stylesheet_file=str(XSLTS["change-start"])
        )

        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to resolve relative paths")

    return result


@pytest.fixture(scope="session")
def odds() -> list[Schema]:
    """Compile all odds found in the pyproject.toml to odds and RelaxNG files. Return as a list of Schema objects."""
    config = load_config()

    if config is None:
        raise ValueError("No config file found")

    odds = [odd_factory(schema, authors=config.authors) for schema in config.schemas]

    return odds


@pytest.fixture(scope="session")
def change_rng_start_per_odd(odds: list[Schema]) -> dict[str, dict[str, str]]:
    """Change the start element of the RNG file to the given name."""
    return {
        odd.name: {el: change_rng_start(odd.rng, el) for el in ELEMENTS} for odd in odds
    }


@pytest.fixture(scope="function")
def writer(tmp_path: Path) -> SimpleTEIWriter:
    """A fixture, which returns a SimpleTEIWriter object, which can be used to write TEI files to a temporary directory."""
    return SimpleTEIWriter(tmp_path)


@pytest.fixture
def main_schema(odds: list[Schema]) -> Schema:
    """A fixture, which returns the main ssrq schema."""
    try:
        return [odd for odd in odds if odd.name == "TEI_Schema"][0]
    except IndexError:
        raise ValueError("No main schema found")


@pytest.fixture
def main_constraints(main_schema: Schema) -> str:
    """A fixture, which returns the schematron rules from the main schema."""
    extracted_rules = extract_schematron_from_relaxng(
        main_schema.rng, XSLT_FILES["extract-sch"]
    )

    return create_schematron_stylesheet(extracted_rules, XSLT_FILES["schxslt"])
