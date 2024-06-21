import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-simple-p",
            "<p>foo</p>",
            True,
        ),
        (
            "valid-simple-p-with-attr",
            "<p xml:lang='de' n='1'>foo</p>",
            True,
        ),
        (
            "p-with-invalid-content",
            "<p><row>bar</row></p>",
            False,
        ),
        (
            "simple-p-with-invalid-attr",
            "<p rend='black' xml:id='facs'>foo</p>",
            False,
        ),
        (
            "invalid-p-with-corr",
            "<p xml:lang='de'><corr>foo</corr></p>",
            False,
        ),
    ],
)
def test_p(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("p", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-simple-p-with-attr",
            "<p xml:lang='de'>foo</p>",
            True,
        ),
        (
            "valid-simple-ps-with-attr",
            "<div><p xml:lang='de'>foo</p><p xml:lang='de'>foo</p></div>",
            True,
        ),
        (
            "invalid-simple-ps-with-attr",
            "<div><p xml:lang='de'>foo</p><p>foo</p></div>",
            False,
        ),
    ],
)
def test_p_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
