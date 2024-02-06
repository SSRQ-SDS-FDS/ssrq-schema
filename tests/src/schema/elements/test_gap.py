import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-gap",
            "<gap reason='illegible' unit='line' quantity='1.0'/>",
            True,
        ),
        (
            "gap-with-invalid-unit",
            "<gap reason='illegible' unit='lines' quantity='1.0'/>",
            False,
        ),
        (
            "gap-with-invalid-quantity",
            "<gap reason='illegible' unit='line' quantity='eins'/>",
            False,
        ),
        (
            "gap-with-valid-source",
            "<gap source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1#n17.1-17.4'/>",
            True,
        ),
    ],
)
def test_gap_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("gap", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-gap-inside-damage",
            "<damage agent='hole'><gap unit='cm' quantity='3.5'/></damage>",
            True,
        ),
        (
            "invalid-gap-inside-damage",
            "<damage agent='hole'><gap reason='illegible' unit='cm' quantity='3.5'/></damage>",
            False,
        ),
        (
            "valid-gap-with-reason-illegible",
            "<gap reason='illegible' unit='line' quantity='1.0'/>",
            True,
        ),
        (
            "invalid-gap-with-reason-illegible",
            "<gap reason='illegible' quantity='1.0'/>",
            False,
        ),
    ],
)
def test_gap_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
