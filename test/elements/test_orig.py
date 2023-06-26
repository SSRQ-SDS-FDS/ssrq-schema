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
            "valid-orig",
            "<orig>bar</orig>",
            True,
        ),
        (
            "valid-orig-with-entity-content",
            "<orig><persName ref='per123456'>bar</persName></orig>",
            True,
        ),
        (
            "valid-orig-with-xml-lang-attribute",
            "<orig xml:lang='de'>foo</orig>",
            True,
        ),
        (
            "invalid-corr-with-wrong-attribute",
            "<orig att='foo'>bar</orig>",
            False,
        ),
    ],
)
def test_orig(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("orig", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-orig",
            "<orig/>",
            False,
        ),
    ],
)
def test_orig_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
