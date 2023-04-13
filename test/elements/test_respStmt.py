from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-respStmt",
            "<respStmt><persName>Friedrich Emil Welti</persName><resp key='transcript'/></respStmt>",
            True,
        ),
        (
            "valid-respStmt",
            "<respStmt><orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName><resp key='publisher'/></respStmt>",
            True,
        ),
        (
            "invalid-respStmt-without-resp",
            "<respStmt><persName>Friedrich Emil Welti</persName></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-p",
            "<respStmt><persName>Friedrich Emil Welti</persName><resp key='transcript'/><p>foo bar foo</p></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-attr",
            "<respStmt facs='foo'><persName>Friedrich Emil Welti</persName><resp key='transcript'/></respStmt>",
            False,
        ),
    ],
)
def test_respStmt(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("respStmt", name, markup, result, False)
