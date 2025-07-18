import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editor-with-persName",
            "<editor><persName>Friedrich Emil Welti</persName></editor>",
            True,
        ),
        (
            "invalid-editor-with-text",
            "<editor>Friedrich Emil Welti</editor>",
            False,
        ),
        (
            "invalid-editor-with-p",
            "<editor><p>Friedrich Emil Welti</p></editor>",
            False,
        ),
    ],
)
def test_editor_rng(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("editor", name, markup, result, False)
