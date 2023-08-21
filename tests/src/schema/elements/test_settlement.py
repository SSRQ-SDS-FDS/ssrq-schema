import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-settlement",
            "<settlement ref='loc000001' xml:lang='de'>foo</settlement>",
            True,
        ),
        (
            "invalid-settlement",
            "<settlement ref='loc000001' xml:lang='de'><p>bar</p></settlement>",
            False,
        ),
        (
            "settlement-with-invalid-ref",
            "<settlement ref='abcdef' xml:lang='de'>foo</settlement>",
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
