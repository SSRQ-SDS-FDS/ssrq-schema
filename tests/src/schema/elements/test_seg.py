import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-seg",
            "<seg>foo</seg>",
            True,
        ),
        (
            "valid-seg-with-n",
            "<seg n='1'>foo</seg>",
            True,
        ),
        (
            "invalid-seg-with-resp",
            "<seg resp='PS'>foo</seg>",
            False,
        ),
        (
            "valid-seg-with-content-default",
            "<seg><lb/>foo</seg>",
            True,
        ),
        (
            "valid-seg-with-other-content",
            """
            <seg>
                <add place='left_top'>baz</add>
                <cb/>
                <head>foo</head>
                <list><item>foo</item></list>
                <p>foo</p>
                <pb/>
                <table><row><cell>foo</cell></row></table>
            </seg>
            """,
            True,
        ),
        (
            "seg-with-wrong-content",
            "<seg><div>foo</div></seg>",
            False,
        ),
        (
            "valid-seg-with-two-segs",
            "<seg><seg>foo</seg><seg>bar</seg></seg>",
            True,
        ),
        (
            "invalid-seg-with-one-seg",
            "<seg><seg>foo</seg></seg>",
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
