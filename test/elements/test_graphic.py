from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic",
            "<graphic type='map' mimeType='image/svg' url='foo.svg'/>",
            True,
        ),
        (
            "valid-graphic",
            "<graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/>",
            True,
        ),
        (
            "invalid-graphic-with-content",
            "<graphic type='map' mimeType='image/svg' url='foo.png'>bar</graphic>",
            False,
        ),
        (
            "invalid-graphic-with-invalid-type",
            "<graphic type='bar' mimeType='image/svg' url='foo.png'/>",
            False,
        ),
    ],
)
def test_graphic(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("graphic", name, markup, result, False)
