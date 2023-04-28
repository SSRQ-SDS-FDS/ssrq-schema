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
            "supplied-valid",
            "<supplied>foo</supplied>",
            True,
        ),
        (
            "supplied-valid-with-reason",
            "<supplied reason='omitted'>foo</supplied>",
            True,
        ),
        (
            "supplied-valid-with-resp",
            "<supplied resp='CS'>foo</supplied>",
            True,
        ),
        (
            "supplied-valid-with-multiple-attributes",
            "<supplied resp='CS' reason='omitted'>foo</supplied>",
            True,
        ),
        (
            "supplied-with-invalid-attribute",
            "<supplied cert='bar'>foo</supplied>",
            False,
        ),
    ],
)
def test_supplied(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("supplied", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-supplied-source",
            "<supplied source='#73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>",
            True,
        ),
        (
            "invalid-supplied-source",
            "<supplied source='something-completely-different'>foo</supplied>",
            False,
        ),
        (
            "invalid-supplied-conflicting-attributes",
            "<supplied source='#73988c1a-40e1-4527-94b7-736d418b29d0' resp='foo'>bar</supplied>",
            False,
        ),
    ],
)
def test_supplied_constraints(main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool):
    """Test the constraints defined for tei:supplied."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(files=writer.list(), isosch=main_constraints)
    assert reports[0].is_valid() is result
