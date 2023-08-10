import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-row",
            "<row><cell>foo</cell></row>",
            True,
        ),
        (
            "invalid-row-content",
            "<row><measureGrp><cell>foo</cell></measureGrp></row>",
            False,
        ),
        (
            "invalid-row-with-attribute",
            "<row type='foo'><cell>foo</cell></row>",
            False,
        ),
    ],
)
def test_row(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("row", name, markup, result, False)
