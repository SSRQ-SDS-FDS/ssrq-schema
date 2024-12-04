import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-height",
            "<height quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-height-without-unit",
            "<height quantity='3'/>",
            False,
        ),
        (
            "invalid-height-without-quantity",
            "<height unit='cm'/>",
            False,
        ),
        (
            "invalid-height-without-unit-and-quantity",
            "<height/>",
            False,
        ),
        (
            "invalid-height-with-content",
            "<height quantity='3' unit='cm'>foo</height>",
            False,
        ),
    ],
)
def test_height(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("height", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-height-with-unknown-values",
            "<height quantity='unknown' unit='unknown'/>",
            True,
        ),
        (
            "invalid-height-with-unknown-values",
            "<height quantity='1' unit='unknown'/>",
            False,
        ),
    ],
)
def test_height_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
