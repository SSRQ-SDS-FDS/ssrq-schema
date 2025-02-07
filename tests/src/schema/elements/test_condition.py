import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-condition-with-content",
            "<condition agent='mice'><p>Mäusefrass</p></condition>",
            True,
        ),
        (
            "valid-condition-with-multiple-p-as-content",
            "<condition agent='mice'><p>Mäusefrass</p><p>Foo</p></condition>",
            False,
        ),
        (
            "valid-condition-without-content",
            "<condition agent='mice ink_blot'/>",
            True,
        ),
        (
            "invalid-condition-without-agent",
            "<condition><p>Mäusefrass</p></condition>",
            False,
        ),
        (
            "invalid-condition-with-wrong-content",
            "<condition agent='mice'><div>Mäusefrass</div></condition>",
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
