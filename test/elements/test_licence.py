from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-licence",
            "<licence target='http://licence.bar'>foo bar</licence>",
            True,
        ),
        (
            "invalid-licence",
            "<licence target='licence.bar'>foo bar</licence>",
            False,
        ),
    ],
)
def test_licence(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("licence", name, markup, result, False)
