import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-signed",
            "<signed><persName ref='per008827'>Jean Jacques Purry</persName></signed>",
            True,
        ),
        (
            "invalid-signed-with-attribute",
            "<signed type='foo'><persName ref='per008827'>Jean Jacques Purry</persName></signed>",
            False,
        ),
    ],
)
def test_signed(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("signed", name, markup, result, False)
