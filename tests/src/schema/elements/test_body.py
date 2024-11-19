import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-body-with-div",
            "<body><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-ab",
            "<body><ab type='dorsal' place='verso'>foo</ab><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb",
            "<body><pb n='1' facs='abcde_1'/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-gap",
            "<body><gap/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-multiple-elements",
            """
            <body>
                <pb n="1"/>
                <div><p>bar</p></div>
                <gap/>
                <div><p>bar</p></div>
                <ab type='dorsal' place='verso'>foo</ab>
            </body>
            """,
            True,
        ),
        (
            "invalid-body-with-text-content",
            "<body>foo</body>",
            False,
        ),
        (
            "invalid-body-with-default-content",
            "<body><p>foo</p></body>",
            False,
        ),
    ],
)
def test_body(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("body", name, markup, result, False)
