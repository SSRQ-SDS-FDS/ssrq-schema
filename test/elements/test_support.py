import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-support-with-material",
            "<support><material type='paper'/></support>",
            True,
        ),
        (
            "invalid-support-with-material-with-attribute",
            "<support type='foo'><material type='paper'/></support>",
            False,
        ),
        (
            "invalid-support-without-material",
            "<support/>",
            False,
        ),
    ],
)
def test_support_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("support", name, markup, result, False)
