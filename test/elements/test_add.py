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
            "valid-add",
            "<add place='left_top'>bar</add>",
            True,
            None,
        ),
        (
            "valid-with-attributes",
            "<add place='left_top' type='sign' rend='other_ink'>bar</add>",
            True,
            None,
        ),
        (
            "invalid-add-without-place",
            "<add>bar</add>",
            False,
            None,
        ),
        (
            "valid-add-with-wrong-attribute-values",
            "<add place='baz' type='foo'>bar</add>",
            False,
            None,
        ),
        (
            "valid-add-with-wrong-attributess",
            "<add place='left_top' att='foo'>bar</add>",
            False,
            None,
        ),
        (
            "valid-add-with-hand-attribute",
            "<add place='left_top' hand='otherHand'>bar</add>",
            False,
            "without matching ID",
        ),
    ],
)
def test_add(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("add", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("add", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("add", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-add",
            "<add/>",
            False,
        ),
    ],
)
def test_add_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
