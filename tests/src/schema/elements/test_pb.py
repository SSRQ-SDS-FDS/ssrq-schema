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
            "<pb n='1' facs='StAZH_F_III_12__Nr_1__S__10'/>",
            True,
        ),
        (
            "valid-pb-with-multiple-facs",
            "<pb n='1' facs='StASH_Ordnungen_A_4_328 StASH_Ordnungen_A_4_328_plica'/>",
            True,
        ),
        (
            "pb-with-invalid-facs",
            "<pb n='1' facs='StASH_Ordnungen_A_4_328u'/>",
            False,
        ),
        (
            "pb-with-invalid-facs",
            "<pb n='1' facs='StASH_Ordnungen A_4_328'/>",
            False,
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
