import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-row",
            "<row xmlns='http://www.tei-c.org/ns/1.0'><cell>foo</cell></row>",
            True,
        ),
        (
            "invalid-row-content",
            "<row xmlns='http://www.tei-c.org/ns/1.0'><measureGrp><cell>foo</cell></measureGrp></row>",
            False,
        ),
        (
            "invalid-row-with-attribute",
            "<row xmlns='http://www.tei-c.org/ns/1.0' type='foo'><cell>foo</cell></row>",
            False,
        ),
    ],
)
def test_row(
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
        schema=element_schema["row"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
