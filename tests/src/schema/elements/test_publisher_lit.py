import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publisher",
            "<publisher>SSRQ-SDS-FDS</publisher>",
            True,
        ),
        (
            "invalid-publisher-with-persName",
            "<publisher><persName>foo</persName></publisher>",
            False,
        ),
        (
            "invalid-publisher-with-orgName",
            "<publisher><orgName>Foo und Co.</orgName></publisher>",
            False,
        ),
        (
            "invalid-publisher-with-wrong-content",
            "<publisher><p>foo</p></publisher>",
            False,
        ),
        (
            "invalid-publisher-with-mixed-content",
            "<publisher><orgName>Foo und Co.</orgName> KG</publisher>",
            False,
        ),
        (
            "invalid-publisher-with-cert",
            "<publisher cert='low'>foo</publisher>",
            False,
        ),
    ],
)
def test_publisher(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("publisher", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publisher-with-correct-text-content",
            "<publicationStmt><publisher>SSRQ-SDS-FDS</publisher></publicationStmt>",
            True,
        ),
        (
            "invalid-publisher-with-wrong-text-content",
            "<publicationStmt><publisher>Foo</publisher></publicationStmt>",
            False,
        ),
        (
            "invalid-publisher-with-cert",
            "<publicationStmt><publisher cert='low'>SSRQ-SDS-FDS</publisher></publicationStmt>",
            False,
        ),
    ],
)
def test_publisher_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
