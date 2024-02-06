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
            "valid-corr-with-entity-content",
            "<corr><persName ref='per123456'>bar</persName></corr>",
            True,
        ),
        (
            "valid-corr-with-resp-attribute",
            "<corr resp='BAR'>foo</corr>",
            True,
        ),
        (
            "invalid-corr-with-wrong-attribute",
            "<corr att='foo'>bar</corr>",
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
