import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origin",
            " <origin><origDate when-custom='1366-06-29' calendar='gregorian'/><origPlace>Rheineck</origPlace></origin>",
            True,
        ),
        (
            "valid-origin-with-lang",
            " <origin xml:lang='de'><origDate when-custom='1366-06-29' calendar='gregorian'/><origPlace>Rheineck</origPlace></origin>",
            True,
        ),
        (
            "invalid-origin-with-note",
            " <origin><origDate when-custom='1366-06-29' calendar='gregorian'/><origPlace>Rheineck</origPlace><note>some text</note></origin>",
            False,
        ),
        (
            "invalid-origin-with-wrong-order-of-child",
            " <origin><origPlace>Rheineck</origPlace><origDate when-custom='1366-06-29' calendar='gregorian'/></origin>",
            False,
        ),
    ],
)
def test_origin_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origin", name, markup, result, False)
