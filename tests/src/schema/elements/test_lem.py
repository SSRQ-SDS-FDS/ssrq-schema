import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-lem",
            "<lem>bar</lem>",
            True,
        ),
        (
            "valid-lem-with-content-default",
            "<lem>foo <del>bar</del></lem>",
            True,
        ),
        (
            "valid-lem-with-seg",
            "<lem><seg>foo</seg><seg>bar</seg></lem>",
            True,
        ),
        (
            "invalid-lem-with-seg-and-mixed-content",
            "<lem><seg>foo</seg> bar</lem>",
            False,
        ),
        (
            "invalid-lem-with-just-one-seg",
            "<lem><seg>foo</seg></lem>",
            False,
        ),
    ],
)
def test_lem(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("lem", name, markup, result, False)
