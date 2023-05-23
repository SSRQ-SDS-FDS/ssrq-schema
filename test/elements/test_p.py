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
            "valid-simple-p",
            "<p>foo</p>",
            True,
        ),
        (
            "valid-simple-p-with-attr",
            "<p xml:lang='de'>foo</p>",
            True,
        ),
        (
            "simple-p-with-invalid-attr",
            "<p rend='black'>foo</p>",
            False,
        ),
        (
            "simple-p-with-invalid-attr",
            "<p xml:id='facs'>foo</p>",
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
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
