import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orig",
            "<orig>bar</orig>",
            True,
        ),
        (
            "valid-orig-with-entity-content",
            "<orig><persName ref='per123456'>bar</persName></orig>",
            True,
        ),
        (
            "valid-orig-with-xml-lang-attribute",
            "<orig xml:lang='de'>foo</orig>",
            True,
        ),
    ],
)
def test_orig(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("orig", name, markup, result, False)
