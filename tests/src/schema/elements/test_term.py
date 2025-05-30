import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

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
            "valid-term-with-type",
            "<term type='unknown'>foo</term>",
            True,
        ),
        (
            "valid-term-with-content-default",
            "<term ref='lem123456'><del>foo</del> bar</term>",
            True,
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
            "invalid-term-without-any-information",
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
            "valid-empty-term-with-keyref-of-type-index",
            "<term ref='key123456' type='index'/>",
            True,
        ),
        (
            "invalid-empty-term-with-keyref-not-of-type-index",
            "<term ref='key123456'/>",
            False,
        ),
        (
            "invalid-empty-term-with-lemref-elsewhere",
            "<term ref='lem123456'/>",
            False,
        ),
        (
            "invalid-term-with-ref-and-wrong-type",
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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
