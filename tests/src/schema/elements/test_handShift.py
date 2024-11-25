import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handShift",
            "<handShift hand='secondHand'/>",
            True,
        ),
        (
            "invalid-handShift-with-content",
            "<handShift hand='secondHand'>foo</handShift>",
            False,
        ),
        (
            "invalid-handShift-with-wrong-attribute",
            "<handShift new='foo'/>",
            False,
        ),
        (
            "invalid-handShift-without-attribute",
            "<handShift/>",
            False,
        ),
    ],
)
def test_hand_shift(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handShift", name, markup, result, False)
