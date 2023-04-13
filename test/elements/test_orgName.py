from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName",
            "<orgName ref='org000001'>bar</orgName>",
            True,
        ),
        (
            "valid-orgName-with-role",
            "<orgName ref='org000001' role='recipient'>bar</orgName>",
            True,
        ),
        (
            "orgName-with-invalid-ref",
            "<orgName ref='abcdefg' role='recipient'>bar</orgName>",
            False,
        ),
        (
            "orgName-with-invalid-role",
            "<orgName ref='org000001' role='xyz'>bar</orgName>",
            False,
        ),
    ],
)
def test_orgName(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("orgName", name, markup, result, False)
