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
            "invalid_title-with-pc",
            "<title>foo<pc>:</pc> bar</title>",
            False,
        ),
        (
            "invalid_title-with-hi",
            "<title>foo <hi rend='sup'>bar</hi></title>",
            False,
        ),
        (
            "invalid-title-with-xml-lang",
            "<title xml:lang='de'>foo</title>",
            False,
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
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("title", name, markup, result, False)
