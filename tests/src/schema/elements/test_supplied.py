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
            "valid-supplied-source",
            "<supplied source='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</supplied>",
            True,
        ),
        (
            "invalid-supplied-source",
            "<supplied source='bar'>foo</supplied>",
            False,
        ),
        (
            "supplied-valid-with-reason",
            "<supplied reason='omitted'>foo</supplied>",
            True,
        ),
        (
            "supplied-valid-with-resp",
            "<supplied resp='CS'>foo</supplied>",
            True,
        ),
        (
            "supplied-valid-with-multiple-attributes",
            "<supplied resp='CS' reason='omitted'>foo</supplied>",
            True,
        ),
        (
            "supplied-with-invalid-attribute",
            "<supplied cert='bar'>foo</supplied>",
            False,
        ),
    ],
)
def test_supplied(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("supplied", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-supplied-source-with-ref-to-bibl",
            """
            <TEI>
                <bibl xml:id='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</bibl>
                <supplied source='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>
            </TEI>""",
            True,
        ),
        (
            "valid-supplied-source-with-urn:ssrq",
            """
            <TEI>
                <supplied source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1'>foo</supplied>
            </TEI>""",
            True,
        ),
        (
            "invalid-empty-supplied-source-with-ref-to-bibl",
            """
            <TEI>
                <bibl xml:id='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</bibl>
                <supplied source='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'/>
            </TEI>""",
            False,
        ),
        (
            "invalid-supplied-without-attribute",
            "<supplied>foo</supplied>",
            False,
        ),
        (
            "invalid-supplied-with-conflicting-attributes",
            """
            <TEI>
                <bibl xml:id='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</bibl>
                <supplied resp='foo' source='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>
            </TEI>""",
            False,
        ),
    ],
)
def test_supplied_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
