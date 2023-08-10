import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-back",
            "<back><div><p>foo</p></div></back>",
            True,
        ),
        (
            "valid-back-with-multiple-divs",
            "<back><div><p>foo</p></div><div><p>foo</p></div></back>",
            True,
        ),
        (
            "invalid-back-with-p-only",
            "<back><p>foo</p></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back xml:id='bar123'><div><p>foo</p></div></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back rend='bar'><div><p>foo</p></div></back>",
            False,
        ),
    ],
)
def test_back(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("back", name, markup, result, False)
