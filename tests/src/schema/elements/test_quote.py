import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

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
            "valid-quote-with-attributes-fully-inserted",
            "<quote type='fully_inserted' source='http://foo.bar'>bar baz foo</quote>",
            True,
        ),
        (
            "valid-quote-with-attributes-partially-inserted",
            "<quote type='partially_inserted' source='http://foo.bar'>bar baz foo</quote>",
            True,
        ),
        ("valid-quote-with-two-segs", "<quote><seg>1</seg><seg>2</seg></quote>", True),
        (
            "invalid-quote-with-two-seg-default-mixed",
            "<quote><seg>1</seg>baz</quote>",
            False,
        ),
        (
            "quote-with-invalid-attribute",
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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
