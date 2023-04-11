from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-respStmt",
            "<respStmt xmlns='http://www.tei-c.org/ns/1.0'><persName>Friedrich Emil Welti</persName><resp key='transcript'/></respStmt>",
            True,
        ),
        (
            "valid-respStmt",
            "<respStmt xmlns='http://www.tei-c.org/ns/1.0'><orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName><resp key='publisher'/></respStmt>",
            True,
        ),
        (
            "invalid-respStmt-without-resp",
            "<respStmt xmlns='http://www.tei-c.org/ns/1.0'><persName>Friedrich Emil Welti</persName></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-p",
            "<respStmt xmlns='http://www.tei-c.org/ns/1.0'><persName>Friedrich Emil Welti</persName><resp key='transcript'/><p>foo bar foo</p></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-attr",
            "<respStmt xmlns='http://www.tei-c.org/ns/1.0' facs='foo'><persName>Friedrich Emil Welti</persName><resp key='transcript'/></respStmt>",
            False,
        ),
    ],
)
def test_respStmt(
    test_element_with_rng: Callable[[str, str, str, bool], None],
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("respStmt", name, markup, result)
