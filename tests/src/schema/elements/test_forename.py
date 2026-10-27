import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-forename-with-text-content",
            "<forename>foo</forename>",
            True,
        ),
        (
            "invalid-forename-with-content-default",
            "<forename><del>foo</del> bar</forename>",
            False,
        ),
        (
            "invalid-forname-with-ref",
            "<forename ref='per123456'>bar</forename>",
            False,
        ),
    ],
)
def test_forename(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("forename", name, markup, result, False)
