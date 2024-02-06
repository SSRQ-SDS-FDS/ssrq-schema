import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editor-with-persName",
            "<editor><persName>Friedrich Emil Welti</persName></editor>",
            True,
        ),
        (
            "valid-editor-with-text",
            "<editor>Friedrich Emil Welti</editor>",
            True,
        ),
        (
            "invalid-editor-with-p",
            "<editor><p>Friedrich Emil Welti</p></editor>",
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
            "<titleStmt><editor><persName>Friedrich Emil Welti</persName></editor></titleStmt>",
            True,
        ),
        (
            "invalid-editor-with-persName-in-titleStmt",
            "<titleStmt><editor>Friedrich Emil Welti</editor></titleStmt>",
            False,
        ),
    ],
)
def test_editor_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
