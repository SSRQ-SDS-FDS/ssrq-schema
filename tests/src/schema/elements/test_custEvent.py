import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-custEvent",
            """
            <custEvent type="lost" notBefore-custom="1858-09-01" calendar="gregorian">
                Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
            </custEvent>
            """,
            True,
        ),
        (
            "invalid-custEvent-with-period",
            """
            <custEvent type="lost" period="winter" calendar="gregorian">
                Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
            </custEvent>
            """,
            False,
        ),
        (
            "invalid-custEvent-type",
            """
            <custEvent type="found_again" notBefore-custom="1858-09-01" calendar="gregorian">
                Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
            </custEvent>
            """,
            False,
        ),
        (
            "invalid-custEvent-without-type",
            """
            <custEvent notBefore-custom="1858-09-01" calendar="gregorian">
                Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
            </custEvent>
            """,
            False,
        ),
    ],
)
def test_cust_event(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("custEvent", name, markup, result, False)
