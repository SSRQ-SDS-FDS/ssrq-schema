from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-app",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit="#B">quadringentesimo</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-with-multiple-readings",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit="#B">quadringentesimo</rdg>
                    <rdg wit="#c">lxxxiiij</rdg>
                </app>""",
            True,
        ),
        (
            "invalid-app-without-lem",
            """<app>
                    <rdg wit="#B">quadringentesimo</rdg>
                </app>""",
            False,
        ),
        (
            "invalid-app-without-rdg",
            """<app>
                    <lem>lxxxvij</lem>
                </app>""",
            False,
        ),
        (
            "invalid-app-wrong-sequence",
            """<app>
                    <rdg wit="#B">quadringentesimo</rdg>
                    <lem>lxxxvij</lem>
                </app>""",
            False,
        ),
        (
            "invalid-app-with-attributes",
            """<app type='foo'>
                    <lem>lxxxvij</lem>
                    <rdg wit="#B">quadringentesimo</rdg>
                </app>""",
            False,
        ),
    ],
)
def test_app(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("app", name, markup, result, False)
