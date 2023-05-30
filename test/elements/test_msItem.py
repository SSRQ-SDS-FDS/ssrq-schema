import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msItem",
            "<msItem><textLang xml:lang='de'/><filiation type='current'>Original</filiation></msItem>",
            True,
        ),
        (
            "invalid-msItem",
            "<msItem><textLang xml:lang='de'/></msItem>",
            False,
        ),
    ],
)
def test_msItem(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msItem", name, markup, result, False)
