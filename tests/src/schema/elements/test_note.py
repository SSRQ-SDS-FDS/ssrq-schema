import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


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
            True,
        ),
        (
            "valid-note-with-content-default",
            "<note><del>foo</del> bar</note>",
            True,
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
            "invalid-note-inside-app-with-content-except-ref-and-orig",
            """
            <app>
                <note type='text_comparison'>
                    <bibl>foo</bibl>
                </note>
            </app>
            """,
            False,
        ),
        (
            "valid-note-inside-app-without-orig",
            """
            <app>
                <note type='text_comparison'>
                    <ref target='http://example.com'/>
                </note>
            </app>
            """,
            True,
        ),
        (
            "invalid-note-inside-app-with-text",
            """
            <app>
                <note type='text_comparison'>
                    <ref target='http://example.com'/>
                    <orig>baz</orig> baz
                </note>
            </app>
            """,
            False,
        ),
        (
            "invalid-note-inside-app-without-ref",
            """
            <app>
                <note type='text_comparison'>
                    <orig>foo</orig>
                </note>
            </app>
            """,
            False,
        ),
        (
            "invalid-note-inside-app-with-two-refs",
            """
            <app>
                <note type='text_comparison'>
                    <ref target='http://example.com'/>
                    <ref target='http://example.org'/>
                    <orig>foo</orig>
                </note>
            </app>
            """,
            False,
        ),
        (
            "invalid-note-inside-app-with-two-origs",
            """
            <app>
                <note type='text_comparison'>
                    <ref target='http://example.com'/>
                    <orig>bar</orig>
                    <orig>foo</orig>
                </note>
            </app>
            """,
            False,
        ),
        (
            "invalid-note-inside-app-without-type",
            """
            <app>
                <note>
                    <ref target='http://example.com'/>
                    <orig>foo</orig>
                </note>
            </app>
            """,
            False,
        ),
        (
            "invalid-note-not-inside-app-with-type",
            "<note type='text_comparison'>foo</note>",
            False,
        ),
    ],
)
def test_note_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
