import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-quote",
            "<quote>foo</quote>",
            True,
        ),
        (
            "invalid-quote-with-wrong-content",
            "<quote><p>foo</p></quote>",
            False,
        ),
        (
            "valid-quote-with-type",
            "<quote type='block'>foo</quote>",
            True,
        ),
        (
            "invalid-quote-with-source",
            "<quote source='http://foo.bar'>foo</quote>",
            False,
        ),
    ],
)
def test_quote(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("quote", name, markup, result, False)
