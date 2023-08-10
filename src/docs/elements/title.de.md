---
title: title
---



# `<title/>` (Titel)

## Beschreibung

Enthält als Teil des [`<titleStmt/>`](titleStmt.md)  den Titel des Rechtsquellenbandes bzw. der Editionseinheit, als Teil des[`<seriesStmt/>`](seriesStmt.md)  den Titel der Serie.

## Erläuterung

Ein Buchtitel, der innerhalb einer Quelle zitiert wird, wird ebenfalls mit [`<title/>`](title.md)  und[@xml:lang](#xml:lang)  ausgezeichnet.

## Inhaltsmodell

- **core**: [hi](hi.md)
- Beliebiger Textinhalt

## Attribute

### @type

Klassifiziert den Titel entsprechend einer geeigneten Typologie.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[^\p{C}\p{Z}]+`

### @xml:lang

ISO-639-1-Sprachkürzel

*Mögliche Werte*

- de – *Deutsch*
- fr – *Französisch*
- he – *Hebräisch*
- it – *Italienisch*
- la – *Latein*
- rm – *Bündnerromanisch*

## Beispiele

### Beispiel 1

Einfacher Titel

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <title>Rechtsquellen der Stadt und Herrschaft Rapperswil (mit den Höfen Busskirch/Jona,
                Kempraten und Wagen)
            </title>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)