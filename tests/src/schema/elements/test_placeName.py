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
            "valid-placeName",
            "<placeName>bar</placeName>",
            True,
        ),
        (
            "valid-placeName-with-ref",
            "<placeName ref='loc000001'>bar</placeName>",
            True,
        ),
        (
            "placeName-with-invalid-ref",
            "<placeName ref='abcdefg'>bar</placeName>",
            False,
        ),
    ],
)
def test_placeName(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("placeName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-placeName",
            "<placeName ref='loc123456'/>",
            False,
        ),
    ],
)
def test_placeName_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
