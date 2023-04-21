from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-lem",
            "<lem>bar</lem>",
            True,
        ),
        (
            "invalid-empty-lem",
            "<lem/>",
            True,
        ),
        (
            "lem-with-valid-attribute",
            "<lem xml:id='foo'>bar</lem>",
            False,
        ),
        (
            "lem-with-invalid-attribute",
            "<lem wit='xyz'>bar</lem>",
            False,
        ),
    ],
)
def test_lem(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("lem", name, markup, result, False)
