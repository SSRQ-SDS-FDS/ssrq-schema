import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
