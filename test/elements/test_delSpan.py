import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-delSpan",
            "<delSpan spanTo='#del1'/>",
            True,
        ),
        (
            "valid-delSpan-with-attributes",
            """<delSpan 
                                    hand='#hand17c'
                                    rend='other ink'
                                    spanTo='#del1'/>""",
            True,
        ),
        # ToDo: Dieser Test wird nicht korrekt ausgewertet, wie kann ich Prüfung auf IDs als Attributwert erzwingen?
        # vgl. test_addSpan
        # (
        #    "delSpan-with-invalid-attribute-values",
        #    "<delSpan hand='foo' spanTo='del1'/>",
        #    False,
        # ),
        (
            "invalid-delSpan",
            "<delSpan spanTo='#del1'>foo</delSpan>",
            False,
        ),
    ],
)
def test_delSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("delSpan", name, markup, result, False)
