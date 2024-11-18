import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName",
            "<orgName ref='org000001'>bar</orgName>",
            True,
        ),
        (
            "valid-orgName-with-role",
            "<orgName ref='org000001' role='recipient'>bar</orgName>",
            True,
        ),
        (
            "orgName-with-invalid-role",
            "<orgName ref='org000001' role='xyz'>bar</orgName>",
            False,
        ),
    ],
)
def test_orgName(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("orgName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName-inside-respStmt",
            "<respStmt><orgName>Fondation des sources du droit de la Société suisse des juristes</orgName></respStmt>",
            True,
        ),
        (
            "valid-orgName-inside-respStmt",
            "<respStmt><orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName></respStmt>",
            True,
        ),
        (
            "invalid-orgName-inside-respStmt-with-attr",
            "<respStmt><orgName ref='bar'>Fondation des sources du droit de la Société suisse des juristes</orgName></respStmt>",
            False,
        ),
        (
            "orgName-inside-respStmt-with-invalid-content",
            "<seriesStmt><respStmt><orgName>bar</orgName></respStmt></seriesStmt>",
            False,
        ),
    ],
)
def test_orgName_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
