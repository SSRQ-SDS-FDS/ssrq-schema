from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handDesc",
            "<handDesc><handNote xml:id='foo'/></handDesc>",
            True,
        ),
        (
            "valid-handDesc-with multiple-handNotes",
            "<handDesc><handNote xml:id='foo'/><handNote xml:id='bar'/></handDesc>",
            True,
        ),
        (
            "invalid-handDesc-with-hands",
            "<handDesc hands='10'><handNote xml:id='foo'/></handDesc>",
            False,
        ),
        (
            "invalid-handDesc",
            "<handDesc><p>Foo</p></handDesc>",
            False,
        ),
        (
            "invalid-empty-handDesc",
            "<handDesc/>",
            False,
        ),
    ],
)
def test_handDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handDesc", name, markup, result, False)
