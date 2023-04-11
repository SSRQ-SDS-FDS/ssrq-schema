from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-back",
            "<back xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            True,
        ),
        (
            "invalid-back-with-p-only",
            "<back xmlns='http://www.tei-c.org/ns/1.0'><p>foo</p></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back xml:id='bar123' xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back rend='bar' xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            False,
        ),
    ],
)
def test_back(
    test_element_with_rng: Callable[[str, str, str, bool], None],
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("back", name, markup, result)
