---
title: listWit
---



# `<listWit/>` (Textzeugenliste)

## Beschreibung

Enthält die Stückbeschreibungen der Quellen.

## Erläuterung

Für jede Quelle wird ein [`<witness/>`](witness.md)  erstellt.

## Inhaltsmodell

- **textcrit**: [witness](witness.md)

## Beispiele

### Beispiel 1

Beispiel für eine Textzeugenliste

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