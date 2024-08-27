import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div",
            "<div><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-type-and-n",
            "<div type='chapter' n='1'><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-list",
            "<div type='chapter' n='1'><list><item>foo</item></list></div>",
            True,
        ),
        (
            "invalid-div-with-wrong-type",
            "<div type='bar'><p>foo</p></div>",
            False,
        ),
        (
            "invalid-div-with-wrong-attribute",
            "<div wit='bar'><p>foo</p></div>",
            False,
        ),
    ],
)
def test_div(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("div", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div-without-text",
            "<div><p>foo</p>     </div>",
            True,
        ),
        (
            "valid-div-without-text-with-linebreaks",
            """<div><p>foo</p>
            <p>bar</p>
            <p>baz</p>
            </div>
            """,
            True,
        ),
        (
            "invalid-div-with-text",
            "<div><p>foo</p> hello</div>",
            False,
        ),
        (
            "valid-xml-lang-in-back",
            "<back><div xml:lang='de'><p>foo</p></div><div xml:lang='fr'><p>bar</p></div></back>",
            True,
        ),
        (
            "invalid-xml-lang-in-back-just-one-div",
            "<back><div xml:lang='de'><p>foo</p></div></back>",
            False,
        ),
        (
            "invalid-xml-lang-in-back-just-one-xml-lang",
            "<back><div xml:lang='de'><p>foo</p></div><div><p>bar</p></div></back>",
            False,
        ),
        (
            "invalid-xml-lang-in-back-just-same-xml-lang",
            "<back><div xml:lang='de'><p>foo</p></div><div xml:lang='de'><p>bar</p></div></back>",
            False,
        ),
        (
            "invalid-xml-lang-in-body",
            "<body><div xml:lang='de'><p>foo</p></div></body>",
            False,
        ),
    ],
)
def test_div_text_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
