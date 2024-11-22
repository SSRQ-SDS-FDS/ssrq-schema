import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-del",
            "<del>bar</del>",
            True,
        ),
        (
            "valid-del-with-p-content",
            "<del><p>bar</p></del>",
            True,
        ),
        (
            "valid-del-with-seg-content",
            "<del><seg>foo</seg><seg>bar</seg></del>",
            True,
        ),
        (
            "invalid-del-with-one-seg",
            "<del><seg>foo</seg></del>",
            False,
        ),
        (
            "invalid-del-with-mixed-content",
            "<del><seg>bar</seg> foo <unclear>bar</unclear></del>",
            False,
        ),
        (
            "valid-del-with-mixed-content",
            "<del><add place='above'>bar</add> foo <unclear>bar</unclear></del>",
            True,
        ),
        (
            "valid-del-with-rend",
            "<del rend='crossout'>bar</del>",
            True,
        ),
        (
            "valid-del-with-hand",
            "<del hand='otherHand'>bar</del>",
            True,
        ),
    ],
)
def test_del(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("del", name, markup, result, False)
