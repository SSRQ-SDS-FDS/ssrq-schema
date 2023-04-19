import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pb-with-type",
            "<pb n='1' type='original'/>",
            True,
        ),
        (
            "valid-pb-without-type",
            "<pb n='1'/>",
            True,
        ),
        (
            "valid-pb-with-facs",
            "<pb n='1' facs='StASH_Ordnungen_A_4_328'/>",
            True,
        ),
        (
            "valid-pb-with-facs-roman",
            "<pb n='IV' facs='StASH_Ordnungen_A_4_328'/>",
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
        (
            "pb-with-invalid-mixed-n",
            "<pb n='1XIV'/>",
            False,
        ),
        (
            "pb-with-invalid-roman-n",
            "<pb n='MV'/>",
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
