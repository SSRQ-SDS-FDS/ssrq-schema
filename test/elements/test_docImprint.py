import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-docImprint",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
        (
            "invalid-docImprint-with-attribute",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0' type='foo'><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-without-pubPlace",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-without-publisher",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-with-multiple-places",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace><pubPlace>St. Gallen</pubPlace><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
    ],
)
def test_docImprint_rng(
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
        schema=element_schema["docImprint"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
