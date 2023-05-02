import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-addSpan",
            "<addSpan spanTo='#add1'/>",
            True,
        ),
        (
            "valid-addSpan-with-attributes",
            """<addSpan 
                            hand='#otherHand'
                            place='below'
                            rend='other ink'
                            spanTo='#add1'
                            type='sign'/>""",
            True,
        ),
        # ToDo: Dieser Test wird nicht korrekt ausgewertet, wie kann ich Prüfung auf IDs als Attributwert erzwingen?
        # vgl. test_delSpan
        # (
        #    "addSpan-with-invalid-attribute-values",
        #    "<addSpan hand='foo' spanTo='add1'/>",
        #    False,
        # ),
        (
            "invalid-addSpan",
            "<addSpan spanTo='#add1'>foo</addSpan>",
            False,
        ),
    ],
)
def test_addSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("addSpan", name, markup, result, False)
