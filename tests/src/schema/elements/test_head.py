import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-simple-head",
            "<head>foo</head>",
            True,
        ),
        (
            "valid-head-with-type",
            "<head type='title'>foo</head>",
            True,
        ),
        (
            "invalid-head-with-mixed-types",
            "<head type='title literature'>foo</head>",
            False,
        ),
        (
            "invalid-head-with-scribe",
            "<head scribe='baz'>foo</head>",
            False,
        ),
        (
            "valid-head-with-p",
            "<head><p>foo</p><p>bar</p></head>",
            True,
        ),
    ],
)
def test_head_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("head", name, markup, result, False)
