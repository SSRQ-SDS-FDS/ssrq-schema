from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-fileDesc",
            """<fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp key="transcript"/>
                    </respStmt>
                </titleStmt>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <p xml:id="facs">Bibliothèque publique et universitaire de Neuchâtel
                            (BPUN)</p>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/"
                            >Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA
                            4.0)</licence>
                    </availability>
                </publicationStmt>
                <seriesStmt xml:id="ssrq-sds-fds">
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                        <resp key="publisher"/>
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
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary>
                                <p xml:lang="de">foo</p>
                            </summary>
                            <msItem>
                                <textLang xml:lang="de"/>
                                <filiation type="current">Abschrift, Buch (729 Seiten) mit
                                    kartoniertem Einband</filiation>
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
                                <origDate calendar='gregorian' from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>""",
            True,
        ),
        (
            "invalid-fileDesc-with-missing-seriesStmt",
            """<fileDesc>
                <titleStmt>
                    <title>foo</title>
                    <editor>
                        <persName>Michael Nadig</persName>
                    </editor>
                    <respStmt>
                        <persName>Ariane Huber Hernández</persName>
                        <persName>Michael Nadig</persName>
                        <resp key="transcript"/>
                    </respStmt>
                </titleStmt>
                <publicationStmt>
                    <publisher>SSRQ-SDS-FDS</publisher>
                    <availability>
                        <p xml:id="facs">Bibliothèque publique et universitaire de Neuchâtel
                            (BPUN)</p>
                        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/"
                            >Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA
                            4.0)</licence>
                    </availability>
                </publicationStmt>
                <sourceDesc>
                    <msDesc>
                        <msIdentifier>
                            <idno xml:lang="de" source="http://foo.bar">bar</idno>
                            <repository xml:lang="de">foo</repository>
                        </msIdentifier>
                        <head>Projekt eines Eides für den Förster oder Bannwart in
                            Sax-Forstegg</head>
                        <msContents>
                            <summary>
                                <p xml:lang="de">foo</p>
                            </summary>
                            <msItem>
                                <textLang xml:lang="de"/>
                                <filiation type="current">Abschrift, Buch (729 Seiten) mit
                                    kartoniertem Einband</filiation>
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
                                <origDate calendar="unknown" from-custom="1615-04-15" to-custom="1700-12-31"/>
                            </origin>
                        </history>
                    </msDesc>
                </sourceDesc>
            </fileDesc>""",
            False,
        ),
    ],
)
def test_fileDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("fileDesc", name, markup, result, False)
