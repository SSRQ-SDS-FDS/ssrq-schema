import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-add",
            "<add place='left_top'>bar</add>",
            True,
        ),
        (
            "valid-add-with-type",
            "<add place='left_top' type='sign'>bar</add>",
            True,
        ),
        (
            "valid-add-with-hand",
            "<add place='left_top' hand='foo'>bar</add>",
            True,
        ),
        (
            "valid-add-with-rend",
            "<add place='left_top' rend='pencil'>bar</add>",
            True,
        ),
        (
            "valid-add-with-p-content",
            "<add place='left_top'><p>bar</p></add>",
            True,
        ),
        (
            "valid-add-with-seg-content",
            "<add place='left_top'><seg>foo</seg><seg>bar</seg></add>",
            True,
        ),
        (
            "invalid-add-with-one-seg",
            "<add place='left_top'><seg>foo</seg></add>",
            False,
        ),
        (
            "invalid-add-with-mixed-content",
            "<add place='left_top'><seg>bar</seg> foo <unclear>bar</unclear></add>",
            False,
        ),
        (
            "valid-add-with-mixed-content",
            "<add place='left_top'><del>bar</del> foo <unclear>bar</unclear></add>",
            True,
        ),
        (
            "invalid-add-without-place",
            "<add>bar</add>",
            False,
        ),
    ],
)
def test_add(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("add", name, markup, result, False)
