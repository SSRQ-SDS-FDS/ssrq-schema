from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "handShift-valid",
            "<handShift hand='#secondHand'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift hand='#secondHand'>foo</handShift>",
            False,
        ),
        (
            "handShift-invalid-attribute",
            "<handShift scribe='per035807'/>",
            False,
        ),
        (
            "handShift-invalid-without-attribute",
            "<handShift/>",
            False,
        ),
    ],
)
def test_handShift(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handShift", name, markup, result, False)
