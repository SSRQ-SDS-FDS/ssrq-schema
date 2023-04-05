import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
                "valid-pubPlace",
                "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
                True,
        ),
        (
                "invalid-pubPlace",
                "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'><p/></pubPlace>",
                False,
        ),
        (
                "invalid-text-with-attributes",
                "<pubPlace type='foobar' xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
                False,
        ),
    ],
)
def test_pubPlace(
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
        schema=element_schema["pubPlace"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)

@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
                "valid-pubPlace",
                "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
                True,
        ),
        (
                "invalid-pubPlace",
                "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'/>",
                False,
        ),
    ],
)
def test_pubPlace_constraints(
        main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:pubPlace."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
