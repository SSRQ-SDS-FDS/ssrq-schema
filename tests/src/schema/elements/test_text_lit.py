import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            """
            <text type='literature'>
                <body>
                    <div>
                        <head>Archive</head>
                        <listBibl>
                            <head>Archiv 1</head>
                            <bibl>foo</bibl>
                        </listBibl>
                    </div>
                </body>
            </text>
            """,
            True,
        ),
        (
            "invalid-text-with-back",
            """
            <text type='literature'>
                <body>
                    <div>
                        <head>Archive</head>
                        <listBibl>
                            <head>Archiv 1</head>
                            <bibl>foo</bibl>
                        </listBibl>
                    </div>
                </body>
                <back>foo</back>
            </text>
            """,
            False,
        ),
        (
            "invalid-text-without-type",
            """
            <text>
                <body>
                    <div>
                        <head>Archive</head>
                        <listBibl>
                            <head>Archiv 1</head>
                            <bibl>foo</bibl>
                        </listBibl>
                    </div>
                </body>
            </text>
            """,
            False,
        ),
        (
            "invalid-text-wrong-type",
            """
            <text type='intro'>
                <body>
                    <div>
                        <head>Archive</head>
                        <listBibl>
                            <head>Archiv 1</head>
                            <bibl>foo</bibl>
                        </listBibl>
                    </div>
                </body>
            </text>
            """,
            False,
        ),
    ],
)
def test_text(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("text", name, markup, result, False)
