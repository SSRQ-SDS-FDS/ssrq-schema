import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-foliation",
            "<foliation><p>Foo</p></foliation>",
            True,
        ),
        (
            "invalid-foliation",
            "<foliation>Foo</foliation>",
            False,
        ),
    ],
)
def test_foliation(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("foliation", name, markup, result, False)
