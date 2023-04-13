from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publisher",
            "<publisher xmlns='http://www.tei-c.org/ns/1.0'>foo</publisher>",
            True,
        ),
        (
            "invalid-publisher",
            "<publisher xmlns='http://www.tei-c.org/ns/1.0'><p>foo</p></publisher>",
            False,
        ),
        (
            "valid-publisher-with-cert-low",
            "<publisher xmlns='http://www.tei-c.org/ns/1.0' cert='low'>foo</publisher>",
            True,
        ),
        (
            "valid-publisher-with-cert-high",
            "<publisher xmlns='http://www.tei-c.org/ns/1.0' cert='high'>foo</publisher>",
            True,
        ),
        (
            "invalid-publisher-with-cert",
            "<publisher xmlns='http://www.tei-c.org/ns/1.0' cert='unsicher'>foo</publisher>",
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
