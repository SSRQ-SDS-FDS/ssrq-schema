import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-licence",
            "<licence xmlns='http://www.tei-c.org/ns/1.0' target='http://licence.bar'>foo bar</licence>",
            True,
        ),
        (
            "invalid-licence",
            "<licence xmlns='http://www.tei-c.org/ns/1.0' target='licence.bar'>foo bar</licence>",
            False,
        ),
    ],
)
def test_licence(
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
        schema=element_schema["licence"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
