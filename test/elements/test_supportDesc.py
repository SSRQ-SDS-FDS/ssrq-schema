import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-supportDesc",
            """<supportDesc>
                            <support>
                                <material type='paper'/>
                            </support>
                            <extent>
                                <dimensions type="leaves">
                                    <height unit="cm" quantity="29.0"/>
                                    <width unit="cm" quantity="54.5"/>
                                </dimensions>
                            </extent>
                        </supportDesc>""",
            True,
        ),
        (
            "supportDesc-with-all-childen",
            """<supportDesc>
                            <support>
                                <material type="paper"/>
                            </support>
                            <extent>
                                <dimensions type="leaves">
                                    <height unit="cm" quantity="33.0"/>
                                    <width unit="cm" quantity="24.0"/>
                                </dimensions>
                            </extent>
                            <foliation>
                                <p>Originale Foliierung des 15. Jhs.</p>
                            </foliation>
                            <condition agent="clipping">
                                <p>Beschneidung am Rand</p>
                            </condition>
                        </supportDesc>""",
            True,
        ),
        (
            "invalid-supportDesc-with-extent-first",
            """<supportDesc>
                            <extent>
                                <dimensions type="leaves">
                                    <height unit="cm" quantity="29.0"/>
                                    <width unit="cm" quantity="54.5"/>
                                </dimensions>
                            </extent>
                            <support>
                                <material type='papier'>Pergament</material>
                            </support>
                        </supportDesc>""",
            False,
        ),
        (
            "invalid-supportDesc-without-support",
            """<supportDesc>
                            <extent>
                                <dimensions type="leaves">
                                    <height unit="cm" quantity="29.0"/>
                                    <width unit="cm" quantity="54.5"/>
                                </dimensions>
                            </extent>
                        </supportDesc>""",
            False,
        ),
    ],
)
def test_supportDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("supportDesc", name, markup, result, False)
