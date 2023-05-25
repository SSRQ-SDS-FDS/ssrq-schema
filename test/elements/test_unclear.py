import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-unclear-with-text",
            "<unclear cert='high'>foo</unclear>",
            True,
        ),
        (
            "valid-unclear-with-text-and-child",
            "<unclear cert='high'>foo<hi rend='sup'>bar</hi></unclear>",
            True,
        ),
        (
            "invalid-unclear-with-reason",
            "<unclear cert='high' reason='bar'>foo</unclear>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("unclear", name, markup, result, False)
