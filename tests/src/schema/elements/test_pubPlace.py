import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pubPlace",
            "<pubPlace>foo</pubPlace>",
            True,
        ),
        (
            "valid-pubPlace-with-cert",
            "<pubPlace cert='low'>foo-low</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace",
            "<pubPlace><p/></pubPlace>",
            False,
        ),
        (
            "invalid-text-with-attributes",
            "<pubPlace type='foobar'>foo</pubPlace>",
            False,
        ),
        (
            "valid-pubPlace-with-invalid-cert",
            "<pubPlace cert='mid'>foo-mid</pubPlace>",
            False,
        ),
    ],
)
def test_pubPlace(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pubPlace", name, markup, result, False)
