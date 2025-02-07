import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-placeName",
            "<placeName>foo</placeName>",
            True,
        ),
        (
            "valid-placeName-with-content-default",
            "<placeName><del>foo</del> bar</placeName>",
            True,
        ),
        (
            "invalid-placeName-with-wrong-content",
            "<placeName><p>foo</p></placeName>",
            False,
        ),
        (
            "valid-placeName-with-ref",
            "<placeName ref='loc000001'>foo</placeName>",
            True,
        ),
    ],
)
def test_place_name(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("placeName", name, markup, result, False)
