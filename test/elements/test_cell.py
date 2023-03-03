import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-cell", "<cell xmlns='http://www.tei-c.org/ns/1.0'>foo</cell>", True),
        (
            "valid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0' role='label'>foo</cell>",
            True,
        ),
        (
            "valid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0'>foo <anchor xml:id='bar'/></cell>",
            True,
        ),
        (
            "invalid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0' role='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell",
            '<cell xmlns="http://www.tei-c.org/ns/1.0" foo="bar"><teiHeader/></cell>',
            False,
        ),
    ],
)
def test_cell(
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
        schema=element_schema["cell"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
