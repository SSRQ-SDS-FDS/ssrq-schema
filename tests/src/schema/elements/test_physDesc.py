import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-physDesc",
            """
            <physDesc>
                <objectDesc>
                    <supportDesc>
                        <support>
                            <material type="paper"/>
                        </support>
                    </supportDesc>
                </objectDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "valid-physDesc-with-bindingDesc",
            """
            <physDesc>
                <objectDesc>
                    <supportDesc>
                        <support>
                            <material type="paper"/>
                        </support>
                    </supportDesc>
                </objectDesc>
                <bindingDesc>
                    <p>foo</p>
                </bindingDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "valid-physDesc-with-handDesc",
            """
            <physDesc>
                <objectDesc>
                    <supportDesc>
                        <support>
                            <material type="paper"/>
                        </support>
                    </supportDesc>
                </objectDesc>
                <handDesc>
                    <handNote xml:id="otherHand"/>
                </handDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "valid-physDesc-with-sealDesc",
            """
            <physDesc>
                <objectDesc>
                    <supportDesc>
                        <support>
                            <material type="paper"/>
                        </support>
                    </supportDesc>
                </objectDesc>
                <sealDesc>
                    <seal condition="absent" n="1"/>
                </sealDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "valid-full-physDesc",
            """
            <physDesc>
                <objectDesc>
                    <supportDesc>
                        <support>
                            <material type="paper"/>
                        </support>
                    </supportDesc>
                </objectDesc>
                <bindingDesc>
                    <p>foo</p>
                </bindingDesc>
                <handDesc>
                    <handNote xml:id="otherHand"/>
                </handDesc>
                <sealDesc>
                    <seal condition="absent" n="1"/>
                </sealDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "invalid-full-physDesc-with-wrong-orger",
            """
                <physDesc>
                    <sealDesc>
                        <seal condition="absent" n="1"/>
                    </sealDesc>
                    <objectDesc>
                        <supportDesc>
                            <support>
                                <material type="paper"/>
                            </support>
                        </supportDesc>
                    </objectDesc>
                    <bindingDesc>
                        <p>foo</p>
                    </bindingDesc>
                    <handDesc>
                        <handNote xml:id="otherHand"/>
                    </handDesc>
                </physDesc>
                """,
            False,
        ),
    ],
)
def test_phys_desc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("physDesc", name, markup, result, False)
