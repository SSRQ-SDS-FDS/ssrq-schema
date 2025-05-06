import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-p",
            "<p>foo</p>",
            True,
        ),
        (
            "valid-p-with-n",
            "<p n='1'>foo</p>",
            True,
        ),
        (
            "valid-p-with-xml-lang",
            "<p xml:lang='de'>foo</p>",
            True,
        ),
        (
            "valid-p-with-list-content",
            "<p><list><item>bar</item></list></p>",
            True,
        ),
        (
            "valid-p-with-bibl-content",
            "<p><bibl>foo</bibl></p>",
            True,
        ),
        (
            "valid-p-with-ref-content",
            "<p><ref>foo</ref></p>",
            True,
        ),
        (
            "valid-p-with-content-default",
            "<p><del>foo</del></p>",
            True,
        ),
        (
            "invalid-p-with-wrong-content",
            "<p><p>foo</p></p>",
            False,
        ),
        (
            "valid-p-with-two-segs",
            "<p><seg>foo</seg><seg>foo</seg></p>",
            True,
        ),
        (
            "invalid-p-with-one-seg",
            "<p><seg>foo</seg></p>",
            False,
        ),
    ],
)
def test_p(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("p", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ps-with-xml-lang",
            "<div><p xml:lang='de'>foo</p><p xml:lang='de'>foo</p></div>",
            True,
        ),
        (
            "invalid-ps-with-xml-lang",
            "<div><p xml:lang='de'>foo</p><p>foo</p></div>",
            False,
        ),
        (
            "valid-p-with-ab",
            "<p>foo<ab type='marginal_note'>bar</ab></p>",
            True,
        ),
        (
            "invalid-p-with-ab",
            "<p>foo<ab type='tax'>bar</ab></p>",
            False,
        ),
    ],
)
def test_p_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
