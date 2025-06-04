import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-fileDesc",
            """
            <fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp>Transkription</resp>
                    </respStmt>
                </titleStmt>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">
                            Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                        </licence>
                    </availability>
                </publicationStmt>
                <seriesStmt>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                        <resp>Herausgabe</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>
                <sourceDesc>
                    <msDesc>
                        <msIdentifier>
                            <settlement ref="loc123456" xml:lang="de">foo</settlement>
                            <repository xml:lang="de">foo</repository>
                            <idno xml:lang="de" source="http://foo.bar">bar</idno>
                        </msIdentifier>
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary xml:lang="de">
                                <p>foo</p>
                            </summary>
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
                                    <extent>
                                        <dimensions type="leaves">
                                            <height unit="cm" quantity="36.0"/>
                                            <width unit="cm" quantity="23.5"/>
                                        </dimensions>
                                    </extent>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate type='document' calendar='gregorian' 
                                    from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>
            """,
            True,
        ),
        (
            "invalid-fileDesc-without-titleStmt",
            """
            <fileDesc>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">
                            Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                        </licence>
                    </availability>
                </publicationStmt>
                <seriesStmt>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                        <resp>Herausgabe</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>
                <sourceDesc>
                    <msDesc>
                        <msIdentifier>
                            <settlement ref="loc123456" xml:lang="de">foo</settlement>
                            <repository xml:lang="de">foo</repository>
                            <idno xml:lang="de" source="http://foo.bar">bar</idno>
                        </msIdentifier>
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary xml:lang="de">
                                <p>foo</p>
                            </summary>
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
                                    <extent>
                                        <dimensions type="leaves">
                                            <height unit="cm" quantity="36.0"/>
                                            <width unit="cm" quantity="23.5"/>
                                        </dimensions>
                                    </extent>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate type='document' calendar='gregorian' 
                                    from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>
            """,
            False,
        ),
        (
            "invalid-fileDesc-without-seriesStmt",
            """
            <fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp>Transkription</resp>
                    </respStmt>
                </titleStmt>
                <seriesStmt>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                        <resp>Herausgabe</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>
                <sourceDesc>
                    <msDesc>
                        <msIdentifier>
                            <settlement ref="loc123456" xml:lang="de">foo</settlement>
                            <repository xml:lang="de">foo</repository>
                            <idno xml:lang="de" source="http://foo.bar">bar</idno>
                        </msIdentifier>
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary xml:lang="de">
                                <p>foo</p>
                            </summary>
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
                                    <extent>
                                        <dimensions type="leaves">
                                            <height unit="cm" quantity="36.0"/>
                                            <width unit="cm" quantity="23.5"/>
                                        </dimensions>
                                    </extent>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate type='document' calendar='gregorian' 
                                    from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>
            """,
            False,
        ),
        (
            "invalid-fileDesc-without-seriesStmt",
            """
            <fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp>Transkription</resp>
                    </respStmt>
                </titleStmt>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/"
                            >Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA
                            4.0)</licence>
                    </availability>
                </publicationStmt>
                <sourceDesc>
                    <msDesc>
                        <msIdentifier>
                            <settlement ref="loc123456" xml:lang="de">foo</settlement>
                            <repository xml:lang="de">foo</repository>
                            <idno xml:lang="de" source="http://foo.bar">bar</idno>
                        </msIdentifier>
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary xml:lang="de">
                                <p>foo</p>
                            </summary>
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
                                    <extent>
                                        <dimensions type="leaves">
                                            <height unit="cm" quantity="36.0"/>
                                            <width unit="cm" quantity="23.5"/>
                                        </dimensions>
                                    </extent>
                                </supportDesc>
                            </objectDesc>
                        </physDesc>
                        <history>
                            <origin>
                                <origDate type='document' calendar="unknown" 
                                    from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>
            """,
            False,
        ),
        (
            "invalid-fileDesc-without-sourceDesc",
            """
            <fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp>Transkription</resp>
                    </respStmt>
                </titleStmt>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">
                            Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                        </licence>
                    </availability>
                </publicationStmt>
                <seriesStmt>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung der Schweizerischen Juristischen Gesellschaft</orgName>
                        <resp>Herausgabe</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>
            </fileDesc>
            """,
            False,
        ),
    ],
)
def test_file_desc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("fileDesc", name, markup, result, False)
