import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listWit",
            """<listWit>
                            <witness xml:id='id-ssrq-00000000-0000-4000-8000-000000000000' n='A'>
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
                                            <origDate calendar="unknown" from-custom="1000-01-01" to-custom="1099-12-31">11. Jahrhundert</origDate>
                                        </origin>
                                    </history>
                                </msDesc>
                            </witness>
                            </listWit>""",
            True,
        ),
        (
            "valid-listWit-with-multiple-entries",
            """<listWit>
                            <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d' n='A'>
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
                                            <origDate calendar="unknown" from-custom="1000-01-01" to-custom="1099-12-31">11. Jahrhundert</origDate>
                                        </origin>
                                    </history>
                                </msDesc>
                            </witness>
                            <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e' n='B'>
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
                                            <origDate calendar="unknown" from-custom="1000-01-01" to-custom="1099-12-31">11. Jahrhundert</origDate>
                                        </origin>
                                    </history>
                                </msDesc>
                            </witness>
                        </listWit>""",
            True,
        ),
        (
            "invalid-empty-listWit",
            "<listWit></listWit>",
            False,
        ),
        (
            "invalid-listWit-with-attribute",
            """<listWit type='foo'>
                            <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d' n='A'>
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
                                            <origDate calendar="unknown" from-custom="1000-01-01" to-custom="1099-12-31">11. Jahrhundert</origDate>
                                        </origin>
                                    </history>
                                </msDesc>
                            </witness>
                        </listWit>""",
            False,
        ),
    ],
)
def test_listWit(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("listWit", name, markup, result, False)
