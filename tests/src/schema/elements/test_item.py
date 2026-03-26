import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-item",
            "<item>foo</item>",
            True,
        ),
        (
            "valid-item-with-content-default",
            "<item><del>foo</del> bar</item>",
            True,
        ),
        (
            "valid-item-with-content-default-and-bibl",
            "<item><del>foo</del> bar <bibl>foo</bibl></item>",
            True,
        ),
        (
            "invalid-item-with-wrong-content",
            "<item><p>foo</p> bar</item>",
            False,
        ),
    ],
)
def test_item(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("item", name, markup, result, False)
