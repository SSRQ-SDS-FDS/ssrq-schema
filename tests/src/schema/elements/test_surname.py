import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-surname-with-text-content",
            "<surname>foo</surname>",
            True,
        ),
        (
            "invalid-surname-with-content-default",
            "<surname><del>foo</del> bar</surname>",
            False,
        ),
        (
            "invalid-surname-with-ref",
            "<surname ref='per123456'>bar</surname>",
            False,
        ),
    ],
)
def test_surname(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("surname", name, markup, result, False)
