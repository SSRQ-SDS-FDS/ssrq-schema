import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-table-with-row",
            "<table><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "valid-table-with-multiple-rows",
            "<table><row><cell>foo</cell></row><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "invalid-table-without-row",
            "<table><head>foo</head></table>",
            False,
        ),
        (
            "valid-table-with-head",
            "<table><head>bar</head><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "valid-table-with-multiple-heads",
            """
            <table>
                <head>bar</head>
                <row><cell>foo</cell></row>
                <head>bar</head>
                <row><cell>foo</cell></row>
            </table>
            """,
            True,
        ),
        (
            "valid-table-with-milestones",
            """
            <table>
                <pb n='32' facs='fol_32v'/>
                <cb n='a'/>
                <row><cell>foo</cell></row>
            </table>
            """,
            True,
        ),
        (
            "invalid-table-with-cols",
            "<table cols='1'><row><cell>foo</cell></row></table>",
            False,
        ),
        (
            "invalid-table-with-rows",
            "<table rows='1'><row><cell>foo</cell></row></table>",
            False,
        ),
        (
            "table-with-invalid-content",
            "<table><p>foo</p><row>bar</row></table>",
            False,
        ),
    ],
)
def test_table(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("table", name, markup, result, False)
