import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-title",
            "<title>foo</title>",
            True,
        ),
        (
            "valid_title-with-pc",
            "<title>foo<pc>:</pc> bar</title>",
            True,
        ),
        (
            "valid_title-with-hi",
            "<title>foo <hi rend='sup'>bar</hi></title>",
            True,
        ),
        (
            "valid-title-with-xml-lang",
            "<title xml:lang='de'>foo</title>",
            True,
        ),
        (
            "invalid-title-with-level",
            "<title level='a'>foo</title>",
            False,
        ),
        (
            "invalid-title-with-type",
            "<title type='main'>foo</title>",
            False,
        ),
        (
            "invalid-title-with-wrong-content",
            "<title><p>foo</p></title>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("title", name, markup, result, False)
