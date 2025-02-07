import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-author",
            "<author>Foo</author>",
            True,
        ),
        (
            "valid-author-with-cert",
            "<author cert='high'>Foo</author>",
            True,
        ),
        (
            "valid-author-with-role",
            "<author role='scribe'>Foo</author>",
            True,
        ),
        (
            "invalid-author-with-resp",
            "<author resp='CS'>Foo</author>",
            False,
        ),
        (
            "valid-author-with-persName",
            "<author><persName ref='per002336'>Adam Böniger</persName></author>",
            True,
        ),
        (
            "valid-author-with-multiple-persName",
            """
            <author role='scribe'>
                <persName ref='per002336'>Adam Böniger</persName>
                <persName>Hans Müller</persName>
            </author>""",
            True,
        ),
        (
            "valid-author-with-orgName",
            "<author><orgName ref='org123456'>Staatskanzlei Zürich</orgName></author>",
            True,
        ),
        (
            "valid-author-with-multiple-orgNames",
            """
            <author>
                <orgName ref='org123456'>Staatskanzlei Zürich</orgName>
                <orgName ref='org123457'>Staatskanzlei Adlikon</orgName>
            </author>""",
            True,
        ),
        (
            "invalid-author-with-persName-and-orgName",
            """
            <author role='scribe'>
                <persName ref='per002336'>Adam Böniger</persName>
                <orgName>Staatskanzlei</orgName>
            </author>""",
            False,
        ),
        (
            "invalid-author-with-wrong-role",
            """
            <author role='scriptor'>
                <persName ref='per002336'>Adam Böniger</persName>, Landschreiber von Glarus
            </author>""",
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
