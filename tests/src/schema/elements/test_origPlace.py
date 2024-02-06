import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-origPlace-without-ref-and-type",
            "<origPlace >foo</origPlace>",
            False,
        ),
        (
            "valid-origPlace-with-ref",
            "<origPlace ref='loc000001' type='document'>foo</origPlace>",
            True,
        ),
        (
            "valid-origPlace-with-ref-and-cert",
            "<origPlace ref='loc000001' cert='low' type='document'>foo</origPlace>",
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
            "<origin><origPlace ref='loc000001' type='content'>foo</origPlace></origin>",
            True,
        ),
        (
            "invalid-origPlace-without-attr-or-text",
            "<origin><origPlace/></origin>",
            False,
        ),
    ],
)
def test_series_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
