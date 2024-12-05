import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-app",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>Foo</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-without-lem",
            """<app>
                  <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">Foo</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-with-multiple-readings",
            """<app>
                    <lem>lxxxvij</lem>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">Foo</rdg>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">Bar</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-with-note",
            """<app>
                    <lem>lxxxvij</lem>
                    <note>Foo</note>
                </app>""",
            True,
        ),
        (
            "valid-app-with-note-and-rdg",
            """<app>
                    <lem>lxxxvij</lem>
                    <note type="text_comparison"><ref>Bar</ref></note>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">Foo</rdg>
                </app>""",
            True,
        ),
        (
            "valid-app-with-multiple-notes-and-rdgs",
            """<app>
                    <lem>lxxxvij</lem>
                    <note type="text_comparison"><ref>Bar</ref></note>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d">Foo</rdg>
                    <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e">Baz</rdg>
                    <note type="text_comparison"><ref>Foos</ref></note>
                </app>""",
            True,
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
    ],
)
def test_app(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("app", name, markup, result, False)
