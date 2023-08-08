---
title: altIdentifier
---



# `<altIdentifier/>` (autre identifiant)

## Description

Contient une ancienne signature d'archive.

## Modèle de contenu

- **header**: [idno](idno.md)

## Exemples

### Exemple 1

Structure modèle

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

## Sections des Guidelines de la TEI

- [10.4. The Manuscript Identifier](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msid)