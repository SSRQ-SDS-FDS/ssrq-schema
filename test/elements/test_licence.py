from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-licence",
            "<licence xmlns='http://www.tei-c.org/ns/1.0' target='http://licence.bar'>foo bar</licence>",
            True,
        ),
        (
            "invalid-licence",
            "<licence xmlns='http://www.tei-c.org/ns/1.0' target='licence.bar'>foo bar</licence>",
            False,
        ),
    ],
)
def test_licence(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("licence", name, markup, result)
