import pytest
from ssrq_cli.validate.xml import RNGJingValidator

from ..conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pb-with-type",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' type='original'/>",
            True,
        ),
        (
            "valid-pb-without-type",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1'/>",
            True,
        ),
        (
            "valid-pb-with-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen_A_4_328'/>",
            True,
        ),
        (
            "pb-with-invalid-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen_A_4_328u'/>",
            False,
        ),
        (
            "pb-with-invalid-facs",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1' facs='StASH_Ordnungen A_4_328'/>",
            False,
        ),
        (
            "pb-with-invalid-n",
            "<pb xmlns='http://www.tei-c.org/ns/1.0' n='1XIV'/>",
            False,
        ),
    ],
)
def test_pb(
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
        schema=element_schema["pb"],
        file_pattern=writer.construct_file_pattern(),
    )
    assert len(validator.get_invalid()) == (0 if result else 1)
