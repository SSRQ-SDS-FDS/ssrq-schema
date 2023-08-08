import pytest

from ..conftest import RNG_test_function, load_example


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sourceDesc",
            """
                    <sourceDesc>
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
                    </sourceDesc>
                """,
            True,
        ),
        (
            "invalid-sourceDesc",
            "<sourceDesc><p>foo</p></sourceDesc>",
            False,
        ),
    ],
)
def test_sourceDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    markup = markup.format(msDesc=load_example("msDesc.xml"))
    test_element_with_rng("sourceDesc", name, markup, result, False)
