from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "TEI-valid",
            """<TEI xml:lang="de">
                                        <teiHeader>
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
                                                        >Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA
                                                        4.0)</licence>
                                                    </availability>
                                                </publicationStmt>
                                                <seriesStmt xml:id="ssrq-sds-fds">
                                                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                                                    <respStmt>
                                                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                                                        <resp>Herausgabe</resp>
                                                    </respStmt>
                                                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                                                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                                                </seriesStmt>
                                                <sourceDesc>
                                                    <msDesc>
                                                    <msIdentifier>
                                                        <idno xml:lang="de" source="http://foo.bar">bar</idno>
                                                        <repository xml:lang="de">foo</repository>
                                                    </msIdentifier>
                                                    <head>Projekt eines Eides für den Förster oder Bannwart in Sax-Forstegg</head>
                                                    <msContents>
                                                        <summary>
                                                            <p xml:lang="de">foo</p>
                                                        </summary>
                                                        <msItem>
                                                            <textLang xml:lang="de"/>
                                                        </msItem>
                                                    </msContents>
                                                    <physDesc>
                                                        <objectDesc form='copy'>
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
                                                            <origDate from-custom="1615-04-15" to-custom="1700-12-31" calendar="unknown"/>
                                                        </origin>
                                                    </history>
                                                    </msDesc>
                                                </sourceDesc>
                                            </fileDesc>
                                            <encodingDesc>
                                        <editorialDecl>
                                            <p>
                                                <ref target="https://www.ssrq-sds-fds.ch/wiki/Transkriptionsrichtlinien"/>
                                            </p>
                                        </editorialDecl>
                                    </encodingDesc>
                                        </teiHeader>
                                        <text type='transcript'>
                                            <body>
                                                <div><p>foo</p></div>
                                            </body>
                                        </text>
                                        </TEI>""",
            True,
            None,
        ),
        (
            "invalid-TEI-with-two-texts",
            """<TEI xml:lang="de">
                                        <teiHeader>
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
                                                <seriesStmt xml:id="ssrq-sds-fds">
                                                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                                                    <respStmt>
                                                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                                                        <resp>Herausgabe</resp>
                                                    </respStmt>
                                                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                                                    <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                                                </seriesStmt>
                                                <sourceDesc>
                                                    <msDesc>
                                                    <msIdentifier>
                                                        <idno xml:lang="de" source="http://foo.bar">bar</idno>
                                                        <repository xml:lang="de">foo</repository>
                                                    </msIdentifier>
                                                    <head>Projekt eines Eides für den Förster oder Bannwart in Sax-Forstegg</head>
                                                    <msContents>
                                                        <summary>
                                                            <p xml:lang="de">foo</p>
                                                        </summary>
                                                        <msItem>
                                                            <textLang xml:lang="de"/>
                                                        </msItem>
                                                    </msContents>
                                                    <physDesc>
                                                        <objectDesc form='copy'>
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
                                                            <origDate from-custom="1615-04-15" to-custom="1700-12-31" calendar="unknown"/>
                                                        </origin>
                                                    </history>
                                                    </msDesc>
                                                </sourceDesc>
                                            </fileDesc>
                                            <encodingDesc>
                                        <editorialDecl>
                                            <p>
                                                <ref target="https://www.ssrq-sds-fds.ch/wiki/Transkriptionsrichtlinien"/>
                                            </p>
                                        </editorialDecl>
                                    </encodingDesc>
                                        </teiHeader>
                                        <text type='transcript'>
                                            <body><div><p>foo</p></div></body>
                                        </text>
                                        <text type='summary'>
                                            <body><div><p>foo</p></div></body>
                                        </text>
                                        </TEI>""",
            False,
            None,
        ),
        (
            "TEI-invalid-content",
            "<TEI xml:lang='de'><teiHeader></teiHeader><facsimile></facsimile><text></text></TEI>",
            False,
            None,
        ),
        (
            "TEI-invalid-att",
            " <TEI xml:lang='fr' n='1234'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'attribute "n" not allowed here',
        ),
        (
            "TEI-invalid-lang",
            " <TEI xml:lang='pt'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'must be equal to "de", "fr" or "it"',
        ),
    ],
)
def test_TEI_main_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    rng_test = test_element_with_rng("TEI", name, markup, result, True)
    if message is not None and rng_test is not None:
        file_reports = rng_test.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
