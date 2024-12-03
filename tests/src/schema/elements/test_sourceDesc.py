import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sourceDesc-with-msDesc",
            """
            <sourceDesc>
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
                            <origDate type='content' calendar="gregorian" when-custom="1600-01-01"/>
                        </origin>
                    </history>
                </msDesc>
            </sourceDesc>
            """,
            True,
        ),
        (
            "valid-sourceDesc-with-listWit",
            """
            <sourceDesc>
                <listWit>
                    <witness xml:id='id-ssrq-00000000-0000-4000-8000-000000000000' n='A'>
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
                                    <origDate type='document' calendar="unknown" when-custom="1000-01-01"/>
                                </origin>
                            </history>
                        </msDesc>
                    </witness>
                </listWit>
            </sourceDesc>
            """,
            True,
        ),
        (
            "invalid-sourceDesc-with-wrong-content",
            "<sourceDesc><p>foo</p></sourceDesc>",
            False,
        ),
    ],
)
def test_source_desc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sourceDesc", name, markup, result, False)
