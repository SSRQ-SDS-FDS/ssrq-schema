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
            "invalid-ab-with-scribe",
            "<ab type='dorsal' place='cover' scribe='per011353'><lb/>Copiert - 976 fol</ab>",
            False,
            None,
        ),
        (
            "valid-ab-with-place-and-type",
            "<ab type='dorsal' place='cover'><lb/>Copiert - 976 fol</ab>",
            True,
            None,
        ),
        (
            "valid-ab-with-hand",
            " <ab type='archiving_reference' place='left_margin' hand='hand20cf'>St. Georgenamt FC 2</ab>",
            False,
            "without matching ID",
        ),
        (
            "invalid-ab-without-type",
            " <ab place='left_margin' hand='hand20c'>St. Georgenamt FC 2</ab>",
            False,
            None,
        ),
    ],
)
def test_ab_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("ab", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("ab", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("ab", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-ab",
            "<ab type='archiving_reference' place='left margin' hand='hand20cf'/>",
            False,
        ),
    ],
)
def test_ab_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
