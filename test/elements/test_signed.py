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
            "valid-signed",
            "<signed><persName ref='per008827'>Jean Jacques Purry</persName></signed>",
            True,
        ),
        (
            "invalid-signed-with-attribute",
            "<signed type='foo'><persName ref='per008827'>Jean Jacques Purry</persName></signed>",
            False,
        ),
    ],
)
def test_signed(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("signed", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-signed",
            "<signed/>",
            False,
        ),
    ],
)
def test_signed_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
