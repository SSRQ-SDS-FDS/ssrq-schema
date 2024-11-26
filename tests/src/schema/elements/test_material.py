import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-material-paper",
            "<material type='paper'/>",
            True,
        ),
        (
            "valid-material-parchment",
            "<material type='parchment'/>",
            True,
        ),
        (
            "invalid-material-wrong-type",
            "<material type='stone'/>",
            False,
        ),
        (
            "invalid-material-without-type",
            "<material/>",
            False,
        ),
        (
            "invalid-material-with-content",
            "<material>Paper</material>",
            False,
        ),
    ],
)
def test_material(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("material", name, markup, result, False)
