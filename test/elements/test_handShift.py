from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'>foo</handShift>",
            False,
        ),
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035807'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
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
