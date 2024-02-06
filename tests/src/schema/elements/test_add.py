import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-add",
            "<add place='left_top'>bar</add>",
            True,
        ),
        (
            "valid-with-attributes",
            "<add place='left_top' type='sign' rend='other_ink'>bar</add>",
            True,
        ),
        (
            "valid-with-hand",
            "<add place='left_top' type='sign' rend='other_ink' hand='foo'>bar</add>",
            True,
        ),
        (
            "invalid-add-without-place",
            "<add>bar</add>",
            False,
        ),
        (
            "valid-add-with-wrong-attribute-values",
            "<add place='baz' type='foo'>bar</add>",
            False,
        ),
        (
            "valid-add-with-wrong-attributess",
            "<add place='left_top' att='foo'>bar</add>",
            False,
        ),
    ],
)
def test_add(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("add", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-add",
            "<add/>",
            False,
        ),
        (
            "invalid-add-without-matching-handNote",
            "<add place='left_top' type='sign' rend='other_ink' hand='otherHand'>bar</add>",
            False,
        ),
        (
            "valid-add-with-matching-handNote",
            "<div><handNote xml:id='otherHand'/><add place='left_top' type='sign' rend='other_ink' hand='otherHand'>bar</add></div>",
            True,
        ),
        (
            "invalid-add-with-matching-wrong-element",
            "<div xml:id='otherHand'><add place='left_top' type='sign' rend='other_ink' hand='otherHand'>bar</add></div>",
            False,
        ),
    ],
)
def test_add_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
