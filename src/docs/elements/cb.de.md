---
title: cb
---



# `<cb/>` (Spaltenbeginn)

## Beschreibung

Beschreibt den Beginn einer neuen Spalte.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @n

Enthält Angaben zur originalen Spaltenzählung.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[a-z]{1}`

## Beispiele

### Beispiel 1

Beispiel für den Beginn einer neuen Spalte.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="1r" />
    <cb n="a" />
    <p>...</p>
    <p>...</p>
    <cb n="b" />
    <p>...</p>
    <p>...</p>
    <pb n="1v" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)