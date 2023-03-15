import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='map' mimeType='image/svg' url='foo.svg'/>",
            True,
        ),
        (
            "valid-graphic",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='familytree' mimeType='image/jpg' url='foo.jpg'/>",
            True,
        ),
        (
            "invalid-graphic-with-content",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='map' mimeType='image/svg' url='foo.png'>bar</graphic>",
            False,
        ),
        (
            "invalid-graphic-with-invalid-type",
            "<graphic xmlns='http://www.tei-c.org/ns/1.0' type='bar' mimeType='image/svg' url='foo.png'/>",
            False,
        ),
    ],
)
def test_graphic_rng(
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
        schema=element_schema["graphic"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
