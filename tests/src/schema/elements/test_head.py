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
            "valid-head-with-content-default",
            "<head><del>foo</del>bar</head>",
            True,
        ),
        (
            "valid-head-with-p",
            "<head><p>foo</p><p>bar</p></head>",
            True,
        ),
        (
            "valid-head-with-bibl",
            "<head><bibl>foo</bibl></head>",
            True,
        ),
        (
            "valid-head-with-seg",
            "<head><seg>foo</seg><seg>bar</seg></head>",
            True,
        ),
        (
            "invalid-head-with-just-one-seg",
            "<head><seg>foo</seg></head>",
            False,
        ),
        (
            "valid-head-with-type",
            "<head type='title'>foo</head>",
            True,
        ),
        (
            "valid-head-with-place",
            "<head place='above'>foo</head>",
            True,
        ),
        (
            "valid-head-with-resp",
            "<head resp='CS'>foo</head>",
            True,
        ),
        (
            "valid-head-with-n",
            "<head n='1'>foo</head>",
            True,
        ),
        (
            "valid-head-with-xml-lang",
            "<head xml:lang='de'>foo</head>",
            True,
        ),
        (
            "valid-head-with-hand",
            "<head hand='otherHand'>foo</head>",
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
