import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-p-with-gi",
            "<p><gi>foo</gi></p>",
            True,
        ),
        (
            "invalid-p-with-n",
            "<p n='1'><gi>foo</gi></p>",
            False,
        ),
        (
            "invalid-p-with-xml-lang",
            "<p xml:lang='fr'><gi>foo</gi></p>",
            False,
        ),
        (
            "invalid-p-with-seg",
            "<p><seg>foo</seg><seg>bar</seg></p>",
            False,
        ),
    ],
)
def test_p(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("p", name, markup, result, False)
