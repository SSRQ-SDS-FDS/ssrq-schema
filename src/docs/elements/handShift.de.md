---
title: handShift
---



# `<handShift/>` (Handwechsel)

## Beschreibung

Gibt den Wechsel einer Hand an.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @hand

Enthält einen Verweis auf die ID eines [`<handNote/>`](handNote.md)-Element, das im[`<teiHeader/>`](teiHeader.md)  deklariert wurde.

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für einen Handwechsel

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <lb />mutter im leben wär, soll die mutter den dritten
        <handShift hand="otherHand" />
        <lb />theil und die geschwüsterte die zwenn theil erben.
    </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.2.1. Document Hands](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDH)