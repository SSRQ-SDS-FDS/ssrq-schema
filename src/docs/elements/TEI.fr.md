---
title: TEI
---



# `<TEI/>` (Document TEI)

## Description

Contient un seul document (morceau) en tant qu'élément dit root. 

## Explication

La langue du traitement est spécifiée avec [@xml:lang](#xml:lang).

## Modèle de contenu

- **header**: [teiHeader](teiHeader.md)
- **textstructure**: [text](text.md)

## Attributs

### @xml:lang

ISO-639-1-Abréviation de la langue

*Valeurs possibles*

- de
- fr
- it

## Exemples

### Exemple 1

Exemple minimal d'un document TEI

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

## Sections des Guidelines de la TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)
- [15.1. Varieties of Composite Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCDEF)