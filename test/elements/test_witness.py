from test.conftest import RNG_test_function, load_example

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-witness",
            """<witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d' n="A">{msDesc}</witness>""",
            True,
        ),
        (
            "invalid-witness-xml-id",
            """<witness xml:id='bla' n="A">
                                                    <msDesc>
                                                        <msIdentifier>
                                                            <idno>foo</idno>
                                                            <repository>bar</repository>
                                                        </msIdentifier>
                                                    </msDesc>
                                                </witness>""",
            False,
        ),
        (
            "witness-with-invalid-attribute",
            """<witness type="foo">
                                                                <msDesc>
                                                                    <msIdentifier>
                                                                        <idno>foo</idno>
                                                                        <repository>bar</repository>
                                                                    </msIdentifier>
                                                                </msDesc>
                                                            </witness>""",
            False,
        ),
    ],
)
def test_witness(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    markup = markup.format(msDesc=load_example("msDesc.xml"))
    test_element_with_rng("witness", name, markup, result, False)
