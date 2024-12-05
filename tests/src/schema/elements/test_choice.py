import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-choice-with-abbr-and-expan",
            "<choice><abbr>bar</abbr><expan>foo</expan></choice>",
            True,
        ),
        (
            "invalid-choice-with-expan-and-abbr",
            "<choice><expan>bar</expan><abbr>foo</abbr></choice>",
            False,
        ),
        (
            "valid-choice-with-sic-and-corr",
            "<choice><sic>bar</sic><corr>foo</corr></choice>",
            True,
        ),
        (
            "invalid-choice-with-corr-and-sic",
            "<choice><corr>bar</corr><sic>foo</sic></choice>",
            False,
        ),
        (
            "invalid-choice-with-other-content",
            "<choice><p>foo</p></choice>",
            False,
        ),
        (
            "invalid-choice-with-attributes",
            "<choice n='foo'><abbr>bar</abbr><expan>foo</expan></choice>",
            False,
        ),
    ],
)
def test_choice(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("choice", name, markup, result, False)
