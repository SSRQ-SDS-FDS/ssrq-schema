---
title: fileDesc
---



# `<fileDesc/>` (Dateibeschreibung)

## Beschreibung

Enthält Elemente zur Beschreibung der edierten Vorlage und der digitalen Erfassung. 

## Inhaltsmodell

- **header**: [publicationStmt](publicationStmt.md) [seriesStmt](seriesStmt.md) [sourceDesc](sourceDesc.md) [titleStmt](titleStmt.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau der Metadaten im Bereich fileDesc

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
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
                <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">Attribution-NonCommercial-
                            ShareAlike 4.0 International (CC BY-NC-SA
                            4.0)
                        </licence>
            </availability>
        </publicationStmt>
        <seriesStmt>
            <title>Sammlung Schweizerischer Rechtsquellen</title>
            <respStmt>
                <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                <resp key="publisher" />
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
                            Sax-Forstegg
                        </head>
                <msContents>
                    <summary>
                        <p xml:lang="de">foo</p>
                    </summary>
                    <msItem>
                        <textLang xml:lang="de" />
                    </msItem>
                </msContents>
                <physDesc>
                    <objectDesc form="copy">
                        <supportDesc>
                            <support>
                                <material type="paper" />
                            </support>
                            <extent>
                                <dimensions type="leaves">
                                    <height unit="cm" quantity="36.0" />
                                    <width unit="cm" quantity="23.5" />
                                </dimensions>
                            </extent>
                        </supportDesc>
                    </objectDesc>
                </physDesc>
                <history>
                    <origin>
                        <origDate from-custom="1615-04-15" to-custom="1700-12-31" />
                    </origin>
                </history>
            </msDesc>
        </sourceDesc>
    </fileDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)
- [2.1.1. The TEI Header and Its Components](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD11)