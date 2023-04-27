from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-rdg",
            "<rdg wit='#foo'>bar</rdg>",
            True,
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
