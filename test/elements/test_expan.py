from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-expan",
            "<expan>bar</expan>",
            True,
        ),
        (
            "valid-expan-with-entity-content",
            "<expan><persName ref='per123456'>bar</persName></expan>",
            True,
        ),
        (
            "invalid-expan-with-wrong-attribute",
            "<expan att='foo'>bar</expan>",
            False,
        ),
        (
            "invalid-expan-with-wrong-content",
            "<expan><p>bar</p></expan>",
            False,
        ),
    ],
)
def test_expan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("expan", name, markup, result, False)
