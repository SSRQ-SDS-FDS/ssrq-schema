import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>foo</p></div></body></text>",
            True,
        ),
        (
            "valid-text",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>bar</p></div></body><back><div><p>foo</p></div></back></text>",
            True,
        ),
        (
            "invalid-text-with-back-only",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><back><div><p>foo</p></div></back></text>",
            False,
        ),
        (
            "invalid-text-with-attribute",
            "<text type='foobar' xmlns='http://www.tei-c.org/ns/1.0'><body><div><p>hallo welt!</p></div></body></text>",
            False,
        ),
        (
            "invalid-text-with-group",
            "<text xmlns='http://www.tei-c.org/ns/1.0'><group><body><div><p>hallo welt!</p></div></body></group></text>",
            False,
        ),
    ],
)
def test_text(
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
        schema=element_schema["text"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
