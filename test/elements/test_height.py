from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-height",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-height-missing-unit",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3'/>",
            False,
        ),
        (
            "invalid-height-wrong-unit",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-height-wrong-quantity",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='bar' unit='cm'/>",
            False,
        ),
    ],
)
def test_height(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("height", name, markup, result, False)
