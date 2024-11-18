import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ab-with-text-content",
            "<ab type='dorsal' place='left_margin'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-default-content",
            "<ab type='dorsal' place='left_margin'><persName>Foo</persName> bar</ab>",
            True,
        ),
        (
            "invalid-ab-without-type",
            "<ab place='left_margin'>Foo</ab>",
            False,
        ),
        (
            "invalid-ab-without-place",
            "<ab type='dorsal'>Foo</ab>",
            False,
        ),
        (
            "valid-ab-with-hand",
            "<ab type='dorsal' place='left_margin' hand='hand20cf'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-rend",
            "<ab type='dorsal' place='left_margin' rend='pencil'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-xml-lang",
            "<ab type='dorsal' place='left_margin' xml:lang='de'>Foo</ab>",
            True,
        ),
    ],
)
def test_ab_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("ab", name, markup, result, False)
