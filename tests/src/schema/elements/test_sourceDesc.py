import pytest

from ..conftest import RNG_test_function


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
                                    <origDate type='document' calendar="gregorian" when-custom="1600-01-01"/>
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
    test_element_with_rng("sourceDesc", name, markup, result, False)
