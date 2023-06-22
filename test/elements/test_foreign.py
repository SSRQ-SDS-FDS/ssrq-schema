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
            "valid-foreign",
            "<foreign xml:lang='la'>foo</foreign>",
            True,
        ),
        (
            "foreign-with-invalid-lang",
            "<foreign xml:lang='latin'>foo</foreign>",
            False,
        ),
        (
            "invalid-foreign-without-lang",
            "<foreign>foo</foreign>",
            False,
        ),
    ],
)
def test_foreign(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("foreign", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-foreign",
            "<foreign xml:lang='la'/>",
            False,
        ),
    ],
)
def test_foreign_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
