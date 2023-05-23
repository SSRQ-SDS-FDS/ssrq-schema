import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-textLang",
            "<textLang xml:lang='de'/>",
            True,
        ),
        (
            "invalid-textLang-with-type",
            "<textLang type='de'/>",
            False,
        ),
        (
            "invalid-textLang-with-content",
            "<textLang xml:lang='de'>deutsch</textLang>",
            False,
        ),
        (
            "invalid-textLang-with-content-and-without-xml-lang",
            "<textLang>deutsch</textLang>",
            False,
        ),
    ],
)
def test_textLang(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("textLang", name, markup, result, False)
