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
            "valid-availability",
            "<availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability>",
            True,
        ),
        (
            "invalid-availability-content",
            "<availability/>",
            False,
        ),
        (
            "invalid-availability-with-attribute",
            "<availability type='foo'><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability>",
            False,
        ),
    ],
)
def test_availability_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("availability", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-availability",
            "<availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability>",
            True,
        ),
        (
            "invalid-availability",
            "<availability><p xml:id='bar'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability>",
            False,
        ),
    ],
)
def test_availability_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:availability."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
