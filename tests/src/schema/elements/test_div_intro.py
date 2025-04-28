import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div-with-type",
            "<div type='chapter'><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-n",
            "<div n='1'><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-p",
            "<div><p>foo</p></div>",
            True,
        ),
        (
            "invalid-div-with-list",
            "<div><list><item>foo</item></list></div>",
            False,
        ),
        (
            "invalid-div-with-one-div",
            "<div><div><p>foo</p></div></div>",
            False,
        ),
        (
            "valid-div-with-two-divs",
            "<div><div><p>foo</p></div><div><p>bar</p></div></div>",
            True,
        ),
        (
            "valid-div-with-two-divs-head",
            """
            <div>
                <head>foo</head>
                <div><p>foo</p></div>
                <div><p>bar</p></div>
            </div>
            """,
            True,
        ),
    ],
)
def test_div(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("div", name, markup, result, False)
