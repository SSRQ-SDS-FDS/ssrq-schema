from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='map' mimeType='image/svg' url='foo.svg'/>",
            True,
        ),
        (
            "valid-graphic",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='familytree' mimeType='image/jpg' url='foo.jpg'/>",
            True,
        ),
        (
            "invalid-graphic-with-content",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='map' mimeType='image/svg' url='foo.png'>bar</graphic>",
            False,
        ),
        (
            "invalid-graphic-with-invalid-type",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='bar' mimeType='image/svg' url='foo.png'/>",
            False,
        ),
    ],
)
def test_graphic(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("graphic", name, markup, result)
