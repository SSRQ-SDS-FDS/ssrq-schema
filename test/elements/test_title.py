import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid_title",
            "<title>foo</title>",
            True,
        ),
        (
            "invalid_title",
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
