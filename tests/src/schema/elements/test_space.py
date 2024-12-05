import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-space",
            "<space unit='word' quantity='2'/>",
            True,
        ),
        (
            "invalid-space-without-unit",
            "<space quantity='2'/>",
            False,
        ),
        (
            "invalid-space-without-quantity",
            "<space unit='word'/>",
            False,
        ),
        (
            "invalid-space-with-content",
            "<space unit='word' quantity='2'>foo</space>",
            False,
        ),
        (
            "invalid-space-with-dim",
            "<space unit='word' quantity='2' dim='horizontal'/>",
            False,
        ),
    ],
)
def test_space(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("space", name, markup, result, False)
