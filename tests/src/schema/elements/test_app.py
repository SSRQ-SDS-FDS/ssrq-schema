import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-app",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e'>quadringentesimo</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-with-multiple-readings",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">quadringentesimo</rdg>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">lxxxiiij</rdg>
                </app>""",
            True,
        ),
        (
            "invalid-app-without-lem",
            """<app>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">quadringentesimo</rdg>
                </app>""",
            False,
        ),
        (
            "invalid-app-without-rdg",
            "<app><lem>lxxxvij</lem></app>",
            False,
        ),
        (
            "invalid-app-wrong-sequence",
            """<app>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">quadringentesimo</rdg>
                    <lem>lxxxvij</lem>
                </app>""",
            False,
        ),
        (
            "invalid-app-with-attributes",
            """<app type='foo'>
                    <lem>lxxxvij</lem>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">quadringentesimo</rdg>
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
