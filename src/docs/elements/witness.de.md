---
title: witness
---



# `<witness/>`

## Beschreibung

Enthält die Stückbeschreibung einer Quelle.

## Inhaltsmodell

- **msdescription**: [msDesc](msDesc.md)

## Attribute

### @n



*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[A-Z][0-9]?`

### @xml:id



*Mögliche Werte*

- Identifikator – Einschränkung: regulärer Ausdruck `id-ssrq-[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}`

## Beispiele

### Beispiel 1

Beispiel für mehrere Textzeugenbeschreibungen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <listWit>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d" n="A">
            <msDesc>
                ...
            </msDesc>
        </witness>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e" n="B">
            <msDesc>
                ...
            </msDesc>
        </witness>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f" n="C">
            <msDesc>
                ...
            </msDesc>
        </witness>
    </listWit>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [12.1. The Apparatus Entry, Readings, and Witnesses](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TCAPLL)