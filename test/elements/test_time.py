import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "time-with-valid-when-custom",
            "<time when-custom='08:48:00'>08:48:00</time>",
            True,
        ),
        (
            "invalid-time-with-when-and-not-when-custom",
            "<time when='08:48:00'>08:48:00</time>",
            False,
        ),
        (
            "time-with-invalid-when-custom",
            "<time when-custom='98:48:00'>08:48:00</time>",
            False,
        ),
        (
            "time-with-valid-dur-iso",
            "<time dur-iso='R/PT10H'>alle zehn Stunden</time>",
            True,
        ),
        (
            "time-with-invalid-dur-iso",
            "<time dur-iso='P10H'>alle zehn Stunden</time>",
            False,
        ),
        (
            "time-with-valid-period",
            "<time period='byNight'>nachts um 12</time>",
            True,
        ),
        (
            "time-with-invalid-period",
            "<time period='atMidnight'>nachts um 12</time>",
            False,
        ),
    ],
)
def test_time_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("time", name, markup, result, False)
