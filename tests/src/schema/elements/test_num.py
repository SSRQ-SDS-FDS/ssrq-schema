import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-num-with-int",
            "<num value='1'>I</num>",
            True,
        ),
        (
            "invalid-num-with-roman-value",
            "<num value='I'>I</num>",
            False,
        ),
        (
            "invalid-num-without-value",
            "<num>I</num>",
            False,
        ),
        (
            "valid-num-with-floating-point",
            "<num value='3.5'>dreieinhalb</num>",
            True,
        ),
        (
            "num-with-invalid-floating-point",
            "<num value='3.1/2'>dreieinhalb</num>",
            False,
        ),
    ],
)
def test_num(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("num", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-num",
            "<num value='1'/>",
            False,
        ),
    ],
)
def test_num_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
