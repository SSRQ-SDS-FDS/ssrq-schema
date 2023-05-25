from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-del",
            "<del>bar</del>",
            True,
            None,
        ),
        (
            "valid-del-with-attributes",
            "<del rend='crossout' hand='otherHand'>bar</del>",
            False,
            "without matching ID",
        ),
        (
            "invalid-del-with-wrong-rend",
            "<del rend='foo'>bar</del>",
            False,
            None,
        ),
        (
            "invalid-del-with-wrong-attributes",
            "<del att='foo'>bar</del>",
            False,
            None,
        ),
    ],
)
def test_del(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("del", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("del", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("del", name, markup, result, False)
