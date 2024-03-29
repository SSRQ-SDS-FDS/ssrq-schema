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
            "valid-abbr-with-mixed-content",
            "<abbr><hi rend='sup'>foo</hi>bar</abbr>",
            True,
        ),
        (
            "invalid-abbr-with-attribute",
            "<abbr att='foo'>bar</abbr>",
            False,
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
