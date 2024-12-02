import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-settlement-de",
            "<settlement ref='loc123456' xml:lang='de'>foo</settlement>",
            True,
        ),
        (
            "valid-settlement-fr",
            "<settlement ref='loc123456' xml:lang='fr'>foo</settlement>",
            True,
        ),
        (
            "invalid-settlement-it",
            "<settlement ref='loc123456' xml:lang='it'>foo</settlement>",
            False,
        ),
        (
            "invalid-settlement-without-xml-lang",
            "<settlement ref='loc000001'>foo</settlement>",
            False,
        ),
        (
            "invalid-settlement-without-ref",
            "<settlement xml:lang='de'>foo</settlement>",
            False,
        ),
        (
            "invalid-settlement-with-element-content",
            "<settlement ref='loc123456' xml:lang='de'><p>foo</p></settlement>",
            False,
        ),
    ],
)
def test_settlement(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("settlement", name, markup, result, False)
