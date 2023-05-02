from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listWit",
            "<listWit><witness xml:id='ad28656b-5c8d-459c-afb4-3e6ddf70810d' n='A'>Foo</witness></listWit>",
            True,
        ),
        (
            "valid-listWit-with-multiple-entries",
            """<listWit><witness xml:id='ad28656b-5c8d-459c-afb4-3e6ddf70810d' n='A'>Foo</witness>
                    <witness xml:id='ad28656b-5c8d-459c-afb4-3e6ddf70810e' n='B'>Bar</witness></listWit>""",
            True,
        ),
        (
            "invalid-empty-listWit",
            "<listWit></listWit>",
            False,
        ),
        (
            "invalid-listWit-with-attribute",
            "<listWit type='foo'><witness xml:id='ad28656b-5c8d-459c-afb4-3e6ddf70810d' n='A'>Foo</witness></listWit>",
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
