import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-cb",
            "<cb/>",
            True,
        ),
        (
            "valid-cb-with-n-attribute",
            "<cb n='a'/>",
            True,
        ),
        (
            "invalid-cb-with-wrong-attribute-value",
            "<cb n='1'/>",
            False,
        ),
        (
            "invalid-cb-with-wrong-attribute",
            "<cb break='foo'/>",
            False,
        ),
        (
            "invalid-cb-with-content",
            "<cb>Foo</cb>",
            False,
        ),
    ],
)
def test_cb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("cb", name, markup, result, False)
