import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-list",
            "<list><item>foo</item></list>",
            True,
        ),
        (
            "invalid-list",
            "<list/>",
            False,
        ),
    ],
)
def test_list(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("list", name, markup, result, False)
