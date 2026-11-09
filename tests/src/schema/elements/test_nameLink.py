import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-nameLink-with-text-content",
            "<nameLink>foo</nameLink>",
            True,
        ),
        (
            "invalid-nameLink-with-content-default",
            "<nameLink><del>foo</del> bar</nameLink>",
            False,
        ),
        (
            "invalid-nameLink-with-ref",
            "<nameLink ref='per123456'>bar</nameLink>",
            False,
        ),
    ],
)
def test_name_link(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("nameLink", name, markup, result, False)
