import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "date-with-valid-when",
            "<date when-custom='1756-02-12' datingMethod='gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "date-with-valid-when-without-year",
            "<date when-custom='--02-12' datingMethod='gregorian'>12. Februar</date>",
            True,
        ),
        (
            "date-with-invalid-when-month-too-large",
            "<date when-custom='1756-92-12' datingMethod='gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "date-with-invalid-when-year-only",
            "<date when-custom='1756' datingMethod='gregorian'>1756</date>",
            False,
        ),
        (
            "date-with-when-instead-of-when-custom",
            "<date when='1756-02-12' datingMethod='gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date datingMethod='julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-from-to",
            "<date datingMethod='julian' from-custom='1501' to-custom='1600'>15. Jahrhundert</date>",
            False,
        ),
        (
            "valid-date-with-notBefore-notAfter",
            "<date datingMethod='julian' from-custom='1510-01-01' notAfter-custom='1515-12-12'>ca. 1510</date>",
            True,
        ),
        (
            "date-with-invalid-notBefore-notAfter",
            "<date datingMethod='julian' from-custom='1510' notAfter-custom='1515'>ca. 1510</date>",
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
            "date-with-type-holiday-without-period-and-datingMethod",
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
            "<date datingMethod='julian' notBefore-custom='1341-01-01' notAfter-custom='1355-12-31'>Um 1346 und um 1350 <precision precision='low' match='@notBefore-custom @notAfter-custom'/></date>",
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
            "valid-date-with-datingMethod",
            "<date when-custom='1756-02-12' datingMethod='gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "invalid-date-without-datingMethod",
            "<date when-custom='1756-02-12'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date datingMethod='julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-timespan",
            "<date datingMethod='julian' from-custom='1589-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            False,
        ),
        (
            "date-with-valid-dur-iso-without-datingMethod",
            "<date dur-iso='R/P3.5Y'>Alle drei einhalb Jahre</date>",
            True,
        ),
        (
            "valid-date-inside-pubStmt",
            "<publicationStmt><date type='electronic' when-custom='2019-08-15'/></publicationStmt>",
            True,
        ),
        (
            "invalid-date-inside-pubStmt",
            "<publicationStmt><date type='holiday' when-custom='2019-08-15'/></publicationStmt>",
            False,
        ),
    ],
)
def test_date_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
