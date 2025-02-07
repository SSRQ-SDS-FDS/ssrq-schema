import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-seriesStmt",
            """
            <seriesStmt>
                <title>Sammlung Schweizerischer Rechtsquellen</title>
                <respStmt>
                    <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                    <resp>Herausgabe</resp>
                </respStmt>
                <idno>SSRQ-FR-I_2_8-1-1</idno>
                <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
            </seriesStmt>
            """,
            True,
        ),
        (
            "invalid-seriesStmt-without-title",
            """
            <seriesStmt>
                <respStmt>
                    <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                    <resp>Herausgabe</resp>
                </respStmt>
                <idno>SSRQ-FR-I_2_8-1-1</idno>
                <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
            </seriesStmt>
            """,
            False,
        ),
        (
            "invalid-seriesStmt-without-respStmt",
            """
            <seriesStmt>
                <title>Sammlung Schweizerischer Rechtsquellen</title>
                <idno>SSRQ-FR-I_2_8-1-1</idno>
                <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
            </seriesStmt>
            """,
            False,
        ),
        (
            "invalid-seriesStmt-with-one-idno",
            """
            <seriesStmt>
                <title>Sammlung Schweizerischer Rechtsquellen</title>
                <respStmt>
                    <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                    <resp>Herausgabe</resp>
                </respStmt>
                <idno>SSRQ-FR-I_2_8-1-1</idno>
            </seriesStmt>
            """,
            False,
        ),
        (
            "invalid-seriesStmt-without-idnos",
            """
            <seriesStmt>
                <title>Sammlung Schweizerischer Rechtsquellen</title>
                <respStmt>
                    <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                    <resp>Herausgabe</resp>
                </respStmt>
            </seriesStmt>
            """,
            False,
        ),
    ],
)
def test_series_stmt_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("seriesStmt", name, markup, result, False)
