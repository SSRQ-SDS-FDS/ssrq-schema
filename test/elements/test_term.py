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
            "valid-simple-term",
            "<term>foo</term>",
            True,
        ),
        (
            "valid-simple-term-with-lemref",
            "<term ref='lem001301.09'>foo</term>",
            True,
        ),
        (
            "valid-simple-term-with-keyref",
            "<term ref='key003521'>foo</term>",
            True,
        ),
        (
            "simple-term-with-invalid-keyref",
            "<term ref='cey003521'>foo</term>",
            False,
        ),
        (
            "simple-term-with-invalid-lemref",
            "<term ref='lem001301.300'>foo</term>",
            False,
        ),
    ],
)
def test_term(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("term", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-simple-term-with-lemref",
            "<term ref='lem001301.09'>foo</term>",
            True,
        ),
        (
            "invalid-empty-term",
            "<term/>",
            False,
        ),
        (
            "valid-term-inside-keywords",
            "<keywords><term ref='key001301'>foo</term></keywords>",
            True,
        ),
        (
            "invalid-term-inside-keywords-with-lemref",
            "<keywords><term ref='lem001301.09'>foo</term></keywords>",
            False,
        ),
        (
            "invalid-term-inside-keywords-without-ref",
            "<keywords><term>foo</term></keywords>",
            False,
        ),
    ],
)
def test_term_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result
