import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from .conftest import SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "with-whitespace",
            "<TEI type=' foo'></TEI>",
            False,
        ),
        (
            "without-whitespace",
            "<TEI type='bar'></TEI>",
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
            "<measure unit='cm'>bar</measure>",
            False,
        ),
        (
            "unit-and-quantity",
            "<measure unit='cm' quantity='3'>foo</measure>",
            True,
        ),
    ],
)
def test_dependency_of_unit_and_quantity(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "correct-facs",
            "<pb facs='foo_1r'/>",
            True,
        ),
        (
            "incorrect-facs",
            "<pb facs='foo._1r'/>",
            False,
        ),
        (
            "incorrect-facs",
            "<pb facs='foo__1r'/>",
            False,
        ),
    ],
)
def test_facs_naming_conventions(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when an attribute starts with whitespace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "correct-datable-with-when",
            "<date datingMethod='gregorian' when-custom='2020'/>",
            True,
        ),
        (
            "incorrect-datable-combination-when-to-custom",
            "<date datingMethod='gregorian' when-custom='2020' to-custom='2020-12-31'/>",
            False,
        ),
        (
            "correct-datable-combination-from-to",
            "<date datingMethod='gregorian' from-custom='2020-01-01' to-custom='2020-12-31'/>",
            True,
        ),
        (
            "incorrect-datable-from-without-to",
            "<date datingMethod='gregorian' from-custom='2020-01-01' />",
            False,
        ),
        (
            "incorrect-datable-combination-from-to-notBefore",
            "<date datingMethod='gregorian' from-custom='2020-01-01' to-custom='2020-12-31' notBefore-custom='2019'/>",
            False,
        ),
        (
            "incorrect-datable-combination-from-to-notAfter",
            "<date datingMethod='gregorian' from-custom='2020-01-01' to-custom='2020-12-31' notAfter-custom='2019'/>",
            False,
        ),
    ],
)
def test_datable_custom_attr(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the various constraints definied for att.datable.custom."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publisher",
            "<publisher>bar</publisher>",
            True,
        ),
        (
            "invalid-publisher",
            "<publisher/>",
            False,
        ),
        (
            "valid-hi",
            "<hi rend='sup'>bar</hi>",
            True,
        ),
        (
            "invalid-hi",
            "<hi rend='sup'/>",
            False,
        ),
        (
            "valid-head",
            "<head>bar</head>",
            True,
        ),
        (
            "invalid-head",
            "<head/>",
            False,
        ),
    ],
)
def test_text_content_constraint_gl4(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the global constraint, which ensure the usage of text() for multiple elements."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
