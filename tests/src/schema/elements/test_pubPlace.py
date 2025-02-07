import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pubPlace",
            "<pubPlace ref='loc123456'>locus amoenus</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace-with-wrong-content",
            "<pubPlace ref='loc123456'><p>foo</p></pubPlace>",
            False,
        ),
        (
            "invalid-pubPlace-without-ref",
            "<pubPlace>foo</pubPlace>",
            False,
        ),
        (
            "valid-pubPlace-with-cert",
            "<pubPlace cert='low' ref='loc123456'>foo-low</pubPlace>",
            True,
        ),
    ],
)
def test_pub_place(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pubPlace", name, markup, result, False)
