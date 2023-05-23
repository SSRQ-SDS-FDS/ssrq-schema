import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-condition-with-text-only",
            "<condition>Mäusefrass</condition>",
            True,
        ),
        (
            "valid-condition-with-p",
            "<condition><p>Mäusefrass</p></condition>",
            True,
        ),
        (
            "invalid-condition-with-div",
            "<condition><div>Mäusefrass</div></condition>",
            False,
        ),
    ],
)
def test_condition_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("condition", name, markup, result, False)
