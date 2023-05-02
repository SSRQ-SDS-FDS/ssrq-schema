from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-rdg",
            "<rdg wit='#ad28656b-5c8d-459c-afb4-3e6ddf70810d #ad28656b-5c8d-459c-afb4-3e6ddf70810e'>bar</rdg>",
            True,
        ),
        (
            "rdg-with-invalid-xml-id",
            "<rdg wit='#bar #ad28656b-5c8d-459c-afb4-3e6ddf70810e'>bar</rdg>",
            False,
        ),
        (
            "invalid-rdg-wit-false-attribute",
            "<rdg type='foo'>bar</rdg>",
            False,
        ),
        (
            "invalid-rdg-without-attribute",
            "<rdg>foo</rdg>",
            False,
        ),
    ],
)
def test_rdg(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("rdg", name, markup, result, False)
