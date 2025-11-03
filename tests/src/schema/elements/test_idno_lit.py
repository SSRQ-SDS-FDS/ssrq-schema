import pytest
from pyschval import SchematronResult
from pyschval.schematron.validate import apply_schematron_validation

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-idno",
            "<idno>SDS-VD-D_2-lit</idno>",
            True,
        ),
        (
            "invalid-idno-with-element-content",
            "<idno><p>SDS-VD-D_2-lit</p></idno>",
            False,
        ),
        (
            "invalid-idno-with-xml-lang",
            "<idno xml:lang='de'>foo</idno>",
            False,
        ),
        (
            "invalid-idno-with-source",
            "<idno source='http://foo.bar'>foo</idno>",
            False,
        ),
        (
            "valid-idno-with-type",
            " <idno type='uuid'>d9bf0588-e28a-4b62-ad82-45b95722d684</idno>",
            True,
        ),
    ],
)
def test_idno(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("idno", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-idno",
            "<seriesStmt><idno>SDS-VD-D_2-lit</idno></seriesStmt>",
            True,
        ),
        (
            "invalid-idno",
            "<seriesStmt><idno>SDS-VD-D_2-1-1</idno></seriesStmt>",
            False,
        ),
    ],
)
def test_series_idno_constraints(
    lit_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=lit_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
