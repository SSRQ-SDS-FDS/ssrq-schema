import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName",
            "<orgName>bar</orgName>",
            True,
        ),
        (
            "invalid-orgName-with-content-default",
            "<orgName><del>foo</del> bar</orgName>",
            False,
        ),
        (
            "invalid-orgName-with-wrong-content",
            "<orgName><p>foo</p></orgName>",
            False,
        ),
        (
            "invalid-orgName-with-role",
            "<orgName role='recipient'>bar</orgName>",
            False,
        ),
        (
            "invalid-orgName-with-ref",
            "<orgName ref='org123456'>bar</orgName>",
            False,
        ),
    ],
)
def test_org_name(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("orgName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName-de-inside-seriesStmt",
            "<seriesStmt><orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName></seriesStmt>",
            True,
        ),
        (
            "valid-orgName-fr-inside-seriesStmt",
            "<seriesStmt><orgName>Fondation des sources du droit de la Société suisse des juristes</orgName></seriesStmt>",
            True,
        ),
        (
            "invalid-orgName-inside-seriesStmt",
            "<seriesStmt><orgName>bar</orgName></seriesStmt>",
            False,
        ),
    ],
)
def test_org_name_constraints(
    intro_constraints: str,
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=intro_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
