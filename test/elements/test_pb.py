import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pb-with-type",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' type='original'/>",
            True,
        ),
        (
            "valid-pb-without-type",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1'/>",
            True,
        ),
        (
            "valid-pb-with-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen_A_4_328'/>",
            True,
        ),
        (
            "pb-with-invalid-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen_A_4_328u'/>",
            False,
        ),
        (
            "pb-with-invalid-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen A_4_328'/>",
            False,
        ),
        (
            "pb-with-invalid-n",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1XIV'/>",
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
