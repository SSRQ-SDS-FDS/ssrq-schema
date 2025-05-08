import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


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


@pytest.mark.parametrize(
    "name, markup, result",
    [
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
                <sealDesc>
                    <seal condition="absent" n="1"/>
                </sealDesc>
            </physDesc>
            """,
            True,
        ),
        (
            "invalid-physDesc-without-bindingDesc",
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
            False,
        ),
    ],
)
def test_phys_desc_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )

    assert reports[0].report.is_valid() is result
