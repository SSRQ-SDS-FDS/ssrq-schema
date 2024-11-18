import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-placeName",
            "<placeName>bar</placeName>",
            True,
        ),
        (
            "valid-placeName-with-ref",
            "<placeName ref='loc000001'>bar</placeName>",
            True,
        ),
    ],
)
def test_placeName(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("placeName", name, markup, result, False)
