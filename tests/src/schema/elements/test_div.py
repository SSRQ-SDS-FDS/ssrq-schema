import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div",
            "<div><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-type-and-n",
            "<div type='chapter' n='1'><p>foo</p></div>",
            True,
        ),
        (
            "invalid-div-with-text-only",
            "<div>foo</div>",
            False,
        ),
        (
            "invalid-div-with-wrong-type",
            "<div type='bar'><p>foo</p></div>",
            False,
        ),
        (
            "invalid-div-with-wrong-attribute",
            "<div wit='bar'><p>foo</p></div>",
            False,
        ),
    ],
)
def test_div(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("div", name, markup, result, False)
