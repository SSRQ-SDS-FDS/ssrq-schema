import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-orgName",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001'>bar</orgName>",
            True,
        ),
        (
            "valid-orgName-with-role",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001' role='recipient'>bar</orgName>",
            True,
        ),
        (
            "orgName-with-invalid-ref",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='abcdefg' role='recipient'>bar</orgName>",
            False,
        ),
        (
            "orgName-with-invalid-key",
            "<orgName xmlns='http://www.tei-c.org/ns/1.0' ref='org000001' role='xyz'>bar</orgName>",
            False,
        ),
    ],
)
def test_orgName(
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
        schema=element_schema["orgName"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
