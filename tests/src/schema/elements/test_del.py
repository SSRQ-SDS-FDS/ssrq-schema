import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-del",
            "<del>bar</del>",
            True,
        ),
        (
            "valid-del-with-attributes",
            "<del rend='crossout' hand='otherHand'>bar</del>",
            True,
        ),
        (
            "invalid-del-with-wrong-rend",
            "<del rend='foo'>bar</del>",
            False,
        ),
        (
            "invalid-del-with-wrong-attributes",
            "<del att='foo'>bar</del>",
            False,
        ),
    ],
)
def test_del(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("del", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-del",
            "<del/>",
            False,
        ),
        (
            "valid-del-inside-subst",
            "<subst><del>abc</del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "valid-del-inside-subst-with-gap",
            "<subst><del><gap reason='illegible' unit='line' quantity='1.0'/></del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "invalid-del-inside-subst",
            "<subst><del/><add place='left_top'>bar</add></subst>",
            False,
        ),
    ],
)
def test_del_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
