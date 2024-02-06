import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-subst",
            "<subst><del>foo</del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "valid-subst-add-first",
            "<subst><add place='left_top'>bar</add><del>foo</del></subst>",
            True,
        ),
        (
            "valid-subst-with-lb-and-pb",
            "<subst><del>foo</del><pb/><lb/><add place='inline'>bar</add></subst>",
            True,
        ),
        (
            "invalid-subst-with-attributes",
            "<subst type='bla'><add place='left_top'>bar</add><del>foo</del></subst>",
            False,
        ),
        (
            "invalid-subst-with-wrong-children",
            "<subst><note>bar</note><p>foo</p></subst>",
            False,
        ),
        (
            "invalid-empty-subst",
            "<subst/>",
            False,
        ),
    ],
)
def test_subst(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("subst", name, markup, result, False)
