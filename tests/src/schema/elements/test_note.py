import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-note",
            "<note>foo</note>",
            True,
        ),
        (
            "valid-note-with-type-and-place",
            "<note type='original' place='left_margin'>foo</note>",
            True,
        ),
        (
            "invalid-note-with-wrong-attribute-value",
            "<note type='foo' place='foo'>foo</note>",
            False,
        ),
        (
            "invalid-note-with-wrong-attribute",
            "<note att='true'>foo</note>",
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


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-note",
            "<note/>",
            False,
        ),
    ],
)
def test_note_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result