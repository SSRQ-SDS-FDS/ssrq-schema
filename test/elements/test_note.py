import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-note",
            "<note>foo</note>",
            True,
        ),
        (
            "invalid-note-with-anchored",
            "<note anchored='true'>foo</note>",
            False,
        ),
    ],
)
def test_note(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("note", name, markup, result, False)
