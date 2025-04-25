import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listBibl",
            """
            <listBibl>
                <head>Archiv 1</head>
                <bibl>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "valid-listBibl-with-multiple-bibls",
            """
            <listBibl>
                <head>Archiv 1</head>
                <bibl>foo</bibl>
                <bibl>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "valid-listBibl-with-listBibls",
            """
            <listBibl>
                <head>Archiv</head>
                <listBibl>
                    <head>Urkunden</head>
                    <bibl>foo</bibl>
                </listBibl>
                <listBibl>
                    <head>Drucke</head>
                    <bibl>foo</bibl>
                </listBibl>
            </listBibl>
            """,
            True,
        ),
        (
            "invalid-listBibl-without-head",
            "<listBibl><bibl>foo</bibl></listBibl>",
            False,
        ),
        (
            "invalid-listBibl-with-attribute",
            """
            <listBibl type="foo">
                <head>Archiv 1</head>
                <bibl>foo</bibl>
            </listBibl>
            """,
            False,
        ),
    ],
)
def test_list_bibl(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("listBibl", name, markup, result, False)
