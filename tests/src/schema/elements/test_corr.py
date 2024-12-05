import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-corr",
            "<corr>bar</corr>",
            True,
        ),
        (
            "valid-corr-with-default-content",
            "<corr><persName ref='per123456'>bar</persName></corr>",
            True,
        ),
        (
            "invalid-corr-with-wrong-content",
            "<corr><div><p>foo</p></div></corr>",
            False,
        ),
        (
            "valid-corr-with-resp",
            "<corr resp='BAR'>foo</corr>",
            True,
        ),
        (
            "invalid-corr-with-cert",
            "<corr cert='high'>foo</corr>",
            False,
        ),
    ],
)
def test_corr(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("corr", name, markup, result, False)
