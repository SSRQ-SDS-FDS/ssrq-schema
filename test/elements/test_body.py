import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-empty-body",
            "<body xmlns='http://www.tei-c.org/ns/1.0'/>",
            True,
        ),
        (
            "valid-body-with-div",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><pb n='1' facs='abcde'/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div-signed",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><pb n='1' facs='abcde'/><div><p>bar</p></div><signed><lb/>Rechenschriber</signed></body>",
            True,
        ),
        (
            "invalid-body-with-text-only",
            "<body xmlns='http://www.tei-c.org/ns/1.0'>foo</body>",
            False,
        ),
        (
            "invalid-body-with-p-as-child",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><p>foo</p></body>",
            False,
        ),
    ],
)
def test_body_rng(
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
        schema=element_schema["body"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
