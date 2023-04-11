from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-width",
            "<width xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-width-missing-unit",
            "<width xmlns='http://www.tei-c.org/ns/1.0' quantity='3'/>",
            False,
        ),
        (
            "invalid-width-wrong-unit",
            "<width xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-width-wrong-quantity",
            "<width xmlns='http://www.tei-c.org/ns/1.0' quantity='bar' unit='cm'/>",
            False,
        ),
    ],
)
def test_width(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("width", name, markup, result)
