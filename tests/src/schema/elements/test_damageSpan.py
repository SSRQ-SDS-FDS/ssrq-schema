import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-damageSpan",
            "<p><damageSpan agent='clipping' spanTo='damage1'/><anchor xml:id='damage1'/></p>",
            True,
        ),
        (
            "invalid-damageSpan-without-agent",
            "<p><damageSpan spanTo='damage1'/><anchor xml:id='damage1'/></p>",
            False,
        ),
        (
            "invalid-damageSpan-without anchor",
            "<p><damageSpan agent='clipping' spanTo='damage1'/></p>",
            False,
        ),
        (
            "invalid-damageSpan-with-content",
            """
            <p>
                <damageSpan agent='clipping' spanTo='damage1'>Foo</damageSpan>
                <anchor xml:id='damage1'/>
            </p>""",
            False,
        ),
    ],
)
def test_damage_span(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("p", name, markup, result, False)
    # In this test, the surrounding p element is the root for the test, because damageSpan always
    # needs a corresponding element with a xml:id to be valid. If damageSpan was the root, all
    # rng-tests would fail.
