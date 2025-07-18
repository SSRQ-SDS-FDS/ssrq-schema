import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-q",
            "<q>foo</q>",
            True,
        ),
        (
            "invalid-q-with-content-default",
            "<q><del>foo</del> bar</q>",
            False,
        ),
        (
            "invalid-q-with-type",
            "<q type='inserted-quote'>valid</q>",
            False,
        ),
    ],
)
def test_q(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("q", name, markup, result, False)
