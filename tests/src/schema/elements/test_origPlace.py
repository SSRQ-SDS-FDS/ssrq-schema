import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origPlace",
            "<origPlace ref='loc000001' type='document'>foo</origPlace>",
            True,
        ),
        (
            "invalid-origPlace-with-element-content",
            "<origPlace ref='loc000001' type='document'><unclear>foo</unclear></origPlace>",
            False,
        ),
        (
            "invalid-origPlace-without-ref",
            "<origPlace type='document'>foo</origPlace>",
            False,
        ),
        (
            "invalid-origPlace-without-type",
            "<origPlace ref='loc123456'>foo</origPlace>",
            False,
        ),
        (
            "valid-origPlace-with-cert",
            "<origPlace ref='loc000001' cert='low' type='document'>foo</origPlace>",
            True,
        ),
    ],
)
def test_orig_place_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origPlace", name, markup, result, False)
