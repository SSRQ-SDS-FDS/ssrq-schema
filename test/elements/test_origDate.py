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
            "valid-origDate",
            "<origDate when-custom='1448-05-25' calendar='gregorian'>bar</origDate>",
            True,
        ),
        (
            "origDate-with-invalid-calendar",
            "<origDate when-custom='1448-05-25' calendar='...'>bar</origDate>",
            False,
        ),
        (
            "invalid-origDate-without-calendar",
            "<origDate when-custom='1448-05-25'>bar</origDate>",
            False,
        ),
        (
            "origDate-with-invalid-calendar",
            "<origDate when-custom='1448-05-25' calendar='Modern'>bar</origDate>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origDate", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origDate",
            "<origDate when-custom='1448-05-25' calendar='gregorian'>bar</origDate>",
            True,
        ),
        (
            "invalid-origDate-with-calendar-only",
            "<origDate calendar='gregorian'>bar</origDate>",
            False,
        ),
    ],
)
def test_origDate_datable_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
