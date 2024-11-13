import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publisher",
            "<publisher>foo</publisher>",
            True,
        ),
        (
            "valid-publisher-with-persName",
            "<publisher><persName>foo</persName></publisher>",
            True,
        ),
        (
            "valid-publisher-with-orgName",
            "<publisher><orgName>Foo und Co.</orgName></publisher>",
            True,
        ),
        (
            "invalid-publisher-with-wrong-child",
            "<publisher><p>foo</p></publisher>",
            False,
        ),
        (
            "invalid-publisher-with-mixed-content",
            "<publisher><orgName>Foo und Co.</orgName> KG</publisher>",
            False,
        ),
        (
            "valid-publisher-with-cert-low",
            "<publisher cert='low'>foo</publisher>",
            True,
        ),
        (
            "valid-publisher-with-cert-high",
            "<publisher cert='high'>foo</publisher>",
            True,
        ),
        (
            "invalid-publisher-with--wrong-cert",
            "<publisher cert='unsicher'>foo</publisher>",
            False,
        ),
    ],
)
def test_publisher(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("publisher", name, markup, result, False)
