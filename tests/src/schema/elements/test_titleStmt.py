import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-titleStmt",
            """
            <titleStmt>
                <title>foo</title>
                <editor>
                    <persName>foo</persName>
                </editor>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Transkription</resp>
                </respStmt>
            </titleStmt>
            """,
            True,
        ),
        (
            "valid-titleStmt-with-multiple-editors",
            """
            <titleStmt>
                <title>foo</title>
                <editor>
                    <persName>foo</persName>
                </editor>
                <editor>
                    <persName>bar</persName>
                </editor>
                <respStmt>
                    <persName>foo</persName>
                    <persName>bar</persName>
                    <resp>Transkription</resp>
                </respStmt>
            </titleStmt>
            """,
            True,
        ),
        (
            "valid-titleStmt-with-multiple-respStmts",
            """
            <titleStmt>
                <title>foo</title>
                <editor>
                    <persName>foo</persName>
                </editor>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Transkription</resp>
                </respStmt>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Qualitätskontrolle</resp>
                </respStmt>
            </titleStmt>
            """,
            True,
        ),
        (
            "invalid-titleStmt-without-title",
            """
            <titleStmt>
                <editor>
                    <persName>foo</persName>
                </editor>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Transkription</resp>
                </respStmt>
            </titleStmt>
            """,
            False,
        ),
        (
            "invalid-titleStmt-without-editor",
            """
            <titleStmt>
                <title>foo</title>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Transkription</resp>
                </respStmt>
            </titleStmt>
            """,
            False,
        ),
        (
            "invalid-titleStmt-without-respStmt",
            """
            <titleStmt>
                <title>foo</title>
                <editor>
                    <persName>foo</persName>
                </editor>
            </titleStmt>
            """,
            False,
        ),
        (
            "invalid-titleStmt-with-wrong-order",
            """
            <titleStmt>
                <editor>
                    <persName>foo</persName>
                </editor>
                <title>foo</title>
                <respStmt>
                    <persName>foo</persName>
                    <resp>Transkription</resp>
                </respStmt>
            </titleStmt>
            """,
            False,
        ),
        (
            "invalid-titleStmt-with-wrong-content",
            "<titleStmt>foo</titleStmt>",
            False,
        ),
    ],
)
def test_title_stmt_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("titleStmt", name, markup, result, False)
