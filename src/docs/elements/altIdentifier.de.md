---
title: altIdentifier
---



# `<altIdentifier/>`

## Beschreibung

Enthält eine alte Archivsignatur.

## Inhaltsmodell

- **header**: [idno](idno.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <repository xml:lang="de">Landesarchiv Glarus</repository>
        <idno source="https://archivverzeichnis.gl.ch/home/#/content/2c27b48bc9864c45b3ae7d3dbeb9747f" xml:lang="de">LAGL AG III.2465:008
                </idno>
        <altIdentifier>
            <idno>LAGL I. 9h.</idno>
        </altIdentifier>
    </msIdentifier>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.4. The Manuscript Identifier](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msid)