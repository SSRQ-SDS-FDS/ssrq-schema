import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-resp-de",
            "<resp>Herausgabe</resp>",
            True,
        ),
        (
            "valid-resp-fr",
            "<resp>Publication</resp>",
            True,
        ),
        (
            "invalid-resp",
            "<resp>foo</resp>",
            False,
        ),
        (
            "invalid-resp-fr-with-key",
            "<resp key='transcript'/>",
            False,
        ),
    ],
)
def test_resp_rng(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("resp", name, markup, result, False)
