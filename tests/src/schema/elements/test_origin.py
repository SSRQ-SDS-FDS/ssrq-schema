import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origin-with-multiple-children",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='content' when-custom='1000-01-12' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <origPlace type='content' ref='loc123456'>Wuppertal</origPlace>
                   <orgName role="issuer" ref="org123456">Kleiner Rat</orgName>
                </origin>""",
            True,
        ),
        (
            "valid-origin-with-lang",
            """<origin xml:lang='de'>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                </origin>""",
            True,
        ),
        (
            "invalid-origin-with-note",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <note>some text</note>
                </origin>""",
            False,
        ),
        (
            "invalid-origin-with-wrong-order-of-child",
            """<origin>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>""",
            False,
        ),
    ],
)
def test_origin_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origin", name, markup, result, False)
