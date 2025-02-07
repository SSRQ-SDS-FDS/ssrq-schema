import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-supplied-with-source",
            "<supplied source='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</supplied>",
            True,
        ),
        (
            "invalid-supplied-source",
            "<supplied source='bar'>foo</supplied>",
            False,
        ),
        (
            "valid-supplied-with-resp",
            "<supplied resp='CS'>foo</supplied>",
            True,
        ),
        (
            "valid-supplied-with-multiple-resp-values",
            "<supplied resp='CS BP'>foo</supplied>",
            True,
        ),
        (
            "invalid-supplied-with-cert",
            "<supplied cert='high'>foo</supplied>",
            False,
        ),
        (
            "valid-supplied-with-p",
            "<supplied resp='CS'><p>foo</p></supplied>",
            True,
        ),
        (
            "valid-supplied-with-ps",
            "<supplied resp='CS'><p>foo</p><p>bar</p></supplied>",
            True,
        ),
        (
            "valid-supplied-with-content-default",
            "<supplied resp='CS'><del>foo</del> bar</supplied>",
            True,
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
                <listBibl>
                    <bibl xml:id='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</bibl>
                </listBibl>
                <supplied source='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>
            </TEI>
            """,
            True,
        ),
        (
            "valid-supplied-source-with-urn:ssrq",
            """
            <TEI>
                <supplied source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1'>foo</supplied>
            </TEI>
            """,
            True,
        ),
        (
            "invalid-supplied-without-attribute",
            "<supplied>foo</supplied>",
            False,
        ),
        (
            "invalid-supplied-with-resp-and-sources",
            """
            <TEI>
                <listBibl>
                    <bibl xml:id='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</bibl>
                </listBibl>
                <supplied resp='foo' source='id-ssrq73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>
            </TEI>
            """,
            False,
        ),
    ],
)
def test_supplied_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
