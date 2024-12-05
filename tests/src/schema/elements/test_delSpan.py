import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-delSpan",
            "<p><delSpan spanTo='del1'/><anchor xml:id='del1'/></p>",
            True,
        ),
        (
            "valid-delSpan-with-rend",
            "<p><delSpan spanTo='del1' rend='crossout'/><anchor xml:id='del1'/></p>",
            True,
        ),
        (
            "valid-delSpan-with-hand",
            "<p><delSpan spanTo='del1' hand='otherHand'/><anchor xml:id='del1'/></p>",
            True,
        ),
        (
            "invalid-delSpan-without anchor",
            "<p><delSpan spanTo='del1'/></p>",
            False,
        ),
        (
            "invalid-delSpan-with-content",
            "<p><delSpan spanTo='del1'>Foo</delSpan><anchor xml:id='del1'/></p>",
            False,
        ),
    ],
)
def test_del_span(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("p", name, markup, result, False)
    # In this test, the surrounding p element is the root for the test, because delSpan always
    # needs a corresponding element with a xml:id to be valid. If delSpam was the root, all
    # rng-tests would fail.
