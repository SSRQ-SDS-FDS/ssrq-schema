---
title: msIdentifier
---



# `<msIdentifier/>`

## Beschreibung

Beschreibt den aktuellen und ehemalige Aufbewahrungsorte der Quelle. 

## Inhaltsmodell

- **header**: [idno](idno.md)
- **msdescription**: [altIdentifier](altIdentifier.md) [repository](repository.md)
- **namesdates**: [settlement](settlement.md)

## Beispiele

### Beispiel 1

Beispielhafte Verwendung des Elements tei:msIdentifier

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <repository xml:lang="de">Staatsarchiv Schwyz</repository>
        <idno xml:lang="de">StASZ, Urk. 190</idno>
    </msIdentifier>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.4. The Manuscript Identifier](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msid)