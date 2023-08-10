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
            "valid-height",
            "<height quantity='3' unit='cm'/>",
            True,
        ),
        (
            "valid-height-with-unknown-values",
            "<height quantity='unknown' unit='unknown'/>",
            True,
        ),
        (
            "invalid-height-missing-unit",
            "<height quantity='3'/>",
            False,
        ),
        (
            "invalid-height-wrong-unit",
            "<height quantity='3' unit='bar'/>",
            False,
        ),
        (
            "invalid-height-wrong-quantity",
            "<height quantity='bar' unit='cm'/>",
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
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
