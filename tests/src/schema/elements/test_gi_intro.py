import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-gi",
            "<gi>p</gi>",
            True,
        ),
        (
            "invalid-gi-with-direct-tag",
            "<gi><p>foo</p></gi>",
            False,
        ),
    ],
)
def test_gi_rng(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("gi", name, markup, result, False)
