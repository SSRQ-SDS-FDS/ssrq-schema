import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origDate",
            "<origDate type='document' when-custom='1448-05-25' calendar='gregorian'>bar</origDate>",
            True,
        ),
        (
            "invalid-origDate-with-datingMethod",
            "<origDate type='document' when-custom='1448-05-25' datingMethod='gregorian'>bar</origDate>",
            False,
        ),
        (
            "origDate-with-invalid-calendar",
            "<origDate type='document' when-custom='1448-05-25' calendar='...'>bar</origDate>",
            False,
        ),
        (
            "invalid-origDate-without-calendar",
            "<origDate type='document' when-custom='1448-05-25'>bar</origDate>",
            False,
        ),
        (
            "origDate-with-invalid-calendar",
            "<origDate type='document' when-custom='1448-05-25' calendar='Modern'>bar</origDate>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origDate", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origDate-with-text",
            "<origDate type='document' when-custom='1448-05-25' calendar='gregorian'>bar</origDate>",
            True,
        ),
        (
            "valid-origDate-without-text",
            "<origDate type='document' when-custom='1448-05-25' calendar='gregorian'/>",
            True,
        ),
        (
            "invalid-origDate-with-calendar-only",
            "<origDate type='document' calendar='gregorian'>bar</origDate>",
            False,
        ),
    ],
)
def test_origDate_datable_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
