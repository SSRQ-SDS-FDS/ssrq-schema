from typing import Callable

import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>foo</p></div></body></text>",
            True,
        ),
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>bar</p></div></body><back><div><p>foo</p></div></back></text>",
            True,
        ),
        (
            "valid-text-with-valid-attribute",
            "<text type='summary' xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>hallo welt!</p></div></body></text>",
            True,
        ),
        (
            "invalid-text-with-back-only",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><back><div><p>foo</p></div></back></text>",
            False,
        ),
        (
            "invalid-text-with-invalid-attribute",
            "<text type='foobar' xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>hallo welt!</p></div></body></text>",
            False,
        ),
        (
            "invalid-text-with-group",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><group><body><div><p>hallo welt!</p></div></body></group></text>",
            False,
        ),
    ],
)
def test_text(
    test_element_with_rng: Callable[[str, str, str, bool], None],
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("text", name, markup, result)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>foo</p></div></body></text>",
            True,
        ),
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body type='summary'><div><p>bar</p></div></body><back><div><p>foo</p></div></back></text>",
            True,
        ),
        (
            "invalid-text-with-type-empty-body",
            "<text type='summary' xmlns='http://www.tei-c.org/ns/1.0'><body/></text>",
            False,
        ),
    ],
)
def test_text_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints definid for tei:text."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
