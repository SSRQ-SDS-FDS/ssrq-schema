import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "idno-archive-valid",
            "<idno xml:lang='de' source='http://foo.bar'>foo 123</idno>",
            True,
        ),
        (
            "idno-archive-invalid",
            "<idno xml:lang='de' source='http://foo.bar http://foo.bar'>foo 123</idno>",
            False,
        ),
        (
            "idno-archive-invalid",
            " <idno xml:lang='de' source='foo.bar'>foo</idno>",
            False,
        ),
    ],
)
def test_idno(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("idno", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-series-idno",
            "<seriesStmt><idno>SSRQ-SG-III_4-77-1</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno-without-tradtion-part",
            "<seriesStmt><idno>SSRQ-SG-III_4-77</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno",
            "<seriesStmt><idno>SSRQ-FR-I_2_8-1-1</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno-with-case",
            "<seriesStmt><idno>SDS-NE-4-1.0-1</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno-with-case-and-opening",
            "<seriesStmt><idno>SDS-NE-4-1.A.1-1</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno-for-paratext",
            "<seriesStmt><idno>SDS-NE-4-lit</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno",
            "<seriesStmt><idno type='uuid'>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            True,
        ),
        (
            "invalid-series-idno",
            "<seriesStmt><idno>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            False,
        ),
    ],
)
def test_series_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ms-idno",
            "<msIdentifier><idno xml:lang='de'>bar</idno><repository xml:lang='de'>bar</repository></msIdentifier>",
            True,
        ),
        (
            "invalid-ms-idno",
            "<msIdentifier><idno>bar</idno></msIdentifier>",
            False,
        ),
    ],
)
def test_msIdent_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    if not result:
        errors = []
        if reports[0].report.failed_asserts:
            for error in reports[0].report.failed_asserts:
                errors.append(error.text)
        if reports[0].report.successful_reports:
            for error in reports[0].report.successful_reports:
                errors.append(error.text)

        assert any("idno element needs" in e for e in errors) is True
