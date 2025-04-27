import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-teiHeader",
            """
            <teiHeader>
                <fileDesc>
                    <titleStmt>
                        <title>xyz</title>
                        <editor>
                            <persName>xyz</persName>
                        </editor>
                        <respStmt>
                            <persName>xyz</persName>
                            <resp>XML-Codierung</resp>
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
                        <p>Born digital.</p>
                    </sourceDesc>
                </fileDesc>
            </teiHeader>
            """,
            True,
        ),
        (
            "invalid-teiHeader-with-encodingDesc",
            """
            <teiHeader>
                <fileDesc>
                    <titleStmt>
                        <title>xyz</title>
                        <editor>
                            <persName>xyz</persName>
                        </editor>
                        <respStmt>
                            <persName>xyz</persName>
                            <resp>XML-Codierung</resp>
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
                        <p>Born digital.</p>
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
            """,
            False,
        ),
        (
            "invalid-teiHeader-with-profileDesc",
            """
            <teiHeader>
                <fileDesc>
                    <titleStmt>
                        <title>xyz</title>
                        <editor>
                            <persName>xyz</persName>
                        </editor>
                        <respStmt>
                            <persName>xyz</persName>
                            <resp>XML-Codierung</resp>
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
                        <p>Born digital.</p>
                    </sourceDesc>
                </fileDesc>           
                <profileDesc>
                    <textClass>
                        <keywords>
                            <term ref="key123456"/>
                        </keywords>
                    </textClass>
                </profileDesc> 
            </teiHeader>
            """,
            False,
        ),
        (
            "invalid-teiHeader-without-fileDesc",
            "<teiHeader>foo</teiHeader>",
            False,
        ),
    ],
)
def test_tei_header(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("teiHeader", name, markup, result, False)
