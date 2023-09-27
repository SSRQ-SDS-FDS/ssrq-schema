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
            "invalid-origPlace-without-ref",
            "<origPlace >foo</origPlace>",
            False,
        ),
        (
            "valid-origPlace-with-ref",
            "<origPlace ref='loc000001'>foo</origPlace>",
            True,
        ),
        (
            "valid-origPlace-with-ref-and-cert",
            "<origPlace ref='loc000001' cert='low'>foo</origPlace>",
            True,
        ),
        (
            "invalid-origPlace-with-ref-and-type",
            "<origPlace ref='loc000001' type='bar'>foo</origPlace>",
            False,
        ),
    ],
)
def test_origPlace_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origPlace", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origPlace-with-ref",
            "<origin><origPlace ref='loc000001'>foo</origPlace></origin>",
            True,
        ),
        (
            "valid-origPlace-without-attr-or-text",
            "<origin><origPlace/></origin>",
            False,
        ),
    ],
)
def test_series_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
