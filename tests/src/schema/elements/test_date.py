import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-date-with-when",
            "<date when='1756-02-12' calendar='gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-notBefore-notAfter",
            """
            <date notBefore-custom='1510-01-01' notAfter-custom='1515-12-12' calendar='julian'>
                ca. 1510
            </date>
            """,
            True,
        ),
        (
            "valid-date-with-dur-iso",
            "<date dur-iso='R/P3.5Y'>Alle drei einhalb Jahre</date>",
            True,
        ),
        (
            "valid-date-with-period",
            "<date period='summer'>es war im Sommer</date>",
            True,
        ),
        (
            "valid-date-with-period-and-type",
            "<date period='summer' type='holiday'>es war im Sommer</date>",
            True,
        ),
        (
            "valid-date-with-type-holiday",
            "<date type='holiday'><persName ref='per000351'>Paul</persName>i</date>",
            True,
        ),
        (
            "valid-date-with-precision",
            """
            <date calendar='julian' notBefore-custom='1341-01-01' notAfter-custom='1355-12-31'>
                Um 1346 und um 1350 
                <precision precision='low' match='@notBefore-custom @notAfter-custom'/>
            </date>
            """,
            True,
        ),
    ],
)
def test_date_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("date", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-date-outside-teiHeader-with-content",
            """
            <text>
                <date when-custom="2000-01-01" calendar="gregorian">foo</date>
            </text>
            """,
            True,
        ),
        (
            "valid-date-outside-teiHeader-with-child",
            """
            <text>
                <date when-custom="2000-01-01" calendar="gregorian">
                    <orig>foo</orig>
                </date>
            </text>
            """,
            True,
        ),
        (
            "invalid-date-outside-publication-stmt-without-calendar",
            """
            <text>
                <date when-custom="2000-01-01">Foo</date>
            </text>    
            """,
            False,
        ),
        (
            "invalid-date-outside-teiHeader-without-content",
            """
            <text>
                <date type="print" when-custom="2000-01-01" calendar="gregorian"/>
            </text>
            """,
            False,
        ),
        (
            "valid-date-in-publication-stmt-without-content-with-type-print-and-with-when",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="print" when-custom="2000-01-01"/>
                </publicationStmt>   
            </teiHeader>
            """,
            True,
        ),
        (
            "invalid-date-in-publication-stmt-with-content",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="print" when-custom="2000-01-01">foo</date>
                </publicationStmt>   
            </teiHeader>
            """,
            False,
        ),
        (
            "invalid-date-in-publication-stmt-with-child",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="print" when-custom="2000-01-01"><orig>foo</orig></date>
                </publicationStmt>   
            </teiHeader>
            """,
            False,
        ),
        (
            "valid-date-in-publication-stmt-with-type-electronic",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="electronic" when-custom="2000-01-01"/>
                </publicationStmt>   
            </teiHeader>
            """,
            True,
        ),
        (
            "invalid-date-in-publication-stmt-with-wrong-type",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="holiday" when-custom="2000-01-01"/>
                </publicationStmt>   
            </teiHeader>
            """,
            False,
        ),
        (
            "valid-date-in-publication-stmt-with-from-to",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="print" from-custom="2000-01-01" to-custom="2000-12-31"/>
                </publicationStmt>   
            </teiHeader>
            """,
            True,
        ),
        (
            "invalid-date-in-publication-stmt-with-calendar",
            """
            <teiHeader>
                <publicationStmt>
                    <date type="print" when-custom="2000-01-01" calendar="gregorian"/>
                </publicationStmt>   
            </teiHeader>
            """,
            False,
        ),
    ],
)
def test_date_constraints(
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
