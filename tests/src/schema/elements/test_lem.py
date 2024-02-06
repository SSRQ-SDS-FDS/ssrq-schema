import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-lem",
            "<lem>bar</lem>",
            True,
        ),
        (
            "valid-lem-with-seg",
            "<lem><seg>foo</seg><seg>bar</seg></lem>",
            True,
        ),
        (
            "invalid-lem-with-seg-and-mixed-content",
            "<lem><seg>foo</seg> bar</lem>",
            False,
        ),
        (
            "invalid-lem-with-just-one-seg",
            "<lem><seg>foo</seg></lem>",
            False,
        ),
        (
            "lem-with-invalid-attribute",
            "<lem att='xyz'>bar</lem>",
            False,
        ),
    ],
)
def test_lem(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("lem", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-lem",
            "<lem/>",
            False,
        ),
    ],
)
def test_lem_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
