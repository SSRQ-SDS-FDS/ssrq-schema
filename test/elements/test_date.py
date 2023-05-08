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
            "<date when-custom='1756-02-12' datingMethod='Gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "date-with-valid-when-without-year",
            "<date when-custom='--02-12' datingMethod='Gregorian'>12. Februar</date>",
            True,
        ),
        (
            "date-with-invalid-when-month-too-large",
            "<date when-custom='1756-92-12' datingMethod='Gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "date-with-invalid-when-year-only",
            "<date when-custom='1756' datingMethod='Gregorian'>1756</date>",
            False,
        ),
        (
            "date-with-when-instead-of-when-custom",
            "<date when='1756-02-12' datingMethod='Gregorian'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date datingMethod='Julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-from-to",
            "<date datingMethod='Julian' from-custom='1501' to-custom='1600'>15. Jahrhundert</date>",
            False,
        ),
        (
            "valid-date-with-notBefore-notAfter",
            "<date datingMethod='Julian' from-custom='1510-01-01' notAfter-custom='1515-12-12'>ca. 1510</date>",
            True,
        ),
        (
            "date-with-invalid-notBefore-notAfter",
            "<date datingMethod='Julian' from-custom='1510' notAfter-custom='1515'>ca. 1510</date>",
            False,
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
            "<date when-custom='1756-02-12' datingMethod='Gregorian'>12. Februar 1756</date>",
            True,
        ),
        (
            "invalid-date-without-datingMethod",
            "<date when-custom='1756-02-12'>12. Februar 1756</date>",
            False,
        ),
        (
            "valid-date-with-from-to",
            "<date datingMethod='Julian' from-custom='1583-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
            True,
        ),
        (
            "date-with-invalid-timespan",
            "<date datingMethod='Julian' from-custom='1589-05-30' to-custom='1584-05-21'>von Pfingstmontag 1583 bis Pfingstmontag 1584</date>",
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
