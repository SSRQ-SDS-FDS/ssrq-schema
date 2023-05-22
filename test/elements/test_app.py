from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-app",
            """<app>
                        <lem>lxxxvij</lem>
                        <rdg wit='ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e'>quadringentesimo</rdg>
                    </app>""",
            False,
            "without matching ID",
        ),
        (
            "valid-app-with-multiple-readings",
            """<app>
                                                    <lem>lxxxvij</lem>
                                                    <rdg wit="ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e">quadringentesimo</rdg>
                                                    <rdg wit="ad28656b-5c8d-459c-afb4-3e6ddf70810f">lxxxiiij</rdg>
                                                </app>""",
            False,
            "without matching ID",
        ),
        (
            "invalid-app-without-lem",
            """<app>
                                                    <rdg wit="ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e">quadringentesimo</rdg>
                                                </app>""",
            False,
            "without matching ID",
        ),
        (
            "invalid-app-without-rdg",
            "<app><lem>lxxxvij</lem></app>",
            False,
            None,
        ),
        (
            "invalid-app-wrong-sequence",
            """<app>
                                                    <rdg wit="ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e">quadringentesimo</rdg>
                                                    <lem>lxxxvij</lem>
                                                </app>""",
            False,
            "without matching ID",
        ),
        (
            "invalid-app-with-attributes",
            """<app type='foo'>
                                                    <lem>lxxxvij</lem>
                                                    <rdg wit="ad28656b-5c8d-459c-afb4-3e6ddf70810d ad28656b-5c8d-459c-afb4-3e6ddf70810e">quadringentesimo</rdg>
                                                </app>""",
            False,
            "without matching ID",
        ),
    ],
)
def test_app(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("app", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("app", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("app", name, markup, result, False)
