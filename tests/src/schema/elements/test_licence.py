import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-licence",
            """
            <licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
            </licence>
            """,
            True,
        ),
        (
            "licence-with-invalid-text",
            """
            <licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                Attribution-NonCommercial-ShareAlike 4.0 International
            </licence>
            """,
            False,
        ),
        (
            "invalid-licence-without-target",
            """
            <licence>
                Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
            </licence>
            """,
            False,
        ),
        (
            "invalid-licence-with-wrong-target",
            """
            <licence target="foo">
                Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
            </licence>
            """,
            False,
        ),
    ],
)
def test_licence(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("licence", name, markup, result, False)
