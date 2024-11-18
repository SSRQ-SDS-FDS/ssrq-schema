import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pb",
            "<pb n='1'/>",
            True,
        ),
        (
            "valid-pb-with-type",
            "<pb n='1' type='original'/>",
            True,
        ),
        (
            "valid-pb-with-facs",
            "<pb n='1' facs='StAZH_F_III_12_Nr_1_S_10'/>",
            True,
        ),
    ],
)
def test_pb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pb", name, markup, result, False)
