import pytest

from ..conftest import RNG_test_function


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
