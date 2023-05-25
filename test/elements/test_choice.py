from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-choice-with-abbr",
            "<choice><abbr>bar</abbr><expan>foo</expan></choice>",
            True,
        ),
        (
            "valid-choice-with-sic",
            "<choice><sic>bar</sic><corr>foo</corr></choice>",
            True,
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
