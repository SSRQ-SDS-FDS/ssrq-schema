import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-textClass",
            "<textClass><keywords><term ref='key000192'/></keywords></textClass>",
            True,
        ),
        (
            "invalid-textClass-with-multiple-keywords",
            """
            <textClass>
                <keywords><term ref='key000192'/></keywords>
                <keywords><term ref='key000192'/></keywords>
            </textClass>
            """,
            False,
        ),
    ],
)
def test_text_class_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("textClass", name, markup, result, False)
