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
            "valid-num-with-fraction",
            "<num value='1.25'>5/4</num>",
            True,
        ),
        (
            "invalid-num-with-decimal-fraction",
            "<num value='3.1/2'>dreieinhalb</num>",
            False,
        ),
        (
            "valid-num-with-hi-content",
            "<num value='1'><hi rend='italic'>foo</hi></num>",
            True,
        ),
        (
            "valid-num-with-lb-content",
            "<num value='1'><lb/>foo</num>",
            True,
        ),
        (
            "valid-num-with-pb-content",
            "<num value='1'><pb n='1'/>foo</num>",
            True,
        ),
        (
            "invalid-num-with-wrong-content",
            "<num value='1'><p>foo</p></num>",
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
