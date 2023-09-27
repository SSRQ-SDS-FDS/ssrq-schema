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
            "valid-div",
            "<div><p>foo</p></div>",
            True,
        ),
        (
            "valid-div-with-type-and-n",
            "<div type='chapter' n='1'><p>foo</p></div>",
            True,
        ),
        (
            "invalid-div-with-wrong-type",
            "<div type='bar'><p>foo</p></div>",
            False,
        ),
        (
            "invalid-div-with-wrong-attribute",
            "<div wit='bar'><p>foo</p></div>",
            False,
        ),
    ],
)
def test_div(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("div", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-div-without-text",
            "<div><p>foo</p>     </div>",
            True,
        ),
        (
            "valid-div-without-text-with-linebreaks",
            """<div><p>foo</p>
            <p>bar</p>
            <p>baz</p>
            </div>
            """,
            True,
        ),
        (
            "invalid-div-with-text",
            "<div><p>foo</p> hello</div>",
            False,
        ),
    ],
)
def test_div_text_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
