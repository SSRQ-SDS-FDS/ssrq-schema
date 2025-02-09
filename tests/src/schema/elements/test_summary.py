import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

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
            "valid-summary-with-multiple-ps",
            "<summary xml:lang='de'><p>foo</p><p>bar</p></summary>",
            True,
        ),
        (
            "invalid-summary-with-wrong-content",
            "<summary xml:lang='de'>foo</summary>",
            False,
        ),
        (
            "invalid-summary-without-xml-lang",
            "<summary><p>foo</p></summary>",
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
            "invalid-summary-with-p-with-xml-lang",
            "<summary><p xml:lang='fr'>foo</p></summary>",
            False,
        ),
    ],
)
def test_summary_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
