from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-profileDesc",
            "<profileDesc><textClass><keywords><term ref='key000192'/></keywords></textClass></profileDesc>",
            True,
        ),
        (
            "invalid-profileDesc-without-textClass",
            "<profileDesc><keywords><term ref='key000192'/></keywords></profileDesc>",
            False,
        ),
        (
            "invalid-profileDesc-with-attribute",
            "<profileDesc type='foo'><textClass><keywords><term ref='key000192'/></keywords></textClass></profileDesc>",
            False,
        ),
    ],
)
def test_profileDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("profileDesc", name, markup, result, False)
