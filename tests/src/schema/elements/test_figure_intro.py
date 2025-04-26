import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-figure",
            """
            <figure>
                <graphic type='map' mimeType='image/svg' url='foo.svg'/>
                <head>Foo</head>
            </figure>
            """,
            True,
        ),
        (
            "invalid-figure-with-type",
            """
            <figure type="illustration">
                <graphic type='map' mimeType='image/svg' url='foo.svg'/>
                <head>Foo</head>
            </figure>
            """,
            False,
        ),
        (
            "invalid-figure-without-head",
            """
            <figure>
                <graphic type='map' mimeType='image/svg' url='foo.svg'/>
            </figure>
            """,
            False,
        ),
        (
            "invalid-figure-without-graphic",
            """
            <figure>
                <head>Foo</head>
            </figure>
            """,
            False,
        ),
    ],
)
def test_figure(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("figure", name, markup, result, False)