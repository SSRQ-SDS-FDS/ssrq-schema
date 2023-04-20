from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-persName",
            "<persName ref='per000001'>bar</persName>",
            True,
        ),
        (
            "valid-persName-with-role",
            "<persName ref='per000001' role='witness'>bar</persName>",
            True,
        ),
        (
            "persName-with-invalid-ref",
            "<persName ref='abcdefg' role='recipient'>bar</persName>",
            False,
        ),
        (
            "persName-with-invalid-role",
            "<persName ref='org000001' role='testis'>bar</persName>",
            False,
        ),
    ],
)
def test_persName(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("persName", name, markup, result, False)
