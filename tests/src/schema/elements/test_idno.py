import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-idno",
            "<idno>SDS-VD-D_2-1-1</idno>",
            True,
        ),
        (
            "invalid-idno-with-element-content",
            "<idno><p>SDS-VD-D_2-1-1</p></idno>",
            False,
        ),
        (
            "valid-idno-with-xml:lang",
            "<idno xml:lang='de'>foo</idno>",
            True,
        ),
        (
            "valid-idno-with-source",
            "<idno source='http://foo.bar'>foo 123</idno>",
            True,
        ),
        (
            "valid-idno-with-type",
            " <idno type='uuid'>d9bf0588-e28a-4b62-ad82-45b95722d684</idno>",
            True,
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
            "invalid-series-idno-without-tradition-part",
            "<seriesStmt><idno>SSRQ-SG-III_4-77</idno></seriesStmt>",
            False,
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
            "valid-series-idno-uuid",
            "<seriesStmt><idno type='uuid'>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            True,
        ),
        (
            "invalid-series-idno-uuid",
            "<seriesStmt><idno type='uuid'>Foo</idno></seriesStmt>",
            False,
        ),
        (
            "invalid-series-idno-without-type",
            "<seriesStmt><idno>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            False,
        ),
        (
            "invalid-series-idno-with-xml-lang",
            "<seriesStmt><idno xml:lang='de'>SSRQ-SG-III_4-77-1</idno></seriesStmt>",
            False,
        ),
        (
            "valid-ms-idno",
            """
            <msIdentifier><idno xml:lang='de'>bar</idno></msIdentifier>
            """,
            True,
        ),
        (
            "invalid-ms-idno-without-xml-lang",
            "<msIdentifier><idno>bar</idno></msIdentifier>",
            False,
        ),
        (
            "valid-idno-all-unique",
            "<TEI><idno>foo</idno><idno>bar</idno></TEI>",
            True,
        ),
        (
            "invalid-idno-not-unique",
            "<TEI><idno>foo</idno><idno>foo</idno></TEI>",
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

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
