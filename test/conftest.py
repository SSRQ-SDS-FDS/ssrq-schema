from dataclasses import dataclass
from pathlib import Path

import pytest
from pyschval.main import XSLT_FILES, extract_schematron_from_relaxng

from main import Schema, load_config, odd_factory


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


@pytest.fixture
def odds() -> list[Schema]:
    """Compile all odds found in the pyproject.toml to odds and RelaxNG files. Return as a list of Schema objects."""
    config = load_config()

    if config is None:
        raise ValueError("No config file found")

    odds = [odd_factory(schema, authors=config.authors) for schema in config.schemas]

    return odds


@pytest.fixture
def constraints(odds: list[Schema]):
    """A fixture, which extracts all schematron rules from the RNG files and returns them as a list of FileConstraints –
    one for each ODD file."""
    constraints = [
        FileConstraints(
            odd.name,
            extract_schematron_from_relaxng(odd.rng, XSLT_FILES["extract-sch"]),
        )
        for odd in odds
    ]

    return constraints


@pytest.fixture(scope="function")
def writer(tmp_path: Path) -> SimpleTEIWriter:
    """A fixture, which returns a SimpleTEIWriter object, which can be used to write TEI files to a temporary directory."""
    return SimpleTEIWriter(tmp_path)
