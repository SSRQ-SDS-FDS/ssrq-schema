---
title: editor
---



# `<editor/>`

## Description

Désigne, dans une notice bibliographique, l'éditeur d'une publication. Dans le [`<titleStmt/>`](titleStmt.md)  d'une pièce, on saisit ainsi les éditeurs de l'unité d'édition.

## Modèle de contenu

- **namesdates**: [persName](persName.md)
- Contenu de texte au choix

## Exemples

### Exemple 1

Exemple d'indication bibliographique

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <biblStruct>
        <analytic>
            <author>Holenstein, André</author>
            <title level="a">Seelenheil und Untertanenpflicht. Zur gesellschaftlichen
                        Funktion und theoretischen Begründung des Eides in der ständischen
                        Gesellschaft
                    </title>
        </analytic>
        <monogr>
            <title level="m">Der Fluch und der Eid. Die metaphysische Begründung
                        gesellschaftlichen Zusammenlebens und politischer Ordnung in der ständischen
                        Gesellschaft
                    </title>
            <editor>Peter Blickle</editor>
            <imprint>
                <pubPlace>Berlin</pubPlace>
                <date when="1993">1993</date>
            </imprint>
        </monogr>
        <monogr>
            <title level="m">Zeitschrift für historische Forschung</title>
            <note>Beih.</note>
            <imprint>
                <biblScope type="vol">15</biblScope>
                <biblScope type="pp">11–63</biblScope>
            </imprint>
        </monogr>
    </biblStruct>
</egXML>
               
```

### Exemple 2

Exemple de saisie des collaborateurs d'une unité d'édition

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <titleStmt>
        <title>I. Abteilung: Die Rechtsquellen des Kantons Zürich. Neue Folge. Zweiter Teil:
                    Rechte der Landschaft. Band 11: Die Obervogteien um die Stadt Zürich
                </title>
        <editor>
            <persName>Ariane Huber Hernández</persName>
        </editor>
        <editor>
            <persName>Michael Nadig</persName>
        </editor>
        <respStmt>
            <persName>Ariane Huber Hernández</persName>
            <persName>Michael Nadig</persName>
            <resp key="transcript" />
        </respStmt>
        <respStmt>
            <persName>Ariane Huber Hernández</persName>
            <persName>Michael Nadig</persName>
            <resp key="tagging" />
        </respStmt>
    </titleStmt>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)