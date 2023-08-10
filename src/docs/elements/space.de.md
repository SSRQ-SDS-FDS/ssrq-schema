---
title: space
---



# `<space/>`

## Beschreibung

Zeichnet eine Lücke aus, die vom Schreiber bewusst zwecks späterer Ergänzung offen gelassen wurde. 

## Erläuterung

Die Grösse der Lücke wird zwingend mit [@unit](#unit)  und[@quantity](#quantity)  angegeben. Dabei handelt es sich um einen leeren Tag. Lücken infolge unbewusster Zeilensprünge werden hingegen mit[`<supplied/>`](supplied.md)  ausgezeichnet.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @quantity

Gibt die Grösse der mit [@unit](#unit)  angegebenen Einheit an

*Mögliche Werte*

- Gleitkommazahl
- Zahl
- unknown – *unbekannt*

### @resp



### @unit

Masseinheit

*Mögliche Werte*

- cm – *cm*
- line – *Zeile*
- character – *Buchstabe*
- page – *Seite*
- word – *Wort*

## Beispiele

### Beispiel 1

Beispiel für einen Freiraum von 5 cm

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <space quantity="5" unit="cm" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.4.1. Space](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHSP)