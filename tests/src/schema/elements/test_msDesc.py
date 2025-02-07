import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import (
    RNG_test_function,
    SimpleTEIWriter,
    add_tei_namespace,
)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msDesc-with-physDesc",
            """
            <msDesc>
                <head>Foo</head>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
            </msDesc>
            """,
            True,
        ),
        (
            "valid-msDesc-with-adminInfo",
            """
            <msDesc>
                <head>Foo</head>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
                <additional>
                    <adminInfo>
                        <custodialHist>
                            <custEvent type="lost">Foo</custEvent>
                        </custodialHist>
                    </adminInfo>
                </additional>
            </msDesc>
            """,
            True,
        ),
        (
            "valid-msDesc-with-multiple-heads",
            """
            <msDesc>
                <head>Foo</head>
                <head>Bar</head>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
            </msDesc>
            """,
            True,
        ),
        (
            "valid-msDesc-with-msIdentifier",
            """
            <msDesc>
                <msIdentifier>
                    <repository xml:lang="de">Foo</repository>
                    <idno xml:lang="de">Foo</idno>
                </msIdentifier>
                <head>Foo</head>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
            </msDesc>
            """,
            True,
        ),
        (
            "valid-msDesc-with-msContents",
            """
            <msDesc>
                <head>Foo</head>
                 <msContents>
                    <msItem>
                        <textLang xml:lang="de"/>
                    </msItem>
                 </msContents>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
            </msDesc>
            """,
            True,
        ),
        (
            "valid-msDesc-with-additional",
            """
            <msDesc>
                <head>Foo</head>
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
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
                <additional>
                    <listBibl type="edition">
                        <bibl>Foo</bibl>
                    </listBibl>
                </additional>
            </msDesc>
            """,
            True,
        ),
    ],
)
def test_ms_desc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msDesc", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msDesc-without-physDesc-with-adminInfo",
            "<msDesc><adminInfo/></msDesc>",
            True,
        ),
        (
            "valid-msDesc-with-physDesc-and-without-adminInfo",
            """
            <msDesc>
                <physDesc>
                    <objectDesc>
                        <supportDesc>
                            <support>
                                <material type="paper"/>
                            </support>
                        </supportDesc>
                    </objectDesc>
                </physDesc>
            </msDesc>""",
            True,
        ),
        (
            "valid-msDesc-without-physDesc-and-adminInfo-and-text-type-collection",
            "<TEI><msDesc/><text type='collection'><body><div><p>foo</p></div></body></text></TEI>",
            True,
        ),
        (
            "invalid-msDesc-with-physDesc-and-text-type-collection",
            """
            <TEI>
                <msDesc>
                    <physDesc>
                    <objectDesc>
                        <supportDesc>
                            <support>
                                <material type="paper"/>
                            </support>
                        </supportDesc>
                    </objectDesc>
                    </physDesc>
                </msDesc>
                <text type='collection'><body><div><p>foo</p></div></body></text>
            </TEI>
            """,
            False,
        ),
        (
            "invalid-msDesc-with-adminInfo-and-text-type-collection",
            """
            <TEI>
                <msDesc><adminInfo/></msDesc>
                <text type='collection'><body><div><p>foo</p></div></body></text>
            </TEI>
            """,
            False,
        ),
        (
            "invalid-msDesc-without-physDesc-and-adminInfo-and-text-type-transcript",
            """
            <TEI>
                <msDesc/>
                <text type='transcript'><body><div><p>foo</p></div></body></text>
            </TEI>
            """,
            False,
        ),
    ],
)
def test_ms_desc_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result
