import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-delSpan",
            "<delSpan spanTo='del1'/>",
            False,
            "without matching ID",
        ),
        (
            "valid-delSpan-with-attributes",
            "<delSpan rend='crossout' hand='hand17c' spanTo='del1'/>",
            False,
            "without matching ID",
        ),
        (
            "invalid-delSpan",
            "<delSpan spanTo='del1'>foo</delSpan>",
            False,
            None,
        ),
    ],
)
def test_delSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("delSpan", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("delSpan", name, markup, result, True)
        assert validation_result is not None
        reports = [err.message for info in validation_result for err in info.report]
        messages = "".join(reports)
        assert message in messages
    else:
        test_element_with_rng("delSpan", name, markup, result, False)
