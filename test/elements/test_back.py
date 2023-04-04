import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-back",
            "<back xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            True,
        ),
        (
            "invalid-back-with-p-only",
            "<back xmlns='http://www.tei-c.org/ns/1.0'><p>foo</p></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back xml:id='bar123' xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back rend='bar' xmlns='http://www.tei-c.org/ns/1.0'><div><p>foo</p></div></back>",
            False,
        ),
    ],
)
def test_back(
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
        schema=element_schema["back"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
