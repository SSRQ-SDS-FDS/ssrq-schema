import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-subst",
            "<subst><del>foo</del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "valid-subst-add-first",
            "<subst><add place='left_top'>bar</add><del>foo</del></subst>",
            True,
        ),
        (
            "valid-subst-with-lb-and-pb",
            "<subst><del>foo</del><pb/><lb/><add place='inline'>bar</add></subst>",
            True,
        ),
        (
            "invalid-subst-with-wrong-content",
            "<subst><note>bar</note><p>foo</p></subst>",
            False,
        ),
        (
            "invalid-subst-with-multiple-adds",
            "<subst><add place='above'>foo</add><add place='above'>bar</add><del>baz</del></subst>",
            False,
        ),
        (
            "invalid-subst-with-multiple-dels",
            "<subst><del>foo</del><add place='above'>bar</add><del>baz</del></subst>",
            False,
        ),
        (
            "invalid-subst-with-multiple-lbs",
            "<subst><lb/><del>foo</del><lb/><add place='inline'>bar</add></subst>",
            False,
        ),
        (
            "invalid-subst-with-multiple-pbs",
            "<subst><pb/><del>foo</del><pb/><add place='inline'>bar</add></subst>",
            False,
        ),
        (
            "valid-subst-with-type",
            "<subst type='cypher'><del>foo</del><add place='left_top'>bar</add></subst>",
            True,
        ),
    ],
)
def test_subst(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("subst", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-subst",
            "<subst><del>foo</del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "valid-subst-with-lb-and-pb",
            "<subst><del>foo</del><pb/><lb/><add place='inline'>bar</add></subst>",
            True,
        ),
        (
            "invalid-subst-with-wrong-order",
            "<subst><add place='left_top'>bar</add><del>foo</del></subst>",
            False,
        ),
        (
            "invalid-subst-with-lb-and-pb-and-wrong-order",
            "<subst><add place='inline'>bar</add><pb/><del>foo</del><lb/></subst>",
            False,
        ),
    ],
)
def test_subst_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
