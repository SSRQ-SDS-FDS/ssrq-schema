import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "date-with-valid-when",
            "<date when-custom='1756-02-12' calendar='gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "date-with-valid-when-without-year",
            "<date when-custom='--02-12' calendar='gregorian'>12. Februar</date>",
            True,
        ),
        (
            "date-with-valid-when-without-year-and-month",
            "<date when-custom='---12' calendar='gregorian'>Immer am 12.</date>",
            True,
        ),
        (
            "date-with-invalid-when-month-too-large",
            "<date when-custom='1756-92-12' calendar='gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "date-with-invalid-when-year-only",
            "<date when-custom='1756' calendar='gregorian'>1756</date>",
            False,
        ),
        (
            "date-with-invalid-when-month-only",
            "<date when-custom='--09' calendar='gregorian'>September</date>",
            False,
        ),
        (
            "date-with-invalid-day",
            "<date when-custom='0001-01-00' calendar='unknown'>foo</date>",
            False,
        ),
        (
            "date-with-invalid-negative-year",
            "<date when-custom='-1337-01-01' calendar='unknown'>foo</date>",
            False,
        ),
        (
            "date-with-when-instead-of-when-custom",
            "<date when='1756-02-12' calendar='gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date calendar='julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-from-to",
            "<date calendar='julian' from-custom='1501' to-custom='1600'>15. Jahrhundert</date>",
            False,
        ),
        (
            "valid-date-with-notBefore-notAfter",
            "<date calendar='julian' from-custom='1510-01-01' notAfter-custom='1515-12-12'>ca. 1510</date>",
            True,
        ),
        (
            "date-with-invalid-notBefore-notAfter",
            "<date calendar='julian' from-custom='1510' notAfter-custom='1515'>ca. 1510</date>",
            False,
        ),
        (
            "date-with-valid-dur-iso-with-decimal",
            "<date dur-iso='R/P3.5Y'>Alle drei einhalb Jahre</date>",
            True,
        ),
        (
            "date-with-valid-dur-iso-with-months",
            "<date dur-iso='R/P3Y6M'>Alle drei einhalb Jahre</date>",
            True,
        ),
        (
            "date-with-invalid-dur-iso",
            "<date dur-iso='P/3Y'>3 Jahre</date>",
            False,
        ),
        (
            "date-with-valid-period",
            "<date period='summer'>es war im Sommer</date>",
            True,
        ),
        (
            "date-with-valid-period-and-type",
            "<date period='summer' type='holiday'>es war im Sommer</date>",
            True,
        ),
        (
            "date-with-type-holiday-without-period-and-calendar",
            "<date type='holiday'><persName ref='per000351'>Paul</persName>i</date>",
            True,
        ),
        (
            "date-with-valid-period-and-invalid-type",
            "<date period='summer' type='summer holiday'>es war im Sommer</date>",
            False,
        ),
        (
            "date-with-invalid-period",
            "<date period='sommer'>es war im Sommer</date>",
            False,
        ),
        (
            "valid-date-with-precision",
            "<date calendar='julian' notBefore-custom='1341-01-01' notAfter-custom='1355-12-31'>Um 1346 und um 1350 <precision precision='low' match='@notBefore-custom @notAfter-custom'/></date>",
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
            "valid-date-with-calendar",
            "<date when-custom='1756-02-12' calendar='gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "invalid-date-without-calendar",
            "<date when-custom='1756-02-12'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date calendar='julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-timespan",
            "<date calendar='julian' from-custom='1589-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            False,
        ),
        (
            "date-with-valid-dur-iso-without-calendar",
            "<date dur-iso='R/P3.5Y'>Alle drei einhalb Jahre</date>",
            True,
        ),
        (
            "valid-date-inside-pubStmt",
            "<teiHeader><publicationStmt><date type='print' when-custom='2019-08-15'/></publicationStmt></teiHeader>",
            True,
        ),
        (
            "valid-date-inside-pubStmt-from-to",
            "<teiHeader><publicationStmt><date type='electronic' from-custom='2019-01-01' to-custom='2019-12-31'/></publicationStmt></teiHeader>",
            True,
        ),
        (
            "invalid-date-inside-pubStmt-from",
            "<teiHeader><publicationStmt><date type='print' from-custom='2019-01-01'/></publicationStmt></teiHeader>",
            False,
        ),
        (
            "invalid-date-inside-pubStmt",
            "<teiHeader><publicationStmt><date type='holiday' when-custom='2019-08-15'/></publicationStmt></teiHeader>",
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
    assert reports[0].report.is_valid() is result
