import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handDesc",
            """
            <handDesc>
                <handNote xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>
            </handDesc>
            """,
            True,
        ),
        (
            "valid-handDesc-with multiple-handNotes",
            """
            <handDesc>
                <handNote xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>
                <handNote xml:id='otherHand'/>
            </handDesc>
            """,
            True,
        ),
        (
            "invalid-handDesc-with-hands",
            "<handDesc hands='10'><handNote xml:id='otherHand'/></handDesc>",
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
