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
                                hand='secondaryHand'
                                place='below'
                                rend='other ink'
                                scribe='per000001'
                                spanTo='#add1'
                                type='sign'/>""",
            True,
        ),
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
