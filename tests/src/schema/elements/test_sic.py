import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-sic-simple", "<sic>bar</sic>", True),
        (
            "valid-sic-with-mixed-content",
            "<sic><lb/><term ref='lem014672.11'>hexenry</term> bar</sic>",
            True,
        ),
        (
            "invalid-sic-simple-with-attribute",
            "<sic n='1'>bar</sic>",
            False,
        ),
    ],
)
def test_sic(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sic", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sic-with-text",
            "<sic>bar</sic>",
            True,
        ),
    ],
)
def test_sic_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
