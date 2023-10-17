import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handNote",
            "<handNote xml:id='foo'/>",
            True,
        ),
        (
            "valid-handNote-with-scribe-attribute",
            "<handNote xml:id='foo' scribe='per000123'/>",
            True,
        ),
        (
            "valid-handNote-with-date",
            "<handNote xml:id='foo'><date from-custom='1001-01-01' to-custom='1100-12-31'/></handNote>",
            True,
        ),
        (
            "valid-handNote-with-p",
            "<handNote xml:id='foo'><p>bar</p></handNote>",
            True,
        ),
        (
            "invalid-handNote-with-invalid-attribute",
            "<handNote xml:id='foo' type='bar'/>",
            False,
        ),
        (
            "invalid-handNote-with-invalid-attribute",
            "<handNote xml:id='foo' n='bar'/>",
            False,
        ),
        (
            "invalid-handNote-without-xml-id",
            "<handNote/>",
            False,
        ),
    ],
)
def test_handNote(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handNote", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handNote-with-reference",
            "<TEI><handNote xml:id='foo'/><p hand='foo'>bar</p></TEI>",
            True,
        ),
        (
            "invalid-handNote-without-reference",
            "<TEI><handNote xml:id='foo'/><p hand='foos'>bar</p></TEI>",
            False,
        ),
    ],
)
def test_handNote_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when a handNote is not referenced"""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
