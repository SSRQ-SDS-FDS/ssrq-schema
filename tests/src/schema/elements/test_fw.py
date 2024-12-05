import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-fw",
            "<fw type='catchword'>foo</fw>",
            True,
        ),
        (
            "valid-fw-with-content-default",
            "<fw type='catchword'><del>foo</del></fw>",
            True,
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
