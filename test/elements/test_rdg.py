from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-rdg",
            "<rdg wit='ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e'>bar</rdg>",
            False,
            "without matching ID",
        ),
        (
            "rdg-with-invalid-xml-id",
            "<rdg wit='ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810f'>bar</rdg>",
            False,
            "without matching ID",
        ),
        (
            "invalid-rdg-wit-false-attribute",
            "<rdg type='foo' wit='ad28656b-5c8d-459c-afb4-3e6ddf70810d'>bar</rdg>",
            False,
            "without matching ID",
        ),
        (
            "invalid-rdg-without-attribute",
            "<rdg>foo</rdg>",
            False,
            None,
        ),
    ],
)
def test_rdg(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("rdg", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("rdg", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("rdg", name, markup, result, False)
