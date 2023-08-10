---
title: msItem
---



# `<msItem/>`

## Beschreibung

Enthält Informationen über die einzelnen Teile einer Quelle.

## Erläuterung

Die Textsprachen der Quelle werden mit [`<textLang/>`](textLang.md)  angeben. Bei Handschriften können die Autoren mit[`<author/>`](author.md)  angegeben werden, bei Druckschriften können innerhalb von[`<docImprint/>`](docImprint.md)  der Druckort und die Druckerei angegeben werden.

## Inhaltsmodell

- **core**: [author](author.md) [textLang](textLang.md)
- **textstructure**: [docImprint](docImprint.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msItem>
        <textLang xml:lang="de" />
    </msItem>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.6.1. The msItem and msItemStruct Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mscoit)