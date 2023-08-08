---
title: author
---



# `<author/>` (Autor)

## Beschreibung

Enthält als Teil einer bibliografischen Angabe den Autor einer Publikation und als Teil von [`<msItem/>`](msItem.md)  den Schreiber einer Quelle.

## Inhaltsmodell

- **namesdates**: [orgName](orgName.md) [persName](persName.md)
- Beliebiger Textinhalt

## Attribute

### @ref

Referenz auf die Datenbanken der SSRQ.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `key\d{6}$?`
- Zeichenkette – Einschränkung: regulärer Ausdruck `lem\d{6}(\.1?\d{2})?`
- Zeichenkette – Einschränkung: regulärer Ausdruck `org\d{6}(\.\d{2})?`
- Zeichenkette – Einschränkung: regulärer Ausdruck `per\d{6}[abc]?(\.\d{2})?`
- Zeichenkette – Einschränkung: regulärer Ausdruck `loc\d{6}(\.\d{2})?`

### @role

Rolle des Schreibenden

*Mögliche Werte*

- scribe – *Schreiber*

## Beispiele

### Beispiel 1

Angabe des Schreibers eines Stücks mit Erfassung des Personennamens

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <author role="scribe">
        <persName ref="per002336">Adam Böniger</persName>, Landschreiber
                von Glarus
            </author>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)