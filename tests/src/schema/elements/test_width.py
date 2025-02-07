import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-width",
            "<width quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-width-without-unit",
            "<width quantity='3'/>",
            False,
        ),
        (
            "invalid-width-without-quantity",
            "<width quantity='3'/>",
            False,
        ),
        (
            "invalid-width-without-unit-and-quantity",
            "<width/>",
            False,
        ),
        (
            "invalid-width-with-content",
            "<width quantity='3' unit='cm'>foo</width>",
            False,
        ),
    ],
)
def test_width(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("width", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-height-with-unknown-values",
            "<width quantity='unknown' unit='unknown'/>",
            True,
        ),
        (
            "invalid-height-with-unknown-values",
            "<width quantity='1' unit='unknown'/>",
            False,
        ),
    ],
)
def test_width_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
