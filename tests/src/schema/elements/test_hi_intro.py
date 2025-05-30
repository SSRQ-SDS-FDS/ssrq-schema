import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-hi",
            "<hi rend='italic'>foo bar</hi>",
            True,
        ),
        (
            "invalid-hi-with-content-default",
            "<hi rend='italic'><del>foo</del> bar</hi>",
            False,
        ),
        (
            "invalid-hi-without-rend",
            "<hi>foo bar</hi>",
            False,
        ),
    ],
)
def test_hi(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("hi", name, markup, result, False)
