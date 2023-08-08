---
title: origin
---



# `<origin/>`

## Beschreibung

Enthält Informationen zur Herkunft eines Dokuments.

## Inhaltsmodell

- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)

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

Erfassung der Herkunft und der Datierung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <origin>
        <origDate when-custom="1366-06-29" calendar="julian" />
        <origPlace>Rheineck</origPlace>
    </origin>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.8. History](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mshy)