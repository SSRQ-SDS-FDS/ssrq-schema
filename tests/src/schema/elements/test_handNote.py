import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-handNote",
            "<handNote xml:id='foo'/>",
            True,
        ),
        (
            "valid-handNote-with-n-attribute",
            "<handNote xml:id='foo' n='otherHand'/>",
            True,
        ),
        (
            "valid-handNote-with-scribe-attribute",
            "<handNote xml:id='foo' n='firstHand' scribe='per000123'/>",
            True,
        ),
        (
            "valid-handNote-with-date",
            "<handNote xml:id='foo' n='otherHand'><date from-custom='1001-01-01' to-custom='1100-12-31'/></handNote>",
            True,
        ),
        (
            "valid-handNote-with-p",
            "<handNote xml:id='foo' n='otherHand'><p>bar</p></handNote>",
            True,
        ),
        (
            "invalid-handNote-with-invalid-attribute",
            "<handNote xml:id='foo' type='bar'/>",
            False,
        ),
        (
            "invalid-handNote-with-invalid-n-attribute",
            "<handNote xml:id='foo' n='bar'/>",
            False,
        ),
        (
            "invalid-handNote-without-xml-id",
            "<handNote/>",
            False,
        ),
    ],
)
def test_handNote(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("handNote", name, markup, result, False)
