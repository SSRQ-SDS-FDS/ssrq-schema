---
title: width
---



# `<width/>`

## Beschreibung

Beschreibt die Breite eines Blattes oder Buchs sowie die Breite der Plica. 

## Erläuterung

Die Masseinheit für [@unit](#unit)  ist Zentimeter (cm).

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @quantity

Gibt die Grösse der mit [@unit](#unit)  angegebenen Einheit an

*Mögliche Werte*

- Gleitkommazahl
- Zahl
- unknown – *unbekannt*

### @unit

Masseinheit

*Mögliche Werte*

- unknown – *unbekannt*
- cm – *cm*

## Beispiele

### Beispiel 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <width unit="cm" quantity="23.0" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)