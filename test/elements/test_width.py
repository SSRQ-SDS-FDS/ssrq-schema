from test.conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace

import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-width",
            "<width quantity='3' unit='cm'/>",
            True,
        ),
        (
            "invalid-width-missing-unit",
            "<width quantity='3'/>",
            False,
        ),
        (
            "invalid-width-wrong-unit",
            "<width quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-width-wrong-quantity",
            "<width quantity='bar' unit='cm'/>",
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
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
