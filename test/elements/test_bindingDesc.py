import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-bindingDesc",
            "<bindingDesc><p>foo</p></bindingDesc>",
            True,
        ),
        (
            "invalid-bindingDesc-without-p",
            "<bindingDesc>foo</bindingDesc>",
            False,
        ),
    ],
)
def test_bindingDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("bindingDesc", name, markup, result, False)
