import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-text",
            """
            <text>
                <body>
                    <div>
                        <p>foo</p>
                    </div>
                </body>
            </text>
            """,
            True,
        ),
        (
            "invalid-text-with-back",
            """
            <text>
                <body>
                    <div>
                        <p>foo</p>
                    </div>
                </body>
                <back>
                    <div>
                        <p>foo</p>
                    </div>
                </back>
            </text>
            """,
            False,
        ),
        (
            "invalid-text-with-type",
            "<text type='summary'><body><div><p>foo</p></div></body></text>",
            False,
        ),
    ],
)
def test_text(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("text", name, markup, result, False)
