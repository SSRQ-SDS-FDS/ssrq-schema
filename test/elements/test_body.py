from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-empty-body",
            "<body xmlns='http://www.tei-c.org/ns/1.0'/>",
            True,
        ),
        (
            "valid-body-with-div",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><pb n='1' facs='abcde'/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb-div-signed",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><pb n='1' facs='abcde'/><div><p>bar</p></div><signed><lb/>Rechenschriber</signed></body>",
            True,
        ),
        (
            "invalid-body-with-text-only",
            "<body xmlns='http://www.tei-c.org/ns/1.0'>foo</body>",
            False,
        ),
        (
            "invalid-body-with-p-as-child",
            "<body xmlns='http://www.tei-c.org/ns/1.0'><p>foo</p></body>",
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
