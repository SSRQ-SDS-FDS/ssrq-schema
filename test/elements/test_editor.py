import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editor-with-persName",
            "<editor xmlns='http://www.tei-c.org/ns/1.0'><persName>Friedrich Emil Welti</persName></editor>",
            True,
        ),
        (
            "valid-editor-with-text",
            "<editor xmlns='http://www.tei-c.org/ns/1.0'>Friedrich Emil Welti</editor>",
            True,
        ),
        (
            "invalid-editor-with-p",
            "<editor xmlns='http://www.tei-c.org/ns/1.0'><p>Friedrich Emil Welti</p></editor>",
            False,
        ),
    ],
)
def test_editor_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("editor", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editor-with-persName-in-titleStmt",
            "<titleStmt xmlns='http://www.tei-c.org/ns/1.0'><editor><persName>Friedrich Emil Welti</persName></editor></titleStmt>",
            True,
        ),
        (
            "invalid-editor-with-persName-in-titleStmt",
            "<titleStmt xmlns='http://www.tei-c.org/ns/1.0'><editor>Friedrich Emil Welti</editor></titleStmt>",
            False,
        ),
    ],
)
def test_editor_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints definid for tei:editor."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
