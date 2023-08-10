import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            "<text type='transcript'><body><div><p>foo</p></div></body></text>",
            True,
        ),
        (
            "valid-text",
            "<text type='transcript'><body><div><p>bar</p></div></body><back><div><p>foo</p></div></back></text>",
            True,
        ),
        (
            "valid-text-with-valid-attribute",
            "<text type='summary'><body><div><p>hallo welt!</p></div></body></text>",
            True,
        ),
        (
            "invalid-text-without-type",
            "<text><body><div><p>hallo welt!</p></div></body></text>",
            False,
        ),
        (
            "invalid-text-with-back-only",
            "<text type='summary'><back><div><p>foo</p></div></back></text>",
            False,
        ),
        (
            "invalid-text-with-invalid-attribute",
            "<text type='foobar'><body><div><p>hallo welt!</p></div></body></text>",
            False,
        ),
        (
            "invalid-text-with-group",
            "<text type='summary'><group><body><div><p>hallo welt!</p></div></body></group></text>",
            False,
        ),
    ],
)
def test_text(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("text", name, markup, result, False)
