import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-seg-with-text",
            "<seg>foo</seg>",
            True,
        ),
        (
            "valid-seg-with-text-and-n",
            "<seg n='1'>foo</seg>",
            True,
        ),
        (
            "valid-seg-with-mixed-content",
            "<seg><lb/>Und sonderlich sol soͤlich unser gebott</seg>",
            True,
        ),
        (
            "seg-with-invalid-child",
            "<seg n='1'><text>foo</text></seg>",
            False,
        ),
        (
            "invalid-seg-with-cert",
            "<seg cert='PS'>foo</seg>",
            False,
        ),
    ],
)
def test_seg(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("seg", name, markup, result, False)
