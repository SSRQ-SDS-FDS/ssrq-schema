import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)
from saxonche import PySaxonProcessor

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
            "valid-measure-as-text-scope",
            "<measure type='text_scope' unit='leaf' quantity='1'/>",
            True,
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
            "invalid-empty-measure",
            "<measure type='area' unit='Juchart' quantity='8' commodity='field'/>",
            "measure must not be empty",
            False,
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
    """Test the constraints defined for tei:measure."""
    writer.write(name, add_tei_namespace(markup))

    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )

    if result is True:
        assert reports[0].is_valid() is True
    else:
        with PySaxonProcessor(license=False) as proc:
            xp = proc.new_xpath_processor()
            xml = reports[0].report
            node = proc.parse_xml(xml_text=xml)
            xp.set_context(xdm_item=node)
            item = xp.evaluate_single(
                f"//*:text[contains(normalize-space(.), '{message}')]"
            )
            assert bool(item) is not result
