import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pc",
            "<pc>;</pc>",
            True,
        ),
        (
            "invalid-pc-with-multiple-chars",
            "<pc>;:</pc>",
            False,
        ),
        (
            "invalid-pc-with-wrong-char",
            "<pc>-</pc>",
            False,
        ),
        (
            "invalid-pc-with-attribute",
            "<pc unit='c'>;</pc>",
            False,
        ),
    ],
)
def test_pc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pc", name, markup, result, False)
