import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from main import Schema

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "TEI-valid",
            "<TEI xmlns='http://www.tei-c.org/ns/1.0' xml:lang='de'><teiHeader></teiHeader><text></text></TEI>",
            False,
            None,
        ),
        (
            "TEI-invalid-content",
            "<TEI xmlns='http://www.tei-c.org/ns/1.0' xml:lang='de'><teiHeader></teiHeader><facsimile></facsimile><text></text></TEI>",
            False,
            None,
        ),
        (
            "TEI-invalid-att",
            " <TEI xmlns='http://www.tei-c.org/ns/1.0' xml:lang='fr' n='1234'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'attribute "n" not allowed here',
        ),
        (
            "TEI-invalid-lang",
            " <TEI xmlns='http://www.tei-c.org/ns/1.0' xml:lang='pt'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'must be equal to "de", "fr" or "it"',
        ),
    ],
)
def test_TEI_main_rng(
    main_schema: Schema,
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    validator = RNGJingValidator()
    writer.write(name, markup)

    validator.validate(
        sources=writer.parse_files(),
        schema=main_schema.rng,
        file_pattern=writer.construct_file_pattern(),
    )

    assert len(validator.get_invalid()) == 1
    assert validator.count_valid() == int(result)
    if message is not None:
        file_reports = validator.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
