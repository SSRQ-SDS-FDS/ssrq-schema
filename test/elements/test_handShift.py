from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'>foo</handShift>",
            False,
        ),
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035807'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
            False,
        ),
    ],
)
def test_handShift(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("handShift", name, markup, result)
