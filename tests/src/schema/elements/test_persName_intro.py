import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-persName-with-text-content",
            "<persName>foo</persName>",
            True,
        ),
        (
            "invalid-persName-with-content-default",
            "<persName><del>foo</del> bar</persName>",
            False,
        ),
        (
            "invalid-persName-with-ref",
            "<persName ref='per123456'>bar</persName>",
            False,
        ),
        (
            "invalid-persName-with-role",
            "<persName role='witness'>bar</persName>",
            False,
        ),
    ],
)
def test_pers_name(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("persName", name, markup, result, False)
