import pytest

from ..conftest import RNG_test_function

BODY = "<body><pb type='pdf' n='43' facs='81'/></body>"


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-retro-text", f"<text type='retro'>{BODY}</text>", True),
        ("invalid-transcript-text", f"<text type='transcript'>{BODY}</text>", False),
        ("invalid-text-without-body", "<text type='retro'/>", False),
        ("invalid-text-with-back", f"<text type='retro'>{BODY}<back/></text>", False),
    ],
)
def test_text_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("text", name, markup, result, False)
