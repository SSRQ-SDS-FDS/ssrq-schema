import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-orig-without-xml-lang",
            "<orig>bar</orig>",
            False,
        ),
        (
            "invalid-orig-with-entity-content",
            "<orig><persName ref='per123456'>bar</persName></orig>",
            False,
        ),
        (
            "valid-orig-with-xml-lang-attribute",
            "<orig xml:lang='de'>foo</orig>",
            True,
        ),
        (
            "valid-orig-with-gap",
            "<orig xml:lang='de'>foo <gap/> bar</orig>",
            True,
        ),
    ],
)
def test_orig(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("orig", name, markup, result, False)
