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
            "valid-list-with-multiple-elements",
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
            "invalid-list",
            "<list/>",
            False,
        ),
        (
            "invalid-list-with-wrong-attribute",
            "<list att='foo'><item>foo</item></list>",
            False,
        ),
        (
            "invalid-list-with-wrong-attribute-value",
            "<list rend='bar'><item>foo</item></list>",
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
