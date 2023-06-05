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
            "valid-figure-without-content",
            "<figure type='locus sigilli'/>",
            True,
        ),
        (
            "valid-figure-with-content",
            "<figure type='illustration'><graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/></figure>",
            True,
        ),
        (
            "invalid-figure-without-content",
            "<figure type='foo'/>",
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
            "<figure type='locus sigilli'/>",
            True,
        ),
        (
            "valid-figure-with-type-illustration",
            "<figure type='illustration'><graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/></figure>",
            True,
        ),
        (
            "invalid-figure-with-type-illustration",
            "<figure type='illustration'/>",
            False,
        ),
    ],
)
def test_figure_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
