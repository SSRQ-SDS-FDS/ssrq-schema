import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measureGrp",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0'><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            True,
        ),
        (
            "invalid-measureGrp-without-content",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
        (
            "invalid-measureGrp-with-attribute",
            "<measureGrp xmlns='http://www.tei-c.org/ns/1.0' type='foo'><lb/></measureGrp>",
            False,
        ),
    ],
)
def test_measureGrp(
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
        schema=element_schema["measureGrp"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
