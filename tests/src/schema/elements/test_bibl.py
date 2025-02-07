import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-bibl",
            "<bibl>foo</bibl>",
            True,
        ),
        (
            "valid-bibl-with-xml-id",
            "<bibl xml:id='id-ssrq-12345678-1234-4123-8123-123456789012'>foo</bibl>",
            True,
        ),
        (
            "invalid-bibl-with-attr",
            "<bibl type='lit'>foo</bibl>",
            False,
        ),
        (
            "invalid-bibl-with-default-content",
            "<bibl><p>foo</p></bibl>",
            False,
        ),
        (
            "valid-bibl-with-ref",
            "<bibl><ref target='http://zotero.org/groups/5048222/items/M8D9EG5B'/>, S. 93</bibl>",
            True,
        ),
        (
            "valid-bibl-with-pc-and-ref",
            """
            <bibl>
                <ref target='http://zotero.org/groups/5048222/items/M8D9EG5B'/><pc>:</pc> S. 93
            </bibl>""",
            True,
        ),
    ],
)
def test_bibl(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("bibl", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-bibl-with-xml-id-inside-listBibl",
            """
            <listBibl>
                <bibl xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "invalid-bibl-with-xml-id-outside-listBibl",
            "<note><bibl xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</bibl></note>",
            False,
        ),
    ],
)
def test_bibl_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
