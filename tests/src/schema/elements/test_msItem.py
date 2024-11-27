import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msItem",
            "<msItem><textLang xml:lang='de'/></msItem>",
            True,
        ),
        (
            "valid-msItem-with-multiple-textLangs",
            "<msItem><textLang xml:lang='de'/><textLang xml:lang='fr'/></msItem>",
            True,
        ),
        (
            "valid-msItem-with-author",
            "<msItem><textLang xml:lang='de'/><author>Foo</author></msItem>",
            True,
        ),
        (
            "valid-msItem-with-multiple-authors",
            "<msItem><textLang xml:lang='de'/><author>Foo</author><author>Bar</author></msItem>",
            True,
        ),
        (
            "valid-msItem-with-docImprint",
            """<msItem>
                <textLang xml:lang='de'/>
                <docImprint>
                    <publisher>Heidegger</publisher>
                </docImprint>
            </msItem>""",
            True,
        ),
        (
            "invalid-msItem-with-wrong-content",
            "<msItem><p>Foo</p></msItem>",
            False,
        ),
    ],
)
def test_ms_item(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msItem", name, markup, result, False)
