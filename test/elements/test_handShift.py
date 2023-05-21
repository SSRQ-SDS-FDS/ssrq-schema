from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "handShift-valid",
            "<handShift hand='secondHand'/>",
            False,
            "without matching ID",
        ),
        (
            "handShift-invalid",
            "<handShift hand='secondHand'>foo</handShift>",
            False,
            "without matching ID",
        ),
        (
            "handShift-invalid-attribute",
            "<handShift scribe='per035807'/>",
            False,
            None,
        ),
        (
            "handShift-invalid-without-attribute",
            "<handShift/>",
            False,
            None,
        ),
    ],
)
def test_handShift(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("handShift", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng(
            "handShift", name, markup, result, True
        )
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("handShift", name, markup, result, False)
