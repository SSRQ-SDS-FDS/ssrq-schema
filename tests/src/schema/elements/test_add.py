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
            "valid-add-with-type",
            "<add place='left_top' type='sign'>bar</add>",
            True,
        ),
        (
            "valid-add-with-hand",
            "<add place='left_top' hand='otherHand'>bar</add>",
            True,
        ),
        (
            "valid-add-with-rend",
            "<add place='left_top' rend='pencil'>bar</add>",
            True,
        ),
        (
            "valid-add-with-p-content",
            "<add place='left_top'><p>bar</p></add>",
            True,
        ),
        (
            "valid-add-with-multiple-ps",
            "<add place='left_top'><p>foo</p><p>bar</p></add>",
            True,
        ),
        (
            "valid-add-with-head-and-ps",
            "<add place='left_top'><head>Foo</head><p>foo</p><p>bar</p></add>",
            True,
        ),
        (
            "invalid-add-with-p-and-content-default",
            "<add place='left_top'><p>foo</p> foo <unclear>bar</unclear></add>",
            False,
        ),
        (
            "valid-add-with-seg-content",
            "<add place='left_top'><seg>foo</seg><seg>bar</seg></add>",
            True,
        ),
        (
            "invalid-add-with-one-seg",
            "<add place='left_top'><seg>foo</seg></add>",
            False,
        ),
        (
            "invalid-add-with-mixed-content",
            "<add place='left_top'><seg>bar</seg> foo <unclear>bar</unclear></add>",
            False,
        ),
        (
            "valid-add-with-mixed-content",
            "<add place='left_top'><del>bar</del> foo <unclear>bar</unclear></add>",
            True,
        ),
        (
            "invalid-add-without-place",
            "<add>bar</add>",
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
            "valid-add-with-del-and-siblings",
            "<add place='left_top'><del>foo</del> bar</add>",
            True,
        ),
        (
            "invalid-add-with-del-without-siblings",
            "<add place='left_top'><del>foo</del></add>",
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
