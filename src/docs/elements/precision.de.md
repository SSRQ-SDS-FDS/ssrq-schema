---
title: precision
---



# `<precision/>`

## Beschreibung

Gibt Unsicherheit bei Datierungen an.

## Erläuterung

Mit [@match](#match)  wird auf ein oder mehrere Attribute von[`<date/>`](date.md)  Bezug genommen. Mit[@precision](#precision)  wird der Grad der Unsicherheit angegeben.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @match

Verweist mittels eines einfachen XPath-Ausdrucks auf den unsicheren Bestandteil – das unsichere Attribut – einer Datierung. 

*Mögliche Werte*

- Zeichenkette

### @precision



*Mögliche Werte*

- high
- medium
- low
- unknown

## Beispiele

### Beispiel 1

Beispiel für ein unsicheres Datum

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" notBefore-custom="1341-01-01" notAfter-custom="1355-12-31">
        Um 1346 und um 1350
        <precision precision="low" match="@notBefore-custom @notAfter-custom" />
    </date>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [21.2. Indications of Precision](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html#CEPREC)