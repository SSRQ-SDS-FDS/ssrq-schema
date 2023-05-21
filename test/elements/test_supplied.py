import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-supplied-source",
            "<supplied source='73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>",
            False,
            "without matching ID",
        ),
        (
            "invalid-supplied-source",
            "<supplied source='bar'>foo</supplied>",
            False,
            None,
        ),
        (
            "supplied-valid-with-reason",
            "<supplied reason='omitted'>foo</supplied>",
            True,
            None,
        ),
        (
            "supplied-valid-with-resp",
            "<supplied resp='CS'>foo</supplied>",
            True,
            None,
        ),
        (
            "supplied-valid-with-multiple-attributes",
            "<supplied resp='CS' reason='omitted'>foo</supplied>",
            True,
            None,
        ),
        (
            "supplied-with-invalid-attribute",
            "<supplied cert='bar'>foo</supplied>",
            False,
            None,
        ),
    ],
)
def test_supplied(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("supplied", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng(
            "supplied", name, markup, result, True
        )
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("supplied", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-supplied-source",
            "<supplied source='73988c1a-40e1-4527-94b7-736d418b29d0'>foo</supplied>",
            True,
        ),
        (
            "invalid-supplied-source",
            "<supplied>foo</supplied>",
            False,
        ),
        (
            "invalid-supplied-conflicting-attributes",
            "<supplied source='73988c1a-40e1-4527-94b7-736d418b29d0' resp='foo'>bar</supplied>",
            False,
        ),
    ],
)
def test_supplied_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:supplied."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
