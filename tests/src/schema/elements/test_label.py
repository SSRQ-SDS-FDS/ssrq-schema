import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-label",
            "<label type='keyword' place='left_margin'>bar baz foo</label>",
            True,
        ),
        (
            "invalid-label-without-place",
            "<label type='keyword'>bar baz foo</label>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("label", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-label",
            "<label type='keyword' place='left_margin'/>",
            False,
        ),
        (
            "valid-label-after-lb",
            "<p><lb/><label type='keyword' place='left_margin'>bar baz foo</label></p>",
            True,
        ),
        (
            "invalid-label-without-lb",
            "<p><label type='keyword' place='left_margin'>bar baz foo</label></p>",
            False,
        ),
    ],
)
def test_label_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
