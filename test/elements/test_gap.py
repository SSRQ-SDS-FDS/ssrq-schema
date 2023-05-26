import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

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
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
