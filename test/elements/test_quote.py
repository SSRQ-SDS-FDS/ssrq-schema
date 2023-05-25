import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-quote",
            "<quote>bar baz foo</quote>",
            True,
        ),
        (
            "invalid-quote",
            "<quote xml:lang='fr'>bar baz foo</quote>",
            False,
        ),
    ],
)
def test_quote(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("quote", name, markup, result, False)
