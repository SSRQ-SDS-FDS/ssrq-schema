import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-unclear-with-text",
            "<unclear>foo</unclear>",
            True,
        ),
        (
            "valid-unclear-with-content-default",
            "<unclear><del>foo</del> bar</unclear>",
            True,
        ),
        (
            "invalid-unclear-with-wrong-content",
            "<unclear><p>foo</p></unclear>",
            False,
        ),
        (
            "invalid-unclear-with-reason",
            "<unclear reason='bar'>foo</unclear>",
            False,
        ),
        (
            "invalid-unclear-with-agent",
            "<unclear agent='water'>foo</unclear>",
            False,
        ),
        (
            "valid-unclear-with-cert",
            "<unclear cert='low'>foo</unclear>",
            True,
        ),
    ],
)
def test_unclear(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("unclear", name, markup, result, False)
