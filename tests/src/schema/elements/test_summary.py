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
            "valid-summary",
            "<summary xml:lang='de'><p>foo</p></summary>",
            True,
        ),
        (
            "invalid-summary",
            "<summary>foo</summary>",
            False,
        ),
    ],
)
def test_summary_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("summary", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-summary",
            "<summary xml:lang='de'><p>foo</p><p>foo</p></summary>",
            True,
        ),
        (
            "invalid-summary-with-p-bearing.xml-lang",
            "<summary><p>foo</p><p xml:lang='fr'>foo</p></summary>",
            False,
        ),
    ],
)
def test_summary_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
