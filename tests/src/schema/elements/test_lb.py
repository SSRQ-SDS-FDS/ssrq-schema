import pytest
from pyschval.schematron.model.svrl import Role
from pyschval.schematron.validate import apply_schematron_validation

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-lb",
            "<lb/>",
            True,
        ),
        (
            "valid-lb-with-break",
            "<lb break='no'/>",
            True,
        ),
        (
            "valid-lb-with-facs",
            "<lb facs='StAZH_C_VI_7_3_Nr_1_v2'/>",
            True,
        ),
        (
            "invalid-lb-with-content",
            "<lb>foo</lb>",
            False,
        ),
    ],
)
def test_lb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("lb", name, markup, result, False)


@pytest.mark.parametrize("attribute", ["", ' break="no"'])
@pytest.mark.parametrize(
    "separator", ["", " ", "\n\t", "<!-- comment -->", " <?test value?> "]
)
def test_lb_before_pb(
    main_constraints: str, writer: SimpleTEIWriter, attribute: str, separator: str
):
    markup = f"<body><p>Wortanfang<lb{attribute}/>{separator}<pb/>Wortende</p></body>"
    writer.write("wrong-order", add_tei_namespace(markup))
    reports = apply_schematron_validation(input=writer.list(), isosch=main_constraints)
    assert not reports[0].report.is_valid(all_error_types=False)


@pytest.mark.parametrize(
    "markup, warning_count",
    [
        ('Wortanfang<pb/><lb break="no"/>Wortende', 0),
        ('Wortanfang<pb/><!-- comment --><lb break="no"/>Wortende', 0),
        ('<hi>Wortanfang</hi><pb/><lb break="no"/><hi>Wortende</hi>', 0),
        ('Wortanfang <pb/><lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/> <lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/><lb break="no"/> Wortende', 1),
        ('Wortanfang\t<pb/><lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/>\n<lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/><lb break="no"/>\tWortende', 1),
        ('Wortanfang&#160;<pb/><lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/>&#160;<lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/><lb break="no"/>&#160;Wortende', 1),
        ('<hi>Wortanfang </hi><pb/><lb break="no"/>Wortende', 1),
        ('Wortanfang<pb/><lb break="no"/><hi> Wortende</hi>', 1),
        ('Wortanfang<pb/> <!-- comment --> <lb break="no"/>Wortende', 1),
        ("Wort <pb/> <lb/> Wort", 0),
        ("<pb/>\n<lb/>Text", 0),
        ('Wortanfang<lb break="no"/>Wortende', 0),
        ('Wortanfang <lb break="no"/>Wortende', 1),
        ('Wortanfang\n <lb break="no"/>Wortende', 1),
        ('Wortanfang<lb break="no"/> Wortende', 1),
        ('Wortanfang <pb/> <lb break="no"/> Wortende', 3),
        ("Wort<lb/>weiterer Text<pb/><lb/>Text", 0),
        ("<hi>Text<lb/></hi><pb/><lb/>Text", 0),
    ],
)
def test_lb_page_break_constraints(
    main_constraints: str, writer: SimpleTEIWriter, markup: str, warning_count: int
):
    writer.write("page-break", add_tei_namespace(f"<body><p>{markup}</p></body>"))
    reports = apply_schematron_validation(input=writer.list(), isosch=main_constraints)
    # Whitespace is a formatting issue and should warn without invalidating the
    # document. The pb/lb order remains a structural error (tested above).
    report = reports[0].report
    assert report.is_valid(all_error_types=False)
    warnings = [
        item
        for item in report.successful_reports or []
        if item.text.startswith("Whitespace is not allowed")
    ]
    assert len(warnings) == warning_count
    assert all(item.role == Role.WARN for item in warnings)
    assert report.is_valid() is (warning_count == 0)
