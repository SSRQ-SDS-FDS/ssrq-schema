import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-persName",
            "<persName ref='per123456'>bar</persName>",
            True,
        ),
        (
            "valid-persName-with-role",
            "<persName ref='per000001' role='witness'>bar</persName>",
            True,
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
