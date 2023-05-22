from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-fw",
            "<fw type='catchword'>foo</fw>",
            True,
        ),
        (
            "invalid-fw-with-wrong-type",
            "<fw type='bar'>foo</fw>",
            False,
        ),
        (
            "invalid-fw-without type",
            "<fw>foo</fw>",
            False,
        ),
    ],
)
def test_fw(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("fw", name, markup, result, False)
