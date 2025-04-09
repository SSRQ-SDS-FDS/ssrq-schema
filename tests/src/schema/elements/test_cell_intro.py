import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-cell",
            "<cell>foo</cell>",
            True,
        ),
        (
            "valid-cell-with-role",
            "<cell role='label'>foo</cell>",
            True,
        ),
        (
            "valid-cell-with-rend",
            "<cell rend='align-bottom'>foo</cell>",
            True,
        ),
        (
            "valid-cell-with-bibl",
            "<cell><bibl><ref>Name 2000</ref>, p. 120</bibl></cell>",
            True,
        ),
        (
            "invalid-cell-with-wrong-attribute",
            "<cell xml:id='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell-with-wrong-role",
            "<cell role='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell-with-wrong-rend",
            '<cell rend="bar">foo</cell>',
            False,
        ),
        (
            "invalid-cell-with-wrong-content",
            '<cell rend="bar"><div><p>foo</p></div></cell>',
            False,
        ),
    ],
)
def test_cell(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("cell", name, markup, result, False)
