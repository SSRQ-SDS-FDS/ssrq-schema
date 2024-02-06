import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measure",
            "<measure type='currency' origin='ZH' unit='lb' quantity='2'>zwai phunt nuwer Zuricher</measure>",
            True,
        ),
        (
            "valid-measure-with-commodity",
            "<measure type='weight' unit='Zentner' quantity='1' commodity='wool'>ein zentner landtwull</measure>",
            True,
        ),
        (
            "measure-with-invalid-commodity",
            "<measure type='weight' unit='Zentner' quantity='1' commodity='bar'>ein zentner landtwull</measure>",
            False,
        ),
        (
            "valid-measure-as-text-scope",
            "<measure type='text_scope' unit='leaf' quantity='1'/>",
            True,
        ),
        (
            "measure-with-invalid-type",
            "<measure type='foo' unit='leaf' quantity='1'/>",
            False,
        ),
        (
            "invalid-measure-without-type",
            "<measure unit='leaf' quantity='1'/>",
            False,
        ),
        (
            "invalid-measure-without-unit",
            "<measure type='currency' origin='ZH' quantity='2'>zwai phunt nuwer Zuricher</measure>",
            False,
        ),
    ],
)
def test_measure(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("measure", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, message, result",
    [
        (
            "valid-measure-with-text",
            "<measure type='currency' unit='Angster' quantity='8' commodity='field'>bar</measure>",
            None,
            True,
        ),
        (
            "valid-area-unit",
            "<measure type='area' unit='Juchart' quantity='8' commodity='field'>acht juchart acher</measure>",
            None,
            True,
        ),
        (
            "invalid-area-unit",
            "<measure type='area' unit='bar' quantity='8' commodity='field'>acht juchart acher</measure>",
            "is not a valid area measurement",
            False,
        ),
        (
            "valid-scope-unit",
            "<extent><measure type='text_scope' unit='leaf' quantity='8'/></extent>",
            None,
            True,
        ),
        (
            "invalid-scope-unit",
            "<measure type='text_scope' unit='bar' quantity='8'/>",
            "is no valid scope measurement",
            False,
        ),
    ],
)
def test_measure_constraints(
    main_constraints: str,
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    message: str,
    result: bool,
):
    writer.write(name, add_tei_namespace(markup))

    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )

    if result is True:
        assert reports[0].report.is_valid() is True
    else:
        errors = []
        if reports[0].report.failed_asserts:
            for error in reports[0].report.failed_asserts:
                errors.append(error.text)
        if reports[0].report.successful_reports:
            for error in reports[0].report.successful_reports:
                errors.append(error.text)
        assert any(message in e for e in errors) is True
