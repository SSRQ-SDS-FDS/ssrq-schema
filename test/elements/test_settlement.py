from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-settlement",
            "<settlement>foo</settlement>",
            True,
        ),
        (
            "invalid-settlement",
            "<settlement><p>bar</p></settlement>",
            False,
        ),
        (
            "valid-settlement-with-ref",
            "<settlement ref='loc000001'>foo</settlement>",
            True,
        ),
        (
            "settlement-with-invalid-ref",
            "<settlement ref='abcdef'>foo</settlement>",
            False,
        ),
    ],
)
def test_settlement(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("settlement", name, markup, result, False)
