from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-resp-de",
            "<resp>Transkription</resp>",
            True,
        ),
        (
            "valid-resp-fr",
            "<resp>Transcription</resp>",
            True,
        ),
        (
            "invalid-resp",
            "<resp>foo</resp>",
            False,
        ),
        (
            "resp-without-content",
            "<resp/>",
            False,
        ),
        (
            "invalid-resp-fr-with-key",
            "<resp key='transcript'>Transcription</resp>",
            False,
        ),
    ],
)
def test_resp_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("resp", name, markup, result, False)
