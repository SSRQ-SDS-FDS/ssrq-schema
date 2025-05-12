import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div-with-head-and-listBibl",
            """
            <div>
                <head>Archive</head>
                <listBibl>
                    <head>Archiv 1</head>
                    <bibl>foo</bibl>
                </listBibl>
            </div>
            """,
            True,
        ),
        (
            "valid-div-with-head-and-multiple-listBibl",
            """
            <div>
                <head>Archive</head>
                <listBibl>
                    <head>Archiv 1</head>
                    <bibl>foo</bibl>
                </listBibl>
                <listBibl>
                    <head>Archiv 2</head>
                    <bibl>foo</bibl>
                </listBibl>
            </div>
            """,
            True,
        ),
        (
            "invalid-div-with-two-divs",
            """
            <div>
                <div>
                    <head>Archive</head>
                    <listBibl>
                        <head>Archiv 1</head>
                        <bibl>foo</bibl>
                    </listBibl>
                </div>
                <div>
                    <head>Bibliotheken</head>
                    <listBibl>
                        <head>Bibliothek 1</head>
                        <bibl>foo</bibl>
                    </listBibl>
                </div>
            </div>
            """,
            False,
        ),
    ],
)
def test_div(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("div", name, markup, result, False)
