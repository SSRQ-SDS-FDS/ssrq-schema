import pytest

from ..conftest import RNG_test_function


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
                        <objectDesc>
                            <supportDesc>
                                <support>
                                    <material type="paper"/>
                                </support>
                            </supportDesc>
                        </objectDesc>
                    </physDesc>
                    <history>
                        <origin>
                            <origDate type="document" calendar="gregorian" when-custom="1600-01-01"/>
                        </origin>
                    </history>
                </msDesc>
            </witness>
            """,
            True,
        ),
        (
            "invalid-witness-without-xml-id",
            """
            <witness n="A">
                <msDesc>
                    <head>foo</head>
                    <physDesc>
                        <objectDesc>
                            <supportDesc>
                                <support>
                                    <material type="paper"/>
                                </support>
                            </supportDesc>
                        </objectDesc>
                    </physDesc>
                    <history>
                        <origin>
                            <origDate type="document" calendar="gregorian" when-custom="1600-01-01"/>
                        </origin>
                    </history>
                </msDesc>
            </witness>
            """,
            False,
        ),
        (
            "invalid-witness-without-n",
            """
                <witness xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>
                    <msDesc>
                        <head>foo</head>
                        <physDesc>
                            <objectDesc>
                                <supportDesc>
                                    <support>
                                        <material type="paper"/>
                                    </support>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate type="document" calendar="gregorian" when-custom="1600-01-01"/>
                            </origin>
                        </history>
                    </msDesc>
                </witness>""",
            False,
        ),
        (
            "invalid-witness-with-wrong-content",
            "<witness n='A' xml:id='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</witness>",
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
    test_element_with_rng("witness", name, markup, result, False)
