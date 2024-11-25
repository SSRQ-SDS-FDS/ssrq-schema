import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-history",
            """
            <history>
                <origin>
                    <origDate type='document' when-custom="1366-06-29" calendar="gregorian"/>
                    <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
               </origin>
            </history>
            """,
            True,
        ),
    ],
)
def test_history(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("history", name, markup, result, False)
