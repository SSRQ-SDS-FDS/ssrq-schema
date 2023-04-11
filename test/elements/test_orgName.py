from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001'>bar</orgName>",
            True,
        ),
        (
            "valid-orgName-with-role",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001' role='recipient'>bar</orgName>",
            True,
        ),
        (
            "orgName-with-invalid-ref",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='abcdefg' role='recipient'>bar</orgName>",
            False,
        ),
        (
            "orgName-with-invalid-key",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001' role='xyz'>bar</orgName>",
            False,
        ),
    ],
)
def test_orgName(
        test_element_with_rng: Callable[[str, str, str, bool], None],
        name: str,
        markup: str,
        result: bool,
):
    test_element_with_rng("orgName", name, markup, result)
