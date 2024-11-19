import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-element-with-calendar-but-no-other-dating-attributes",
            "<date calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "valid-element-with-calendar-and-another-dating-attributes",
            "<date calendar='gregorian' when-custom='1000-01-01'>Foo</date>",
            True,
        ),
        (
            "valid-element-with-calendar-and-two-other-dating-attributes",
            "<date calendar='gregorian' from-custom='1000-01-01' to-custom='1001-01-00'>Foo</date>",
            True,
        ),
    ],
)
def test_constraint_sch_att_calendar(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the usage of other attributes in combination with @calendar."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-datable-with-when",
            "<date calendar='gregorian' when-custom='2020-01-01'>Foo</date>",
            True,
        ),
        (
            "invalid-datable-with-when-and-from",
            """<date calendar='gregorian' 
                     when-custom='2020-01-01' 
                     from-custom='2020-12-31'>Foo</date>""",
            False,
        ),
        (
            "invalid-datable-with-when-and-to",
            """<date calendar='gregorian' 
                     when-custom='2020-01-01' 
                     to-custom='2020-12-31'>Foo</date>""",
            False,
        ),
        (
            "invalid-datable-with-when-and-notBefore",
            """<date calendar='gregorian' 
                     when-custom='2020-01-01' 
                     notBefore-custom='2020-12-31'>Foo</date>""",
            False,
        ),
        (
            "invalid-datable-with-when-and-notAfter",
            """<date calendar='gregorian' 
                     when-custom='2020-01-01' 
                     notAfter-custom='2020-12-31'>Foo</date>""",
            False,
        ),
        (
            "valid-datable-with-from-and-to",
            """<date calendar='gregorian' 
                     from-custom='2020-01-01' 
                     to-custom='2020-12-31'>Foo</date>""",
            True,
        ),
        (
            "invalid-datable-with-to-without-from",
            "<date calendar='gregorian' to-custom='2020-01-01'>Foo</date>",
            False,
        ),
        (
            "invalid-datable-with-from-without-to",
            "<date calendar='gregorian' from-custom='2020-01-01'>Foo</date>",
            False,
        ),
        (
            "invalid-datable-with-from-and-to-and-notBefore",
            """<date calendar='gregorian' 
                     from-custom='2020-01-01' to-custom='2020-12-31' 
                     notBefore-custom='2019'>Foo</date>""",
            False,
        ),
        (
            "invalid-datable-with-from-and-to-and-notAfter",
            """<date calendar='gregorian' 
                     from-custom='2020-01-01' to-custom='2020-12-31' 
                     notAfter-custom='2019'>Foo</date>""",
            False,
        ),
        (
            "invalid-datable-with-to-before-from",
            """<date calendar='gregorian' 
                     from-custom='2000-01-01' 
                     to-custom='1000-12-31'>Foo</date>""",
            False,
        ),
    ],
)
def test_constraint_sch_att_data_custom(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the various constraints defined by sch-data-custom."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-unit-and-quantity-with-value-unknown",
            "<damage agent='clipping' unit='unknown' quantity='unknown'>Foo</damage>",
            True,
        ),
        (
            "invalid-unit-and-quantity-with-value-unknown",
            "<damage agent='clipping' unit='unknown' quantity='1'>Foo</damage>",
            False,
        ),
    ],
)
def test_constraint_sch_att_dimensions(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the value "unknown" for @unit and @quantity."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-element-with-unit-and-quantity",
            "<damage agent='clipping' unit='cm' quantity='1'>Foo</damage>",
            True,
        ),
        (
            "invalid-element-with-unit-without-quantity",
            "<damage agent='clipping' unit='cm'>Foo</damage>",
            False,
        ),
        (
            "invalid-element-without-unit-with-quantity",
            "<damage agent='clipping' quantity='1'>Foo</damage>",
            False,
        ),
    ],
)
def test_constraint_sch_att_dimensions_2(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the dependency of @unit and @quantity."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-quantity-zero-currency",
            "<measure type='currency' unit='lb' quantity='0'>0 lb</measure>",
            True,
        ),
        (
            "valid-quantity-zero-currency-as-float",
            "<measure type='currency' unit='lb' quantity='0.0'>0 lb</measure>",
            True,
        ),
        (
            "invalid-quantity-zero-length",
            "<measure type='length' unit='cm' quantity='0'>0 cm</measure>",
            False,
        ),
        (
            "invalid-quantity-zero-length-as-float",
            "<measure type='length' unit='cm' quantity='0.0'>0 cm</measure>",
            False,
        ),
    ],
)
def test_constraint_att_dimensions_3(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraint for @quantity being 0."""
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
def test_constraint_sch_att_span_to(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the global constraint for @spanTo."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-facs",
            "<pb facs='foo_1r'/>",
            True,
        ),
        (
            "invalid-facs-with-two-underscores",
            "<pb facs='foo__1r'/>",
            False,
        ),
    ],
)
def test_constraint_sch_att_facs(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraint for @facs."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-wit-referencing-a-witness-element",
            """
            <div>
                <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
                <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
            </div>        
            """,
            True,
        ),
        (
            "valid-wit-referencing-a-bibl-element",
            """
            <div>
                <bibl xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">Foo</bibl>
                <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
            </div>        
            """,
            True,
        ),
        (
            "invalid-wit-referencing-a-wrong-element",
            """
            <div>
                <anchor xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
                <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
            </div>        
            """,
            False,
        ),
        (
            "invalid-wit-missing-id",
            """
            <div>
                <witness/>
                <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d"/>
            </div>        
            """,
            False,
        ),
    ],
)
def test_constraint_sch_att_wit(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraint for @wit."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-hand-referencing-a-handNote-element",
            """
            <div>
                <handNote xml:id="otherHand" />
                <handShift hand="otherHand"/>
            </div>        
            """,
            True,
        ),
        (
            "invalid-hand-referencing-a-wrong-element",
            """
            <div>
                <anchor xml:id="otherHand" />
                <handShift hand="otherHand"/>
            </div>        
            """,
            False,
        ),
        (
            "invalid-hand-referencing-no-xml-id",
            """
            <div>
                <handShift hand="otherHand"/>
            </div>        
            """,
            False,
        ),
    ],
)
def test_constraint_sch_att_hand(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraint for @hand."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-attribute-value-without-whitespace",
            "<TEI type='bar'></TEI>",
            True,
        ),
        (
            "valid_attribute-values-with-whitespace-in-between",
            "<TEI type='bar foo'></TEI>",
            True,
        ),
        (
            "invalid-attribute-value-starting-with-whitespace",
            "<TEI type=' foo'></TEI>",
            False,
        ),
        (
            "invalid-attribute-value-ending-with-whitespace",
            "<TEI type='foo '></TEI>",
            False,
        ),
    ],
)
def test_constraint_sch_trim_attributes(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test, if an attribute value starts or ends with whitespace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-single-attribute-value",
            "<damage agent='clipping'><unclear>foo</unclear></damage>",
            True,
        ),
        (
            "valid-multiple-attribute-values",
            "<damage agent='clipping cancelled'><unclear>foo</unclear></damage>",
            True,
        ),
        (
            "invalid-duplicate-attribute-values",
            "<damage agent='clipping clipping'><unclear>foo</unclear></damage>",
            False,
        ),
        (
            "invalid-duplicate-attribute-values-in-random-order",
            "<damage agent='clipping cancelled clipping'><unclear>foo</unclear></damage>",
            False,
        ),
    ],
)
def test_constraint_sch_duplicate_attribute_values(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test that no attribute has duplicate attribute values."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-ab",
            "<ab type='dorsal' place='cover'/>",
            False,
        ),
        (
            "invalid-empty-abbr",
            "<abbr/>",
            False,
        ),
        (
            "invalid-empty-add",
            "<add place='left_top'/>",
            False,
        ),
        (
            "invalid-empty-author",
            "<author/>",
            False,
        ),
        (
            "invalid-empty-availability",
            "<availability/>",
            False,
        ),
        (
            "invalid-empty-bibl",
            "<bibl/>",
            False,
        ),
        (
            "invalid-empty-body",
            "<body/>",
            False,
        ),
        (
            "invalid-empty-custEvent",
            "<custEvent type='lost' notBefore-custom='1858-09-01' calendar='gregorian'/>",
            False,
        ),
        (
            "invalid-empty-del",
            "<del/>",
            False,
        ),
        (
            "invalid-empty-div",
            "<div/>",
            False,
        ),
        (
            "invalid-empty-expan",
            "<expan/>",
            False,
        ),
        (
            "invalid-empty-foreign",
            "<foreign xml:lang='la'/>",
            False,
        ),
        (
            "invalid-empty-fw",
            "<fw type='catchword'/>",
            False,
        ),
        (
            "invalid-empty-head",
            "<head/>",
            False,
        ),
        (
            "invalid-empty-hi",
            "<hi rend='italic'/>",
            False,
        ),
        (
            "invalid-empty-idno",
            "<idno xml:lang='de' source='http://foo.bar'/>",
            False,
        ),
        (
            "invalid-empty-item",
            "<item/>",
            False,
        ),
        (
            "invalid-empty-label",
            "<label type='keyword' place='left_margin'/>",
            False,
        ),
        (
            "invalid-empty-lem",
            "<lem/>",
            False,
        ),
        (
            "invalid-empty-licence",
            "<licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'/>",
            False,
        ),
        (
            "invalid-empty-note",
            "<note/>",
            False,
        ),
        (
            "invalid-empty-num",
            "<num value='1'/>",
            False,
        ),
        (
            "invalid-empty-orgName",
            "<orgName ref='org000001'/>",
            False,
        ),
        (
            "invalid-empty-orig",
            "<orig/>",
            False,
        ),
        (
            "invalid-empty-p",
            "<p/>",
            False,
        ),
        (
            "invalid-empty-persName",
            "<persName/>",
            False,
        ),
        (
            "invalid-empty-placeName",
            "<placeName/>",
            False,
        ),
        (
            "invalid-empty-publisher",
            "<publisher/>",
            False,
        ),
        (
            "invalid-empty-pubPlace",
            "<pubPlace ref='loc123456'/>",
            False,
        ),
        (
            "invalid-empty-q",
            "<q/>",
            False,
        ),
        (
            "invalid-empty-quote",
            "<quote/>",
            False,
        ),
        (
            "invalid-empty-repository",
            "<repository xml:lang='de'/>",
            False,
        ),
        (
            "invalid-empty-seg",
            "<seg/>",
            False,
        ),
        (
            "invalid-empty-settlement",
            "<settlement ref='loc000001' xml:lang='de'/>",
            False,
        ),
        (
            "invalid-empty-signed",
            "<signed/>",
            False,
        ),
        (
            "invalid-empty-supplied",
            "<supplied reason='omitted'/>",
            False,
        ),
        (
            "invalid-empty-time",
            "<time when-custom='08:48:00'/>",
            False,
        ),
        (
            "invalid-empty-title",
            "<title/>",
            False,
        ),
        (
            "invalid-empty-unclear",
            "<unclear/>",
            False,
        ),
    ],
)
def test_constraint_sch_non_empty_elements(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Tests the usage of text() for multiple elements."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-node-with-normal-whitespace",
            "<p>foo bar</p>",
            True,
        ),
        (
            "invalid-node-with-text-using-nbsp-as-unicode",
            "<p>foo bar</p>",
            False,
        ),
        (
            "invalid-node-with-text-using-nbsp-as-decimal-entity",
            "<p>foo&#160;bar</p>",
            False,
        ),
        (
            "invalid-node-with-text-using-nbsp-as-hexadecimal-entity",
            "<p>foo&#xA0;bar</p>",
            False,
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
