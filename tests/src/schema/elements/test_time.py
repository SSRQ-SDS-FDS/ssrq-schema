import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-time",
            "<time when-custom='08:48:00'>08:48:00</time>",
            True,
        ),
        (
            "valid-time-with-content-default",
            "<time when-custom='08:48:00'><del>foo</del> bar</time>",
            True,
        ),
        (
            "invalid-time-with-wrong-content",
            "<time when-custom='08:48:00'><p>foo</p></time>",
            False,
        ),
        (
            "valid-time-with-dur-iso",
            "<time dur-iso='PT01H'>foo</time>",
            True,
        ),
        (
            "valid-time-with-period",
            "<time period='afternoon'>foo</time>",
            True,
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
