import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from .conftest import SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "starts-with-whitespace",
            "<TEI type=' foo'></TEI>",
            False,
        ),
        (
            "ends-with-whitespace",
            "<TEI type='foo '></TEI>",
            False,
        ),
        (
            "valid-without-whitespace",
            "<TEI type='bar'></TEI>",
            True,
        ),
        (
            "multiple-values-with-whitespace-in-between",
            "<TEI type='bar foo'></TEI>",
            True,
        ),
    ],
)
def test_attribute_whitespace_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the if the validation fails, when an attribute starts or ends with whitespace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-quantity-with-zero-length",
            """
             <p>
                <height unit='cm' quantity='0'/>
                <width unit='cm' quantity='0.0'/>
                <measure type="length" unit="cm" quantity="00">0 cm</measure>
             </p>
            """,
            False,
        ),
        (
            "valid-quantity-with-zero-currency",
            "<measure type='currency' unit='lb' quantity='0'>0 lb</measure>",
            True,
        ),
    ],
)
def test_quantity_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test if the validation fails, when an attribute starts with whitespace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "correct-facs",
            "<pb facs='foo_1r'/>",
            True,
        ),
        (
            "incorrect-facs-with-two-underscores",
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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "correct-datable-with-when",
            "<date calendar='gregorian' when-custom='2020'/>",
            True,
        ),
        (
            "incorrect-datable-combination-when-to-custom",
            "<date calendar='gregorian' when-custom='2020' to-custom='2020-12-31'/>",
            False,
        ),
        (
            "correct-datable-combination-from-to",
            "<date calendar='gregorian' from-custom='2020-01-01' to-custom='2020-12-31'/>",
            True,
        ),
        (
            "incorrect-datable-from-without-to",
            "<date calendar='gregorian' from-custom='2020-01-01' />",
            False,
        ),
        (
            "incorrect-datable-combination-from-to-notBefore",
            "<date calendar='gregorian' from-custom='2020-01-01' to-custom='2020-12-31' notBefore-custom='2019'/>",
            False,
        ),
        (
            "incorrect-datable-combination-from-to-notAfter",
            "<date calendar='gregorian' from-custom='2020-01-01' to-custom='2020-12-31' notAfter-custom='2019'/>",
            False,
        ),
    ],
)
def test_datable_custom_attr(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the various constraints definied for att.datable.custom."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


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
        (
            "invalid-idno-with-whitespace-only",
            "<idno> </idno>",
            False,
        ),
        (
            "invalid-empty-idno",
            "<idno/>",
            False,
        ),
    ],
)
def test_text_content_constraint_gl4(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the global constraint, which ensure the usage of text() for multiple elements."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-spanTo",
            "<p><delSpan spanTo='del1'/><anchor xml:id='del1'/></p>",
            True,
        ),
        (
            "invalid-spanTo",
            "<p><anchor xml:id='del1'/><delSpan spanTo='del1'/></p>",
            False,
        ),
    ],
)
def test_constraint_attspanning(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the global constraint for @spanTo."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-duplicate-attribute-values-agent",
            "<damage agent='clipping cancelled clipping'><unclear>foo</unclear></damage>",
            False,
        ),
        (
            "invalid-duplicate-attribute-values-place",
            "<add place='above verso above'>foo</add>",
            False,
        ),
    ],
)
def test_duplicate_attribute_values_constraint_gl6(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the global constraint, which ensures that no attribute has duplicate attribute values."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-node-with-text-using-nbsp-as-html-entity-160",
            "<p>&#160;foo</p>",
            False,
        ),
        (
            "invalid-node-with-text-using-nbsp-as-html-entity-xA0",
            "<p>&#xA0;foo</p>",
            False,
        ),
        (
            "invalid-node-with-text-using-nbsp-in-unicode-notation",
            "<p> foo</p>",
            False,
        ),
        (
            "valid-node-with-text",
            "<p>foo</p>",
            True,
        ),
    ],
)
def test_uses_nbsp_in_text_node(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the global constraint, which ensures that no non-breaking-space is used."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
