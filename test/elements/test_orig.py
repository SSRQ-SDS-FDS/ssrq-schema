from test.conftest import RNG_test_function

import pytest


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
        (
            "invalid-corr-with-wrong-attribute",
            "<orig att='foo'>bar</orig>",
            False,
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
