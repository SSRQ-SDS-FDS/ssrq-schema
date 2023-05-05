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
