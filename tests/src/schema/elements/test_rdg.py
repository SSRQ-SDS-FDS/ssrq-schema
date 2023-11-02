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
                <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e'/>
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
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
