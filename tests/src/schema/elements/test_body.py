import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-body",
            "<body/>",
            False,
        ),
        (
            "valid-body-with-div",
            "<body><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div",
            "<body><pb n='1' facs='abcde_1'/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div-signed",
            "<body><pb n='1' facs='abcde_1'/><div><p>bar</p></div><signed><lb/>Rechenschriber</signed></body>",
            True,
        ),
        (
            "invalid-body-with-text-only",
            "<body>foo</body>",
            False,
        ),
        (
            "invalid-body-with-p-as-child",
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
