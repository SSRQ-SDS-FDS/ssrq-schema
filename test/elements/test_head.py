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
            "valid-simple-head",
            "<head>foo</head>",
            True,
        ),
        (
            "valid-head-with-type",
            "<head type='title'>foo</head>",
            True,
        ),
        (
            "invalid-head-with-mixed-types",
            "<head type='title literature'>foo</head>",
            False,
        ),
        (
            "invalid-head-with-scribe",
            "<head scribe='baz'>foo</head>",
            False,
        ),
    ],
)
def test_head_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("head", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-head-inside-listBibl",
            "<listBibl><head type='edition'>foo</head></listBibl>",
            True,
        ),
        (
            "invalid-head-inside-listBibl-without-type",
            "<listBibl><head>foo</head></listBibl>",
            False,
        ),
        (
            "head-inside-listBibl-with-invalid-type",
            "<listBibl><head type='bar'>foo</head></listBibl>",
            False,
        ),
    ],
)
def test_head_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
