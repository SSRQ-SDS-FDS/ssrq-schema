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
            "valid-table-with-head-and-pb",
            "<table><head>bar</head> <pb n='32' facs='fol_32v'/><row><cell>foo</cell></row></table>",
            True,
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
    ],
)
def test_table(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("table", name, markup, result, False)
