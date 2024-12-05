import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-custodialHist",
            """
            <custodialHist>
                <custEvent type="lost" notBefore-custom="1858-09-01" calendar="gregorian">
                    Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
                </custEvent>
            </custodialHist>
            """,
            True,
        ),
        (
            "invalid-custodialHist-with-default-content",
            "<custodialHist><p>foo</p></custodialHist>",
            False,
        ),
    ],
)
def test_custodial_hist(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("custodialHist", name, markup, result, False)
