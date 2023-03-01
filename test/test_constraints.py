from pyschval import isoschematron_validate

from main import Schema


def test_attribute_whitespace_constraint(odds: list[Schema], writer):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(
        "with-whitespace",
        "<TEI xmlns='http://www.tei-c.org/ns/1.0' type=' foo'></TEI>",
    )
    writer.write(
        "without-whitespace",
        "<TEI xmlns='http://www.tei-c.org/ns/1.0' type='bar'></TEI>",
    )
    test_files = writer.list()
    main_schema = [odd for odd in odds if odd.name == "TEI_Schema"][0]
    assert main_schema is not None
    assert len(test_files) == 2
    reports = isoschematron_validate(files=test_files, relaxng=main_schema.rng)
    assert len(reports) == 2
    assert reports[0].is_valid() is False
    assert reports[1].is_valid() is True


def test_dependency_of_unit_and_quantity(odds: list[Schema], writer):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(
        "unit-only",
        "<measure xmlns='http://www.tei-c.org/ns/1.0' unit='cm'></measure>",
    )
    writer.write(
        "unit-and-quantity",
        "<measure xmlns='http://www.tei-c.org/ns/1.0' unit='cm' quantity='3'></measure>",
    )
    test_files = writer.list()
    main_schema = [odd for odd in odds if odd.name == "TEI_Schema"][0]
    assert main_schema is not None
    assert len(test_files) == 2
    reports = isoschematron_validate(files=test_files, relaxng=main_schema.rng)
    assert len(reports) == 2
    unit_only = [report for report in reports if "unit-only" in report.file][0]
    unit_and_quantity = [
        report for report in reports if "unit-and-quantity" in report.file
    ][0]
    assert unit_only.is_valid() is False
    assert unit_and_quantity.is_valid() is True
