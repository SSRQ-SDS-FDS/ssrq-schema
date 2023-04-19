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
            "valid-dimensions-with-two-childs",
            "<dimensions type='leaves'><height unit='cm' quantity='16.0'/><width unit='cm' quantity='23.0'/></dimensions>",
            True,
        ),
        (
            "valid-dimensions-with-one-childs",
            "<dimensions type='plica'><width unit='cm' quantity='23.0'/></dimensions>",
            True,
        ),
        (
            "invalid-dimensions-without-child",
            "<dimensions type='plica'/>",
            False,
        ),
        (
            "dimensions-with-invalid-type",
            "<dimensions type='foo'><width unit='cm' quantity='23.0'/></dimensions>",
            False,
        ),
        (
            "invalid-dimensions-with-additional-attribute",
            "<dimensions source='bar' type='leaves'><height unit='cm' quantity='16.0'/><width unit='cm' quantity='23.0'/></dimensions>",
            False,
        ),
    ],
)
def test_dimensions_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("dimensions", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-dimensions-type-child-combination",
            "<dimensions type='plica'><width unit='cm' quantity='23.0'/></dimensions>",
            True,
        ),
        (
            "invalid-dimensions-type-child-combination",
            "<dimensions type='plica'><height unit='cm' quantity='23.0'/></dimensions>",
            False,
        ),
    ],
)
def test_dimensions_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:extent."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
