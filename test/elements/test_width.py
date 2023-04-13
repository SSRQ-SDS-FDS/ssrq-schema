from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-width",
            "<width quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-width-missing-unit",
            "<width quantity='3'/>",
            False,
        ),
        (
            "invalid-width-wrong-unit",
            "<width quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-width-wrong-quantity",
            "<width quantity='bar' unit='cm'/>",
            False,
        ),
    ],
)
def test_width(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("width", name, markup, result, False)
