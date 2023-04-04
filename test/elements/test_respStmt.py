import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


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
    element_schema: dict[str, str],
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    validator = RNGJingValidator()
    writer.write(name, markup)

    validator.validate(
        sources=writer.parse_files(),
        schema=element_schema["respStmt"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
