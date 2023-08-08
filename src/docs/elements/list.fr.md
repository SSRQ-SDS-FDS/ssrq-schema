---
title: list
---



# `<list/>` (liste)

## Description

Décrit une liste ou une énumération de tout type.

## Modèle de contenu

- **core**: [item](item.md)

## Attributs

### @rend

Spécification d'affichage de la liste

*Valeurs possibles*

- bulleted – *Liste avec des puces*
- numbered – *Liste numérotée*

### @type



*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[^\p{C}\p{Z}]+`

## Exemples

### Exemple 1

Liste simple sans indication de présentation

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <list>
        <item>Apfel</item>
        <item>Fisch</item>
        <item>...</item>
    </list>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.8. Lists](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COLI)