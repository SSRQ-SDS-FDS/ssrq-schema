import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-date",
            "<date when-custom='2000-01-01' type='print'/>",
            True,
        ),
        (
            "valid-date-with-type-electronic",
            "<date when-custom='2000-01-01' type='electronic'/>",
            True,
        ),
        (
            "invalid-date-with-wrong-type",
            "<date when-custom='2000-01-01' type='deadline'/>",
            False,
        ),
        (
            "invalid-date-with-content",
            "<date when-custom='2000-01-01' type='print'>2000</date>",
            False,
        ),
        (
            "valid-date-with-from-and-to",
            "<date from-custom='2000-01-01' to-custom='2000-12-31' type='print'/>",
            True,
        ),
        (
            "invalid-date-with-calendar",
            "<date when-custom='2000-01-01' calendar='gregorian' type='print'/>",
            False,
        ),
    ],
)
def test_date_rng(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("date", name, markup, result, False)
