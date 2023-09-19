import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-adminInfo",
            """<adminInfo>
        <custodialHist>
            <custEvent type="lost" notBefore-custom="1858-09-01" calendar="gregorian">Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.</custEvent>
        </custodialHist>
    </adminInfo>""",
            True,
        ),
        (
            "invalid-adminInfo",
            "<adminInfo/>",
            False,
        ),
    ],
)
def test_adminInfo(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("adminInfo", name, markup, result, False)
