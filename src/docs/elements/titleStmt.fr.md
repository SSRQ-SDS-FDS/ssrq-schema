---
title: titleStmt
---



# `<titleStmt/>` (Informations sur le titre)

## Description

Contient des éléments décrivant le titre et les responsabilités. 

## Modèle de contenu

- **core**: [editor](editor.md) [respStmt](respStmt.md) [title](title.md)

## Exemples

### Exemple 1

Exemple de titleStmt avec deux rédacteurs

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
            <resp>Transkription</resp>
        </respStmt>
        <respStmt>
            <persName>Ariane Huber Hernández</persName>
            <persName>Michael Nadig</persName>
            <resp>XML-Codierung der Transkription</resp>
        </respStmt>
    </titleStmt>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)