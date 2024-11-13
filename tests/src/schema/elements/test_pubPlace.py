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
            "invalid-pubPlace-without-ref",
            "<pubPlace>foo</pubPlace>",
            False,
        ),
        (
            "valid-pubPlace-with-cert",
            "<pubPlace cert='low' ref='loc123456'>foo-low</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace",
            "<pubPlace ref='loc123456'><p/></pubPlace>",
            False,
        ),
        (
            "invalid-pubPlace-with-attributes",
            "<pubPlace ref='loc123456' type='foobar'>foo</pubPlace>",
            False,
        ),
        (
            "invalid-pubPlace-with-invalid-cert",
            "<pubPlace cert='mid' ref='loc123456'>foo-mid</pubPlace>",
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
