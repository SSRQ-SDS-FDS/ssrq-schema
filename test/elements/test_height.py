import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-height",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-height-missing-unit",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3'/>",
            False,
        ),
        (
            "invalid-height-wrong-unit",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-height-wrong-quantity",
            "<height xmlns='http://www.tei-c.org/ns/1.0' quantity='bar' unit='cm'/>",
            False,
        ),
    ],
)
def test_height(
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
        schema=element_schema["height"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
