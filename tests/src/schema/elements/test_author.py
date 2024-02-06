import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-author-with-persName",
            "<author role='scribe'><persName ref='per002336'>Adam Böniger</persName></author>",
            True,
        ),
        (
            "valid-author-with-multiple-persName",
            "<author role='scribe'><persName ref='per002336'>Adam Böniger</persName> <persName>Hans Müller</persName></author>",
            True,
        ),
        (
            "invalid-author-with-persName-orgName",
            "<author role='scribe'><persName ref='per002336'>Adam Böniger</persName> <orgName>Staatskanzlei</orgName></author>",
            False,
        ),
        (
            "invalid-author-with-key",
            "<author role='scribe' key='bar'><persName ref='per002336'>Adam Böniger</persName></author>",
            False,
        ),
        (
            "author-with-invalid-role",
            "<author role='scriptor'><persName ref='per002336'>Adam Böniger</persName>, Landschreiber von Glarus</author>",
            False,
        ),
    ],
)
def test_author(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("author", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-author-with-persName",
            "<author role='scribe'><persName ref='per002336'>Adam Böniger</persName>, Landschreiber von Glarus</author>",
            True,
        ),
        (
            "invalid-author-without-content",
            "<author role='scribe'/>",
            False,
        ),
    ],
)
def test_author_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result
