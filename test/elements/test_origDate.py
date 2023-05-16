import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origDate",
            "<origDate when-custom='1448-05-25' calendar='gregorian'>bar</origDate>",
            True,
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
