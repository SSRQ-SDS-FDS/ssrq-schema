import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-addSpan",
            "<p><addSpan spanTo='add1'/><anchor xml:id='add1'/></p>",
            True,
        ),
        (
            "valid-addSpan-with-place",
            "<p><addSpan spanTo='add1' place='above'/><anchor xml:id='add1'/></p>",
            True,
        ),
        (
            "valid-addSpan-with-type",
            "<p><addSpan spanTo='add1' type='sign'/><anchor xml:id='add1'/></p>",
            True,
        ),
        (
            "valid-addSpan-with-rend",
            "<p><addSpan spanTo='add1' rend='pencil'/><anchor xml:id='add1'/></p>",
            True,
        ),
        (
            "valid-addSpan-with-hand",
            "<p><addSpan spanTo='add1' hand='otherHand'/><anchor xml:id='add1'/></p>",
            True,
        ),
        (
            "invalid-addSpan-without anchor",
            "<p><addSpan spanTo='add1'/></p>",
            False,
        ),
        (
            "invalid-addSpan-with-content",
            "<p><addSpan spanTo='add1'>Foo</addSpan><anchor xml:id='add1'/></p>",
            False,
        ),
    ],
)
def test_add_span(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("p", name, markup, result, False)
    # In this test, the surrounding p element is the root for the test, because addSpan always
    # needs a corresponding element with a xml:id to be valid. If addSpan was the root, all
    # rng-tests would fail.
