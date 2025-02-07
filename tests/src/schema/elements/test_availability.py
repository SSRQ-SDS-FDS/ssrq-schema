import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-availability",
            """
            <availability>
                <licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                    Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                </licence>
            </availability>""",
            True,
        ),
        (
            "invalid-availability-with-status-attribute",
            """
            <availability status='foo'>
                <licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                    Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                </licence>
            </availability>""",
            False,
        ),
        (
            "invalid-availability-with-wrong-content",
            "<availability><p xml:id='facs'>bar</p></availability>",
            False,
        ),
    ],
)
def test_availability_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("availability", name, markup, result, False)
