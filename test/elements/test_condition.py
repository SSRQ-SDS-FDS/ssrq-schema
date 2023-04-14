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
            "valid-condition-with-text-only",
            "<condition>Mäusefrass</condition>",
            True,
        ),
        (
            "valid-condition-with-p",
            "<condition><p>Mäusefrass</p></condition>",
            True,
        ),
        (
            "invalid-condition-with-div",
            "<condition><div>Mäusefrass</div></condition>",
            False,
        ),
    ],
)
def test_condition_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("condition", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-condition-with-text-only",
            "<condition>Mäusefrass</condition>",
            True,
        ),
        (
            "valid-condition-with-p",
            "<condition><p>Mäusefrass</p></condition>",
            True,
        ),
        (
            "invalid-condition-without-text-or-child",
            "<condition/>",
            False,
        ),
    ],
)
def test_condition_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:pubPlace."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
