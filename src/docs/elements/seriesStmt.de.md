---
title: seriesStmt
---



# `<seriesStmt/>` (Angaben zur Reihe)

## Beschreibung

Beinhaltet Elemente zur Beschreibung der Reihe Sammlung Schweizerischer Rechtsquellen. 

## Inhaltsmodell

- **core**: [respStmt](respStmt.md) [title](title.md)
- **header**: [idno](idno.md)

## Beispiele

### Beispiel 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seriesStmt>
        <title>Sammlung Schweizerischer Rechtsquellen</title>
        <respStmt>
            <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
            <resp>Herausgabe</resp>
        </respStmt>
        <idno>SSRQ-FR-I_2_8-1-1</idno>
        <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
    </seriesStmt>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)
- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)