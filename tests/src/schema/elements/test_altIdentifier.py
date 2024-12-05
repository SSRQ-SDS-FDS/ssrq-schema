import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-altIdentifier",
            "<altIdentifier><idno>Foo</idno></altIdentifier>",
            True,
        ),
        (
            "invalid-altIdentifier-with-wrong-content",
            "<altIdentifier>abc</altIdentifier>",
            False,
        ),
    ],
)
def test_alt_identifier(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("altIdentifier", name, markup, result, False)
