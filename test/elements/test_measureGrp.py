from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measureGrp",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0'><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            True,
        ),
        (
            "invalid-measureGrp-without-content",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
        (
            "invalid-measureGrp-with-attribute",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0' type='foo'><lb/></measureGrp>",
            False,
        ),
        (
            "invalid-measureGrp-with-one-measure",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0'><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            False,
        ),
    ],
)
def test_measureGrp(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("measureGrp", name, markup, result)
