import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div-with-type",
            "<div type='chapter'><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-n",
            "<div n='1'><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-p",
            "<div><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-list",
            "<div><list><item>foo</item></list></div>",
            True,
        ),
        (
            "valid-div-with-seg",
            "<div><seg>foo</seg></div>",
            True,
        ),
        (
            "valid-div-with-content-default",
            "<div><del>foo</del></div>",
            True,
        ),
        (
            "invalid-div-with-one-div",
            "<div><div>foo</div></div>",
            False,
        ),
        (
            "valid-div-with-two-divs",
            "<div><div>foo</div><div>bar</div></div>",
            True,
        ),
        (
            "valid-div-with-two-divs-and-milestones",
            """
            <div>
                <addSpan spanTo='add1'/>
                <pb n='1'/>
                <div>foo</div>
                <cb n='a'/>
                <div>bar</div>
                <anchor xml:id='add1'/>
            </div>""",
            True,
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
            "<div><p>foo</p></div>",
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
            "invalid-div-with-xml-lang-in-body",
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
