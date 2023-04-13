from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "handShift-valid",
            "<handShift scribe='secondaryHand'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift scribe='secondaryHand'>foo</handShift>",
            False,
        ),
        (
            "handShift-valid",
            "<handShift scribe='per035807'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift scribe='per035'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift scribe='foo'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift scribe='foo'/>",
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
