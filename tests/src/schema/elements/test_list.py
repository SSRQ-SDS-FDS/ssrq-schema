import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-list",
            "<list><item>foo</item></list>",
            True,
        ),
        (
            "valid-list-with-head",
            "<list><head>foo</head><item>foo</item></list>",
            True,
        ),
        (
            "valid-list-with-milestone-elements",
            """<list>
                <head>foo</head>
                <pb n='1r'/>
                <cb n='a'/>
                <item>foo</item>
                <item>foo</item>
                <cb n='b'/>
                <item>bar</item>
                <item>bar</item>
            </list>""",
            True,
        ),
        (
            "valid-list-with-spanning-elements",
            """<list>
                <head>foo</head>
                <addSpan spanTo="add1"/>
                <delSpan spanTo="del1"/>
                <damageSpan agent="cancelled" spanTo="damage1"/>
                <item>foo</item>
                <item>foo</item>
                <anchor xml:id="add1"/>
                <anchor xml:id="del1"/>
                <anchor xml:id="damage1"/>
                <item>foo</item>
                <item>bar</item>
                <item>bar</item>
            </list>""",
            True,
        ),
        (
            "valid-list-with-rend-bulleted",
            "<list rend='bulleted'><item>foo</item></list>",
            True,
        ),
        (
            "valid-list-with-rend-numbered",
            "<list rend='numbered'><item>foo</item></list>",
            True,
        ),
        (
            "invalid-list-with-wrong-rend",
            "<list rend='foo'><item>foo</item></list>",
            False,
        ),
    ],
)
def test_list(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("list", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-list-with-nested-list",
            """
            <list>
                <item>foo</item>
                <item>
                    <list>
                        <item>bar</item>
                        <item>baz</item>
                    </list>
                </item>
            </list>
            """,
            True,
        ),
        (
            "invalid-list-with-three-levels",
            """
            <list>
                <item>foo</item>
                <item>
                    <list>
                        <item>bar</item>
                        <item>
                            <list>
                                <item>baz</item>
                                <item>qux</item>
                            </list>
                        </item>
                    </list>
                </item>
            </list>
            """,
            False,
        ),
    ],
)
def test_list_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
