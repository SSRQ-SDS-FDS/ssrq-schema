import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ab-with-text-content",
            "<ab type='dorsal' place='left_margin'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-default-content",
            "<ab type='dorsal' place='left_margin'><persName>Foo</persName> bar</ab>",
            True,
        ),
        (
            "invalid-ab-without-type",
            "<ab place='left_margin'>Foo</ab>",
            False,
        ),
        (
            "invalid-ab-without-place",
            "<ab type='dorsal'>Foo</ab>",
            False,
        ),
        (
            "valid-ab-with-hand",
            "<ab type='dorsal' place='left_margin' hand='hand20cf'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-rend",
            "<ab type='dorsal' place='left_margin' rend='pencil'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-rend-rotated",
            "<ab type='dorsal' place='left_margin' rend='rotated_180'>Foo</ab>",
            True,
        ),
        (
            "valid-ab-with-xml-lang",
            "<ab type='dorsal' place='left_margin' xml:lang='de'>Foo</ab>",
            True,
        ),
    ],
)
def test_ab_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("ab", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ab-with-hi-and-text",
            "<ab type='dorsal' place='left_margin'><hi rend='italic'>Foo</hi> bar</ab>",
            True,
        ),
        (
            "invalid-ab-with-hi-only",
            "<ab type='dorsal' place='left_margin'><hi rend='rotated_180'>Foo</hi> </ab>",
            False,
        ),
    ],
)
def test_ab_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
