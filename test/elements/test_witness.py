from test.conftest import RNG_test_function, load_example

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-witness",
            """
                <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d' n="A">
                    <msDesc>
                        <head>foo</head>
                        <physDesc>
                            <objectDesc form="book">
                                <supportDesc>
                                    <support>
                                        <material type="paper"/>
                                    </support>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate calendar="gregorian" when-custom="1600-01-01"/>
                            </origin>
                        </history>
                    </msDesc>
                </witness>""",
            True,
        ),
        (
            "invalid-witness-xml-id",
            """
                <witness xml:id='bla' n="A">
                    <msDesc>
                        <head>foo</head>
                        <physDesc>
                            <objectDesc form="book">
                                <supportDesc>
                                    <support>
                                        <material type="paper"/>
                                    </support>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate calendar="gregorian" when-custom="1600-01-01"/>
                            </origin>
                        </history>
                    </msDesc>
                </witness>""",
            False,
        ),
        (
            "witness-with-invalid-attribute",
            """
                <witness type="foo">
                    <msDesc>
                        <head>foo</head>
                        <physDesc>
                            <objectDesc form="book">
                                <supportDesc>
                                    <support>
                                        <material type="paper"/>
                                    </support>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate calendar="gregorian" when-custom="1600-01-01"/>
                            </origin>
                        </history>
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
