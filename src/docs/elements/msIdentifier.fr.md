---
title: msIdentifier
---



# `<msIdentifier/>` (identifiant du manuscrit)

## Description

Décrit les emplacements actuels et historiques de la source. 

## Modèle de contenu

- **header**: [idno](idno.md)
- **msdescription**: [altIdentifier](altIdentifier.md) [repository](repository.md)
- **namesdates**: [settlement](settlement.md)

## Exemples

### Exemple 1

Exemple d'utilisation de l'élément tei:msIdentifier

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <repository xml:lang="de">Staatsarchiv Schwyz</repository>
        <idno xml:lang="de">StASZ, Urk. 190</idno>
    </msIdentifier>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.4. The Manuscript Identifier](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msid)