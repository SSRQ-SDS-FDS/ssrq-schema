import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-lb",
            "<lb/>",
            True,
        ),
        (
            "valid-lb-with-attribute",
            "<lb break='no'/>",
            True,
        ),
        (
            "lb-with-invalid-break",
            "<lb break='foo'/>",
            False,
        ),
    ],
)
def test_lb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("lb", name, markup, result, False)
