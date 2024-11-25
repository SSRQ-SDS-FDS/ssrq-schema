import pytest

from ..conftest import RNG_test_function


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
    ],
)
def test_hand_desc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handDesc", name, markup, result, False)
