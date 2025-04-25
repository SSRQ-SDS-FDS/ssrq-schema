import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-body-with-one-div",
            """
            <body>
                <div>
                    <head>Archive</head>
                    <listBibl>
                        <head>Archiv 1</head>
                        <bibl>foo</bibl>
                    </listBibl>
                </div>
            </body>
            """,
            True,
        ),
        (
            "invalid-body-with-multiple-divs",
            """
             <body>
                 <div>
                     <head>Archive</head>
                     <listBibl>
                         <head>Archiv 1</head>
                         <bibl>foo</bibl>
                     </listBibl>
                 </div>
                 <div>
                     <head>Archive</head>
                     <listBibl>
                         <head>Archiv 1</head>
                         <bibl>foo</bibl>
                     </listBibl>
                 </div>
             </body>
             """,
            False,
        ),
        (
            "invalid-body-with-other-content",
            """
             <body>
                 <div>
                     <head>Archive</head>
                     <listBibl>
                         <head>Archiv 1</head>
                         <bibl>foo</bibl>
                     </listBibl>
                 </div>
                 <pb n="1r"/>
             </body>
             """,
            False,
        ),
    ],
)
def test_body(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("body", name, markup, result, False)
