import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-list",
            "<list xmlns='http://www.tei-c.org/ns/1.0'><item>foo</item></list>",
            True,
        ),
        (
            "invalid-list",
            "<list xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
    ],
)
def test_list(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("list", name, markup, result, False)
