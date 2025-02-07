import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-gap",
            "<gap/>",
            True,
        ),
        (
            "invalid-gap-with-content",
            "<gap>Foo</gap>",
            False,
        ),
        (
            "valid-gap-with-source",
            "<gap source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1#n17.1-17.4'/>",
            True,
        ),
        (
            "valid-gap-with-reason",
            "<gap reason='missing'/>",
            True,
        ),
        (
            "valid-gap-with-unit-and-quantity",
            "<gap quantity='1' unit='cm'/>",
            True,
        ),
        (
            "valid-gap",
            "<gap reason='illegible' unit='line' quantity='1.0'/>",
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
            "invalid-gap-inside-damage-with-reason",
            "<damage agent='hole'><gap reason='illegible' unit='cm' quantity='3.5'/></damage>",
            False,
        ),
        (
            "invalid-gap-inside-damage-without-unit",
            "<damage agent='hole'><gap quantity='3.5'/></damage>",
            False,
        ),
        (
            "invalid-gap-inside-damage-without-quantity",
            "<damage agent='hole'><gap unit='cm'/></damage>",
            False,
        ),
        (
            "invalid-gap-inside-damage-without-unit-and-quantity",
            "<damage agent='hole'><gap/></damage>",
            False,
        ),
        (
            "valid-gap-with-reason-illegible",
            "<gap reason='illegible' unit='cm' quantity='3.5'/>",
            True,
        ),
        (
            "invalid-gap-with-reason-illegible-without-unit-and-quantity",
            "<gap reason='illegible'/>",
            False,
        ),
        (
            "invalid-gap-with-source-and-reason",
            "<gap source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1#n17.1-17.4' reason='illegible' />",
            False,
        ),
        (
            "invalid-gap-with-source-and-unit-and-quantity",
            "<gap source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1#n17.1-17.4' quantity='1' unit='cm'/>",
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
