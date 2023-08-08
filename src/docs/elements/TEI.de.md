---
title: TEI
---



# `<TEI/>` (TEI Dokument)

## Beschreibung

Beinhaltet ein einzelnes Dokument (Stück) als sogenanntes Root-Element. 

## Erläuterung

Mit [@xml:lang](#xml:lang)  wird die Sprache der Bearbeitung angegeben.

## Inhaltsmodell

- **header**: [teiHeader](teiHeader.md)
- **textstructure**: [text](text.md)

## Attribute

### @xml:lang

ISO-639-1-Sprachkürzel

*Mögliche Werte*

- de
- fr
- it

## Beispiele

### Beispiel 1

Minimalbeispiel für ein TEI-Dokument

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <TEI xml:lang="de">
        <teiHeader>
            ...
        </teiHeader>
        <text type="transcript">
            ...
        </text>
    </TEI>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)
- [15.1. Varieties of Composite Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCDEF)