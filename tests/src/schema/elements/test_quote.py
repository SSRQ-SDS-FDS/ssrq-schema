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
            "valid-quote",
            "<quote>bar baz foo</quote>",
            True,
        ),
        (
            "invalid-quote",
            "<quote xml:lang='fr'>bar baz foo</quote>",
            False,
        ),
    ],
)
def test_quote(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("quote", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-quote-with-note",
            "<div><quote>bar baz foo</quote><note>bar baz foo</note></div>",
            True,
        ),
        (
            "invalid-quote-without-note",
            "<div><quote>bar baz foo</quote></div>",
            False,
        ),
        (
            "invalid-quote-with-later-note",
            "<div><quote>bar baz foo</quote><p>foo</p><note>bar baz foo</note></div>",
            False,
        ),
    ],
)
def test_quote_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result