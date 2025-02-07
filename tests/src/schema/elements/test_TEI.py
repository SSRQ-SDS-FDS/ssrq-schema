import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-TEI",
            """
            <TEI xml:lang="de">
                <teiHeader>
                    <fileDesc>
                        <titleStmt>
                            <title>xyz</title>
                            <editor>
                                <persName>xyz</persName>
                            </editor>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Transkription</resp>
                                <resp>XML-Codierung der Transkription</resp>
                            </respStmt>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Qualitätskontrolle</resp>
                            </respStmt>
                        </titleStmt>
                        <publicationStmt>
                            <publisher>SSRQ-SDS-FDS</publisher>
                            <date type="electronic" when-custom="0000-01-01"/>
                            <date type="print" when-custom="0000-01-01"/>
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
                            <idno>SSRQ-EX-I_1-1-1</idno>
                            <idno type="uuid">b06d72bd-6e9f-48db-9573-9d19b9cbb396</idno>
                        </seriesStmt>
                        <sourceDesc>
                            <msDesc>
                                <msIdentifier>
                                    <settlement xml:lang="de" ref="loc000000">xyz</settlement>
                                    <repository xml:lang="de">xyz</repository>
                                    <idno xml:lang="de">xyz</idno>
                                </msIdentifier>
                                <head>xyz</head>
                                <msContents>
                                    <summary xml:lang="de">
                                        <p>xyz</p>
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
                                        </supportDesc>
                                    </objectDesc>
                                </physDesc>
                                <history>
                                    <origin>
                                       <origDate type="document" calendar="unknown" when-custom="0000-01-01"/>
                                        <origPlace type="document" ref="loc000000">xyz</origPlace>
                                    </origin>
                                </history>
                            </msDesc>
                        </sourceDesc>
                    </fileDesc>
                    <encodingDesc>
                        <editorialDecl>
                            <p>
                                <ref target="https://p.ssrq-sds-fds.ch/guidelines/transcription"/>
                            </p>
                        </editorialDecl>
                    </encodingDesc>
                </teiHeader>
                <text type="transcript">
                    <body>
                        <div>
                            <p>xyz</p>
                        </div>
                    </body>
                </text>
            </TEI>
            """,
            True,
        ),
        (
            "invalid-TEI-without-xml-lang",
            """
            <TEI>
                <teiHeader>
                    <fileDesc>
                        <titleStmt>
                            <title>xyz</title>
                            <editor>
                                <persName>xyz</persName>
                            </editor>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Transkription</resp>
                                <resp>XML-Codierung der Transkription</resp>
                            </respStmt>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Qualitätskontrolle</resp>
                            </respStmt>
                        </titleStmt>
                        <publicationStmt>
                            <publisher>SSRQ-SDS-FDS</publisher>
                            <date type="electronic" when-custom="0000-01-01"/>
                            <date type="print" when-custom="0000-01-01"/>
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
                            <idno>SSRQ-EX-I_1-1-1</idno>
                            <idno type="uuid">b06d72bd-6e9f-48db-9573-9d19b9cbb396</idno>
                        </seriesStmt>
                        <sourceDesc>
                            <msDesc>
                                <msIdentifier>
                                    <settlement xml:lang="de" ref="loc000000">xyz</settlement>
                                    <repository xml:lang="de">xyz</repository>
                                    <idno xml:lang="de">xyz</idno>
                                </msIdentifier>
                                <head>xyz</head>
                                <msContents>
                                    <summary xml:lang="de">
                                        <p>xyz</p>
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
                                        </supportDesc>
                                    </objectDesc>
                                </physDesc>
                                <history>
                                    <origin>
                                       <origDate type="document" calendar="unknown" when-custom="0000-01-01"/>
                                        <origPlace type="document" ref="loc000000">xyz</origPlace>
                                    </origin>
                                </history>
                            </msDesc>
                        </sourceDesc>
                    </fileDesc>
                    <encodingDesc>
                        <editorialDecl>
                            <p>
                                <ref target="https://p.ssrq-sds-fds.ch/guidelines/transcription"/>
                            </p>
                        </editorialDecl>
                    </encodingDesc>
                </teiHeader>
                <text type="transcript">
                    <body>
                        <div>
                            <p>xyz</p>
                        </div>
                    </body>
                </text>
            </TEI>
            """,
            False,
        ),
        (
            "invalid-TEI-without-teiHeader",
            """
            <TEI xml:lang="de">
                <text type='transcript'>
                    <body>
                        <div>
                            <p>foo</p>
                        </div>
                    </body>
                </text>
            </TEI>
            """,
            False,
        ),
        (
            "invalid-TEI-without-text",
            """
            <TEI xml:lang="de">
                <teiHeader>
                    <fileDesc>
                        <titleStmt>
                            <title>xyz</title>
                            <editor>
                                <persName>xyz</persName>
                            </editor>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Transkription</resp>
                                <resp>XML-Codierung der Transkription</resp>
                            </respStmt>
                            <respStmt>
                                <persName>xyz</persName>
                                <resp>Qualitätskontrolle</resp>
                            </respStmt>
                        </titleStmt>
                        <publicationStmt>
                            <publisher>SSRQ-SDS-FDS</publisher>
                            <date type="electronic" when-custom="0000-01-01"/>
                            <date type="print" when-custom="0000-01-01"/>
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
                            <idno>SSRQ-EX-I_1-1-1</idno>
                            <idno type="uuid">b06d72bd-6e9f-48db-9573-9d19b9cbb396</idno>
                        </seriesStmt>
                        <sourceDesc>
                            <msDesc>
                                <msIdentifier>
                                    <settlement xml:lang="de" ref="loc000000">xyz</settlement>
                                    <repository xml:lang="de">xyz</repository>
                                    <idno xml:lang="de">xyz</idno>
                                </msIdentifier>
                                <head>xyz</head>
                                <msContents>
                                    <summary xml:lang="de">
                                        <p>xyz</p>
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
                                        </supportDesc>
                                    </objectDesc>
                                </physDesc>
                                <history>
                                    <origin>
                                       <origDate type="document" calendar="unknown" when-custom="0000-01-01"/>
                                        <origPlace type="document" ref="loc000000">xyz</origPlace>
                                    </origin>
                                </history>
                            </msDesc>
                        </sourceDesc>
                    </fileDesc>
                    <encodingDesc>
                        <editorialDecl>
                            <p>
                                <ref target="https://p.ssrq-sds-fds.ch/guidelines/transcription"/>
                            </p>
                        </editorialDecl>
                    </encodingDesc>
                </teiHeader>
            </TEI>
            """,
            False,
        ),
        (
            "invalid-TEI-with-wrong-content",
            "<TEI xml:lang='de'><p>foo</p></TEI>",
            False,
        ),
    ],
)
def test_tei_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("TEI", name, markup, result, True)
