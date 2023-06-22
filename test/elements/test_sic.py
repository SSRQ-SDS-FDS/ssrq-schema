import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

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
        (
            "invalid-empty-sic",
            "<sic/>",
            False,
        ),
    ],
)
def test_sic_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
