import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-p-with-gi",
            "<p><gi>foo</gi></p>",
            True,
        ),
    ],
)
def test_p(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("p", name, markup, result, False)
