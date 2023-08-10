import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-respStmt",
            "<respStmt><persName>Friedrich Emil Welti</persName><resp>Transkription</resp></respStmt>",
            True,
        ),
        (
            "valid-respStmt",
            "<respStmt><orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName><resp>Herausgabe</resp></respStmt>",
            True,
        ),
        (
            "invalid-respStmt-without-resp",
            "<respStmt><persName>Friedrich Emil Welti</persName></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-p",
            "<respStmt><persName>Friedrich Emil Welti</persName><resp>Transkription</resp><p>foo bar foo</p></respStmt>",
            False,
        ),
        (
            "invalid-respStmt-with-attr",
            "<respStmt facs='foo'><persName>Friedrich Emil Welti</persName><resp>Transkription</resp></respStmt>",
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
