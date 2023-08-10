---
title: bibl
---



# `<bibl/>` (bibliografische Angabe)

## Beschreibung

Enthält eine bibliographische Angabe mit Seitenangaben.

## Erläuterung

Das Kindelement [`<ref/>`](ref.md)  verweist auf externe Websites, weitere edierte Stücke oder die Zotero-Literaturdatenbank.

## Inhaltsmodell

- **core**: [ref](ref.md)
- Beliebiger Textinhalt

## Beispiele

### Beispiel 1

Erfassung mit Verweis auf Literaturdatenbank

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="http://zotero.org/groups/5048222/items/M8D9EG5B" />, S. 93
            </bibl>
</egXML>
               
```

### Beispiel 2

Erfassung mit Verweis auf weiteres Stück

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="urn:ssrq:SSRQ-ZH-NF_II_11-74-1">SSRQ ZH NF II/11, Nr. 74</ref>
    </bibl>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.1. Methods of Encoding Bibliographic References and Lists of References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBITY)
- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)
- [15.3.2. Declarable Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAS2)