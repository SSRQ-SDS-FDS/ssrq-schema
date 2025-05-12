import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-note-with-text-content",
            "<note>foo</note>",
            True,
        ),
        (
            "valid-note-with-bibl",
            "<note><bibl>foo</bibl></note>",
            True,
        ),
        (
            "valid-note-with-ref",
            "<note><ref>foo</ref></note>",
            False,
        ),
        (
            "valid-note-with-xml:id",
            "<note xml:id='note-28'>foo</note>",
            True,
        ),
    ],
)
def test_note(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("note", name, markup, result, False)
