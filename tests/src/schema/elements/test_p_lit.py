import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-p",
            "<p>foo</p>",
            True,
        ),
        (
            "invalid-p-with-n",
            "<p n='1'>foo</p>",
            False,
        ),
        (
            "invalid-p-with-xml-lang",
            "<p xml:lang='de'>foo</p>",
            False,
        ),
        (
            "invalid-p-with-other-content",
            "<p><list><item>bar</item></list></p>",
            False,
        ),
    ],
)
def test_p(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("p", name, markup, result, False)
