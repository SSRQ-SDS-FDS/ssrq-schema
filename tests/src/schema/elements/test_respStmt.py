import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-respStmt-with-persName",
            """
            <respStmt>
                <persName>Friedrich Emil Welti</persName>
                <resp>Transkription</resp>
            </respStmt>
            """,
            True,
        ),
        (
            "valid-respStmt-with-multiple-persNames",
            """
            <respStmt>
                <persName>Friedrich Emil Welti</persName>
                <persName>Hans Emil Welti</persName>
                <resp>Transkription</resp>
            </respStmt>
            """,
            True,
        ),
        (
            "valid-respStmt-with-orgName",
            """
            <respStmt>
                <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                <resp>Herausgabe</resp>
            </respStmt>
            """,
            True,
        ),
        (
            "invalid-respStmt-with-multiple-orgNames",
            """
            <respStmt>
                <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                <resp>Herausgabe</resp>
            </respStmt>
            """,
            False,
        ),
        (
            "invalid-respStmt-with-persName-and-orgName",
            """
            <respStmt>
                <persName>Friedrich Emil Welti</persName>
                <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                <resp>Herausgabe</resp>
            </respStmt>
            """,
            False,
        ),
        (
            "valid-respStmt-multiple-resps",
            """
            <respStmt>
                <persName>Friedrich Emil Welti</persName>
                <resp>Transkription</resp>
                <resp>Erstellung Faksimile</resp>
            </respStmt>
            """,
            True,
        ),
        (
            "invalid-respStmt-without-resp",
            "<respStmt><persName>Friedrich Emil Welti</persName></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-wrong-content",
            "<respStmt><p>foo</p></respStmt>",
            False,
        ),
    ],
)
def test_resp_stmt(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("respStmt", name, markup, result, False)
