---
title: titleStmt
---



# `<titleStmt/>` (Angaben zum Titel)

## Beschreibung

Enthält Elemente zur Beschreibung des Titels und der Verantwortlichkeiten. 

## Inhaltsmodell

- **core**: [editor](editor.md) [respStmt](respStmt.md) [title](title.md)

## Beispiele

### Beispiel 1

Beispielhaftes titleStmt mit zwei Editor*innen

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

## Abschnitte in den Guidelines der TEI

- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)