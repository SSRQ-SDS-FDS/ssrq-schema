import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-rdg",
            "<rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e#fol30r'>bar</rdg>",
            True,
        ),
        (
            "rdg-with-invalid-xml-id-reference",
            "<rdg wit='baz id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e'>bar</rdg>",
            False,
        ),
        (
            "invalid-rdg-wit-false-attribute",
            "<rdg type='foo' wit='ad28656b-5c8d-459c-afb4-3e6ddf70810d'>bar</rdg>",
            False,
        ),
        (
            "invalid-rdg-without-attribute",
            "<rdg>foo</rdg>",
            False,
        ),
        (
            "valid-rdg-with-different-wit-values",
            """
            <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#p123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#p123-234
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#n123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#n123-234
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123r
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123v
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123r-124v">bar</rdg>""",
            True,
        ),
        (
            "invalid-rdg-with-incorrect-wit-value-1",
            """
            <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#s123">bar</rdg>""",
            False,
        ),
        (
            "invalid-rdg-with-incorrect-wit-value-2",
            """
            <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123">bar</rdg>""",
            False,
        ),
    ],
)
def test_rdg(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("rdg", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-wit-references",
            """<TEI>
                <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>
                <bibl xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e'>foo</bibl>
                <rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e#fol30r'>bar</rdg>
            </TEI>""",
            True,
        ),
        (
            "invalid-wit-reference",
            """<TEI>
                <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>
                <rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d baz'>bar</rdg>
            </TEI>""",
            False,
        ),
    ],
)
def test_witness_attr_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
