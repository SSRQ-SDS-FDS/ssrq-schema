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
            "valid-term-with-keyref",
            "<term ref='key123456'>foo</term>",
            True,
        ),
        (
            "valid-term-with-lemref",
            "<term ref='lem123456'>foo</term>",
            True,
        ),
        (
            "invalid-term-with-wrong-keyref",
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
            "invalid-term-without-attributes",
            "<term>foo</term>",
            False,
        ),
        (
            "invalid-empty-term-without-attributes",
            "<term/>",
            False,
        ),
        (
            "valid-empty-term-with-keyref-inside-keywords",
            "<keywords><term ref='key123456'/></keywords>",
            True,
        ),
        (
            "invalid-empty-term-with-lemref-inside-keywords",
            "<keywords><term ref='lem123456'/></keywords>",
            False,
        ),
        (
            "valid-empty-term-with-keyref-elsewhere-with-indextype",
            "<text><term ref='key123456' type='index'/></text>",
            True,
        ),
        (
            "invalid-empty-term-with-keyref-elsewhere-without-indextype",
            "<text><term ref='key123456'/></text>",
            False,
        ),
        (
            "invalid-empty-term-with-lemref-elsewhere",
            "<text><term ref='lem123456'/></text>",
            False,
        ),
        (
            "valid-term-without-ref-but-with-type",
            "<term type='unknown'>foo</term>",
            True,
        ),
        (
            "invalid-term-with-ref-and-with-wrong-type",
            "<term type='unknown' ref='key123456'>foo</term>",
            False,
        ),
        (
            "invalid-term-without-ref-but-with-wrong-type",
            "<term type='index'>foo</term>",
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
