import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-foreign",
            "<foreign xml:lang='la'>foo</foreign>",
            True,
        ),
        (
            "invalid-foreign-without-lang",
            "<foreign>foo</foreign>",
            False,
        ),
        (
            "invalid-foreign-with-content-default",
            "<foreign xml:lang='la'><del>foo</del></foreign>",
            False,
        ),
    ],
)
def test_foreign(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("foreign", name, markup, result, False)
