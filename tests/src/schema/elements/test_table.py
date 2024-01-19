import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-table-without-head",
            "<table><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "valid-table-with-head",
            "<table><head>bar</head><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "valid-table-with-multiple-heads",
            "<table><head>bar</head><row><cell>foo</cell></row><head>bar</head><row><cell>foo</cell></row></table>",
            True,
        ),
        (
            "valid-table-with-head-and-breaks",
            "<table><head>bar</head> <pb n='32' facs='fol_32v'/><cb n='a'/><row><cell>foo</cell></row><cb n='b'/></table>",
            True,
        ),
        (
            "invalid-table-with-attr",
            "<table rows='1' cols='1'><row><cell>foo</cell></row></table>",
            False,
        ),
        (
            "invalid-table-without-content",
            "<table/>",
            False,
        ),
        (
            "table-with-invalid-content",
            "<table><p>bar</p><row><cell>foo</cell></row></table>",
            False,
        ),
        (
            "invalid-table-without-row",
            "<table><head>foo</head></table>",
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
