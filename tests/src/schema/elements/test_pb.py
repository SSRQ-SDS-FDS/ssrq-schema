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
            "valid-pb-n-with-ab",
            "<pb n='1a'/>",
            True,
        ),
        (
            "valid-pb-as-cover",
            "<pb n='cover'/>",
            True,
        ),
        (
            "valid-pb-digit-dot-digit",
            "<pb n='1.32'/>",
            True,
        ),
        (
            "valid-pb-without-type-with-r",
            "<pb n='12r'/>",
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
        ("pb-with-valid-roman-numerals", "<pb n='MDCLXVI'/>", True),
        (
            "pb-with-invalid-roman-numerals",
            "<pb n='PVI'/>",
            False,
        ),
        (
            "pb-with-section-numbering",
            "<pb n='s1'/>",
            True,
        ),
        ("pb-with-invalid-zero-numbering", "<pb n='0'/>", False),
        ("pb-with-invalid-leading-zero-numbering", "<pb n='01r'/>", False),
    ],
)
def test_pb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pb", name, markup, result, False)
