---
title: publisher
---



# `<publisher/>` (Verlag)

## Beschreibung

Enthält bei Druckschriften als Teil von [`<docImprint/>`](docImprint.md)  den Namen der Druckerei oder des Druckers, als Teil von[`<publicationStmt/>`](publicationStmt.md)  die Angabe der herausgebenden Institution.

## Inhaltsmodell

- Beliebiger Textinhalt

## Attribute

### @cert

Angabe des Grads der Sicherheit

*Mögliche Werte*

- high – *hoch*
- medium – *mittel*
- low – *niedrig*

## Beispiele

### Beispiel 1

Beispiel für ein Impressum mit Druckort und Druckerei

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

### Beispiel 2

Beispiel für tei:publisher mit @cert

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher cert="low">Heidegger und Rahn</publisher>
    </docImprint>
</egXML>
               
```

### Beispiel 3

Beispiel für tei:publisher innerhalb von tei:publicationStmt

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <publicationStmt>
        <publisher>SSRQ-SDS-FDS</publisher>
    </publicationStmt>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)