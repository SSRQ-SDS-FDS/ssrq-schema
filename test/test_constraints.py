import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from .conftest import SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "with-whitespace",
            "<TEI xmlns='http://www.tei-c.org/ns/1.0' type=' foo'></TEI>",
            False,
        ),
        (
            "without-whitespace",
            "<TEI xmlns='http://www.tei-c.org/ns/1.0' type='bar'></TEI>",
            True,
        ),
    ],
)
def test_attribute_whitespace_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "unit-only",
            "<measure xmlns='http://www.tei-c.org/ns/1.0' unit='cm'>bar</measure>",
            False,
        ),
        (
            "unit-and-quantity",
            "<measure xmlns='http://www.tei-c.org/ns/1.0' unit='cm' quantity='3'>foo</measure>",
            True,
        ),
    ],
)
def test_dependency_of_unit_and_quantity(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
