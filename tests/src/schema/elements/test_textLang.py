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
            "invalid-textLang-with-mainLang",
            "<textLang mainLang='de'/>",
            False,
        ),
        (
            "invalid-textLang-with-otherLangs",
            "<textLang otherLangs='de'/>",
            False,
        ),
        (
            "invalid-textLang-with-content",
            "<textLang xml:lang='de'>deutsch</textLang>",
            False,
        ),
        (
            "invalid-textLang-without-xml-lang",
            "<textLang/>",
            False,
        ),
    ],
)
def test_text_lang(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("textLang", name, markup, result, False)
