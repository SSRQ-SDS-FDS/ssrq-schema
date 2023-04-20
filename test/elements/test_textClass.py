from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-textClass",
            "<textClass><keywords><term ref='key000192'/></keywords></textClass>",
            True,
        ),
        (
            "invalid-textClass-without-keywords",
            "<textClass/>",
            False,
        ),
        (
            "invalid-textClass-with-attributes",
            "<textClass default='true'><keywords><term ref='key000192'/></keywords></textClass>",
            False,
        ),
    ],
)
def test_textClass_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("textClass", name, markup, result, False)
