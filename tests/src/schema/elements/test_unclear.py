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
            "valid-unclear-with-text",
            "<unclear cert='high'>foo</unclear>",
            True,
        ),
        (
            "valid-unclear-with-text-and-child",
            "<unclear cert='high'>foo<hi rend='sup'>bar</hi></unclear>",
            True,
        ),
        (
            "invalid-unclear-with-reason",
            "<unclear cert='high' reason='bar'>foo</unclear>",
            False,
        ),
    ],
)
def test_unclear(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("unclear", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-unclear",
            "<unclear/>",
            False,
        ),
    ],
)
def test_unclear_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
