import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-altIdentifier",
            "<altIdentifier><idno>LAGL I. 9h.</idno></altIdentifier>",
            True,
        ),
        (
            "invalid-altIdentifier-with-attributes",
            "<altIdentifier type='foo'><idno>LAGL I. 9h.</idno></altIdentifier>",
            False,
        ),
        (
            "invalid-altIdentifier-without-idno",
            "<altIdentifier>abc</altIdentifier>",
            False,
        ),
    ],
)
def test_altIdentifier(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("altIdentifier", name, markup, result, False)
