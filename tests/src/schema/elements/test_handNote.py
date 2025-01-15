import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handNote-empty",
            "<handNote xml:id='otherHand'/>",
            True,
        ),
        (
            "valid-handNote-with-scribe-attribute",
            "<handNote xml:id='hand10c' scribe='per000123'/>",
            True,
        ),
        (
            "valid-handNote-with-date",
            """
            <handNote xml:id='firstHand'>
                <date from-custom='1001-01-01' to-custom='1100-12-31'/>
            </handNote>""",
            True,
        ),
        (
            "valid-handNote-with-p",
            "<handNote xml:id='secondHand'><p>bar</p></handNote>",
            True,
        ),
        (
            "invalid-handNote-without-xml-id",
            "<handNote/>",
            False,
        ),
        (
            "valid-handNote-with-uuid",
            "<handNote xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>",
            True,
        ),
        (
            "invalid-handNote-with-random-id",
            "<handNote xml:id='foo'/>",
            False,
        ),
    ],
)
def test_hand_note(
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
            "<TEI><handNote xml:id='otherHand'/><p hand='otherHand'>bar</p></TEI>",
            True,
        ),
        (
            "invalid-handNote-without-reference",
            "<TEI><handNote xml:id='otherHand'/></TEI>",
            False,
        ),
    ],
)
def test_hand_note_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
