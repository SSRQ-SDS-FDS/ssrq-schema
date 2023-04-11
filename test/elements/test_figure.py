import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-figure-without-content",
            "<figure xmlns='http://www.tei-c.org/ns/1.0' type='locus sigilli'/>",
            True,
        ),
        (
            "valid-figure-with-content",
            "<figure type='illustration' xmlns='http://www.tei-c.org/ns/1.0'><graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/></figure>",
            True,
        ),
        (
            "invalid-figure-without-content",
            "<figure xmlns='http://www.tei-c.org/ns/1.0' type='foo'/>",
            False,
        ),
    ],
)
def test_figure(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("figure", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-figure-with-type-locus",
            "<figure xmlns='http://www.tei-c.org/ns/1.0' type='locus sigilli'/>",
            True,
        ),
        (
            "valid-figure-with-type-illustration",
            "<figure type='illustration' xmlns='http://www.tei-c.org/ns/1.0'><graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/></figure>",
            True,
        ),
        (
            "invalid-figure-with-type-illustration",
            "<figure type='illustration' xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
    ],
)
def test_figure_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints definid for tei:figure."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
