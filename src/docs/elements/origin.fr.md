---
title: origin
---



# `<origin/>` (origine)

## Description

Contient des informations sur l'origine d'un document.

## Modèle de contenu

- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)

## Attributs

### @xml:lang

ISO-639-1-Abréviation de la langue

*Valeurs possibles*

- de – *Allemand*
- fr – *Français*
- he – *Hébreu*
- it – *Italien*
- la – *Latin*
- rm – *Romanche*

## Exemples

### Exemple 1

Saisie de l'origine et de la datation

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <origin>
        <origDate when-custom="1366-06-29" calendar="julian" />
        <origPlace>Rheineck</origPlace>
    </origin>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.8. History](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mshy)