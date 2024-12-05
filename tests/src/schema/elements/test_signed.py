import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-signed",
            "<signed>foo</signed>",
            True,
        ),
        (
            "valid-signed-with-content-default",
            "<signed><del>foo</del> bar</signed>",
            True,
        ),
        (
            "invalid-signed-with-wrong-content",
            "<signed><p>foo</p></signed>",
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
