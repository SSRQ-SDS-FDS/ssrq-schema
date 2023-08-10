---
title: textLang
---



# `<textLang/>`

## Beschreibung

Beschreibt eine Textsprache einer Quelle.

## Erläuterung

Für jede Textsprache wird ein eigenes Element [`<textLang/>`](textLang.md)  angelegt.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @xml:lang

ISO-639-1-Sprachkürzel

*Mögliche Werte*

- de – *Deutsch*
- fr – *Französisch*
- he – *Hebräisch*
- it – *Italienisch*
- la – *Latein*
- rm – *Bündnerromanisch*

## Beispiele

### Beispiel 1

Einfaches Beispiel

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <textLang xml:lang="de" />
</egXML>
               
```

### Beispiel 2

Mehrere Sprachen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msItem>
        <textLang xml:lang="de" />
        <textLang xml:lang="fr" />
    </msItem>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [10.6.6. Languages and Writing Systems](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mslangs)