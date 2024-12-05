import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-abbr",
            "<abbr>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-hi",
            "<abbr><hi rend='sup'>foo</hi>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-lb",
            "<abbr>foo<lb/>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-sic",
            "<abbr><sic>foobar</sic></abbr>",
            True,
        ),
        (
            "valid-abbr-with-unclear",
            "<abbr><unclear>foobar</unclear></abbr>",
            True,
        ),
    ],
)
def test_abbr(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("abbr", name, markup, result, False)
