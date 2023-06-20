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
            "valid-licence",
            "<licence target='http://licence.bar'>foo bar</licence>",
            True,
        ),
        (
            "invalid-licence",
            "<licence target='licence.bar'>foo bar</licence>",
            False,
        ),
    ],
)
def test_licence(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("licence", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-licence",
            "<licence target='http://licence.bar'/>",
            False,
        ),
    ],
)
def test_licence_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
