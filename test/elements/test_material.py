import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-material",
            "<material type='paper'/>",
            True,
        ),
        (
            "invalid-material-wihout-type",
            "<material>Paper</material>",
            False,
        ),
        (
            "material-with-invalid-type",
            "<material type='stone'/>",
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
