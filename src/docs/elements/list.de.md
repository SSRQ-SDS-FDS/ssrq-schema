---
title: list
---



# `<list/>` (Liste)

## Beschreibung

Beschreibt eine Liste oder Aufzählung jeder Art.

## Inhaltsmodell

- **core**: [item](item.md)

## Attribute

### @rend

Angabe zur Darstellung der Liste

*Mögliche Werte*

- bulleted – *Liste mit Bullet-Points*
- numbered – *Nummerierte Liste*

### @type

Beschreibt die Art der Listenpunkte.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[^\p{C}\p{Z}]+`

## Beispiele

### Beispiel 1

Einfache Liste ohne Angabe zur Darstellung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <list>
        <item>Apfel</item>
        <item>Fisch</item>
        <item>...</item>
    </list>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.8. Lists](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COLI)