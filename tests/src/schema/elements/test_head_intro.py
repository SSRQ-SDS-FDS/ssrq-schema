import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-head",
            "<head>foo</head>",
            True,
        ),
        (
            "valid-head-with-pc",
            "<head>foo<pc>;</pc> bar</head>",
            True,
        ),
        (
            "invalid-head-with-content-default",
            "<head><del>foo</del>bar</head>",
            False,
        ),
        (
            "invalid-head-with-attribute",
            "<head type='title'>foo</head>",
            False,
        ),
    ],
)
def test_head_rng(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("head", name, markup, result, False)
