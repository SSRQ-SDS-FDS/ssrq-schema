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
            "invalid-hi-without-rend",
            "<hi>foo bar</hi>",
            False,
        ),
        (
            "invalid-hi-with-wrong-rend",
            "<hi rend='foo'>foo bar</hi>",
            False,
        ),
    ],
)
def test_hi(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("hi", name, markup, result, False)
