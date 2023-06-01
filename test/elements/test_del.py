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
            "valid-del",
            "<del>bar</del>",
            True,
            None,
        ),
        (
            "valid-del-with-attributes",
            "<del rend='crossout' hand='otherHand'>bar</del>",
            False,
            "without matching ID",
        ),
        (
            "invalid-del-with-wrong-rend",
            "<del rend='foo'>bar</del>",
            False,
            None,
        ),
        (
            "invalid-del-with-wrong-attributes",
            "<del att='foo'>bar</del>",
            False,
            None,
        ),
    ],
)
def test_del(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("del", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("del", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("del", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-del-inside-subst",
            "<subst><del>abc</del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "valid-del-inside-subst-with-gap",
            "<subst><del><gap reason='illegible' unit='line' quantity='1.0'/></del><add place='left_top'>bar</add></subst>",
            True,
        ),
        (
            "invalid-del-inside-subst",
            "<subst><del/><add place='left_top'>bar</add></subst>",
            False,
        ),
    ],
)
def test_del_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
