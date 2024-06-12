import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-expan",
            "<expan>bar</expan>",
            True,
        ),
        (
            "valid-expan-with-entity-content",
            "<expan><persName ref='per123456'>bar</persName></expan>",
            True,
        ),
        (
            "valid-expan-with-attributes",
            "<expan cert='high' resp='CS'>foo</expan>",
            True,
        ),
        (
            "invalid-expan-with-wrong-attribute",
            "<expan att='foo'>bar</expan>",
            False,
        ),
        (
            "invalid-expan-with-wrong-content",
            "<expan><p>bar</p></expan>",
            False,
        ),
    ],
)
def test_expan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("expan", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-expan",
            "<expan/>",
            False,
        ),
    ],
)
def test_expan_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
