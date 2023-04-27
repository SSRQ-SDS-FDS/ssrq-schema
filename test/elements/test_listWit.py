from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listWit",
            "<listWit><witness>Foo</witness></listWit>",
            True,
        ),
        (
            "valid-listWit-with-multiple-entries",
            "<listWit><witness xml:id='bar'>Foo</witness><witness xml:id='foo'>Bar</witness></listWit>",
            True,
        ),
        (
            "invalid-empty-listWit",
            "<listWit></listWit>",
            False,
        ),
        (
            "invalid-listWit-with-attribute",
            "<listWit type='foo'><witness xml:id='bar'>Foo</witness></listWit>",
            False,
        ),
    ],
)
def test_listWit(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("listWit", name, markup, result, False)
