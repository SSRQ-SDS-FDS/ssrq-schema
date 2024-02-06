import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-fw",
            "<fw type='catchword'>foo</fw>",
            True,
        ),
        (
            "invalid-fw-with-wrong-type",
            "<fw type='bar'>foo</fw>",
            False,
        ),
        (
            "invalid-fw-without type",
            "<fw>foo</fw>",
            False,
        ),
    ],
)
def test_fw(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("fw", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-fw",
            "<fw type='catchword'/>",
            False,
        ),
    ],
)
def test_fw_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
