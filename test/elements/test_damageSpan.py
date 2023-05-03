import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-damageSpan",
            "<damageSpan agent='clipping' spanTo='#dmg1'/>",
            True,
        ),
        (
            "valid-damageSpan-with-attributes",
            """<damageSpan 
                                                            agent='clipping'
                                                            spanTo='#dmg1'/>""",
            True,
        ),
        (
            "damageSpan-with-invalid-attribute-values",
            "<damageSpan agent='foo' spanTo='#dmg1'/>",
            False,
        ),
        (
            "invalid-damageSpan",
            "<damageSpan agent='clipping' spanTo='#dmg1'>foo</damageSpan>",
            False,
        ),
        (
            "damageSpan-with-wrong-attribute",
            "<damageSpan agent='clipping' spanTo='#dmg1' type='bar'/>",
            False,
        ),
    ],
)
def test_damageSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("damageSpan", name, markup, result, False)
