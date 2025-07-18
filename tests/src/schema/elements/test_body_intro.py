import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-body-with-one-div",
            """
            <body>
                <div type="chapter">
                    <head>Foo</head>
                    <p>Foo</p>
                </div>
            </body>
            """,
            True,
        ),
        (
            "valid-body-with-multiple-divs",
            """
             <body>
                <div type="chapter">
                    <head>Foo</head>
                    <p>Foo</p>
                </div>
                <div type="chapter">
                    <head>Foo</head>
                    <p>Foo</p>
                </div>
             </body>
             """,
            True,
        ),
        (
            "invalid-body-with-other-content",
            """
             <body>
                <div type="chapter">
                    <head>Foo</head>
                    <p>Foo</p>
                </div>
                <pb n="1r"/>
             </body>
             """,
            False,
        ),
    ],
)
def test_body(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("body", name, markup, result, False)
