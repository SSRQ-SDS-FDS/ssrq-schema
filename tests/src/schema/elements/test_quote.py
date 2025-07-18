import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-quote",
            "<quote>foo</quote>",
            True,
        ),
        (
            "valid-quote-with-content-default",
            "<quote><del>foo</del> bar</quote>",
            True,
        ),
        (
            "valid-quote-with-two-segs",
            "<quote><seg>1</seg><seg>2</seg></quote>",
            True,
        ),
        (
            "valid-quote-with-paragraphs",
            "<quote><p>1</p><p>2</p></quote>",
            True,
        ),
        (
            "ivalid-quote-with-paragraph",
            "<quote><p>1</p></quote>",
            False,
        ),
        (
            "invalid-quote-with-paragraph-and-seg",
            "<quote><p>1</p><p>2</p><seg>3</seg><seg>4</seg></quote>",
            False,
        ),
        (
            "invalid-quote-with-mixed-content",
            "<quote><seg>1</seg>baz</quote>",
            False,
        ),
        (
            "invalid-quote-with-wrong-content",
            "<quote><p>foo</p></quote>",
            False,
        ),
        (
            "valid-quote-with-type",
            "<quote type='fully_inserted'>foo</quote>",
            True,
        ),
        (
            "valid-quote-with-source",
            "<quote source='http://foo.bar'>foo</quote>",
            True,
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
            "<div><quote>foo</quote><note>bar</note></div>",
            True,
        ),
        (
            "invalid-quote-without-note",
            "<div><quote>foo</quote></div>",
            False,
        ),
        (
            "valid-quote-without-note-inside-back",
            "<back><quote>foo</quote></back>",
            True,
        ),
    ],
)
def test_quote_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
