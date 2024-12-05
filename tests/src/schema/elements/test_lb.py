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
            "valid-lb-with-break",
            "<lb break='no'/>",
            True,
        ),
        (
            "valid-lb-with-facs",
            "<lb facs='StAZH_C_VI_7_3_Nr_1_v2'/>",
            True,
        ),
        (
            "invalid-lb-with-content",
            "<lb>foo</lb>",
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
