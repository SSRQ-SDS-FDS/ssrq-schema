import pytest
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
    assert not reports[0].report.is_valid()


@pytest.mark.parametrize(
    "markup, valid",
    [
        ('Wortanfang<pb/><lb break="no"/>Wortende', True),
        ('Wortanfang<pb/><!-- comment --><lb break="no"/>Wortende', True),
        ('<hi>Wortanfang</hi><pb/><lb break="no"/><hi>Wortende</hi>', True),
        ('Wortanfang <pb/><lb break="no"/>Wortende', False),
        ('Wortanfang<pb/> <lb break="no"/>Wortende', False),
        ('Wortanfang<pb/><lb break="no"/> Wortende', False),
        ('Wortanfang\t<pb/><lb break="no"/>Wortende', False),
        ('Wortanfang<pb/>\n<lb break="no"/>Wortende', False),
        ('Wortanfang<pb/><lb break="no"/>\tWortende', False),
        ('Wortanfang&#160;<pb/><lb break="no"/>Wortende', False),
        ('Wortanfang<pb/>&#160;<lb break="no"/>Wortende', False),
        ('Wortanfang<pb/><lb break="no"/>&#160;Wortende', False),
        ('<hi>Wortanfang </hi><pb/><lb break="no"/>Wortende', False),
        ('Wortanfang<pb/><lb break="no"/><hi> Wortende</hi>', False),
        ('Wortanfang<pb/> <!-- comment --> <lb break="no"/>Wortende', False),
        ("Wort <pb/> <lb/> Wort", True),
        ("<pb/>\n<lb/>Text", True),
        ('Wortanfang<lb break="no"/>Wortende', True),
        ('Wortanfang <lb break="no"/>Wortende', False),
        ('Wortanfang\n <lb break="no"/>Wortende', False),
        ("Wort<lb/>weiterer Text<pb/><lb/>Text", True),
        ("<hi>Text<lb/></hi><pb/><lb/>Text", True),
    ],
)
def test_lb_page_break_constraints(
    main_constraints: str, writer: SimpleTEIWriter, markup: str, valid: bool
):
    writer.write("page-break", add_tei_namespace(f"<body><p>{markup}</p></body>"))
    reports = apply_schematron_validation(input=writer.list(), isosch=main_constraints)
    assert reports[0].report.is_valid() is valid
