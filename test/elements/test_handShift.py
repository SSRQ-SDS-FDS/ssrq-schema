import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='secondaryHand'>foo</handShift>",
            False,
        ),
        (
            "handShift-valid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035807'/>",
            True,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='per035'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
        (
            "handShift-invalid",
            "<handShift xmlns='http://www.tei-c.org/ns/1.0' scribe='foo'/>",
            False,
        ),
    ],
)
def test_handShift_rng(
    element_schema: dict[str, str],
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    """Test the content model defined for tei:handShift."""

    validator = RNGJingValidator()
    writer.write(name, markup)

    validator.validate(
        sources=writer.parse_files(),
        schema=element_schema["handShift"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
