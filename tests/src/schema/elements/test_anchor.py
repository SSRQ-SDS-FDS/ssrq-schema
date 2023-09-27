import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-anchor-for-del", "<anchor xml:id='del1'/>", True),
        (
            "valid-anchor-for-add",
            "<anchor xml:id='add1'/>",
            True,
        ),
        (
            "invalid-anchor-without-id",
            "<anchor/>",
            False,
        ),
        (
            "invalid-anchor-with-resp",
            "<anchor xml:id='del1' resp='foo'/>",
            False,
        ),
    ],
)
def test_anchor(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("anchor", name, markup, result, False)
