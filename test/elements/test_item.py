import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-item",
            "<item>valid item</item>",
            True,
        ),
        (
            "invalid-item-with-attr",
            "<item n='1'>valid item</item>",
            False,
        ),
    ],
)
def test_item(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("item", name, markup, result, False)
