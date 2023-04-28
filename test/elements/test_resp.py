from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-resp",
            "<resp key='transcript'/>",
            True,
        ),
        (
            "invalid-resp-with-content",
            "<resp key='transcript'>Walther Merz</resp>",
            False,
        ),
        (
            "resp-with-invalid-key",
            "<resp key='everything'/>",
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
