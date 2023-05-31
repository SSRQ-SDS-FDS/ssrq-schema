import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-num-with-int",
            "<num value='1'>I</num>",
            True,
        ),
        (
            "invalid-num-with-roman-value",
            "<num value='I'>I</num>",
            False,
        ),
        (
            "invalid-num-without-value",
            "<num>I</num>",
            False,
        ),
        (
            "valid-num-with-floating-point",
            "<num value='3.5'>dreieinhalb</num>",
            True,
        ),
        (
            "num-with-invalid-floating-point",
            "<num value='3.1/2'>dreieinhalb</num>",
            False,
        ),
    ],
)
def test_num(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("num", name, markup, result, False)
