---
title: dimensions
---



# `<dimensions/>` (dimensions)

## Description

Dimensions d'une source

## Explication

Si [@type](#type)  a la valeur`plica`  alors un seul élément [`<width/>`](width.md)  est autorisé comme contenu.

## Modèle de contenu

- **msdescription**: [height](height.md) [width](width.md)

## Attributs

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- leaves
- plica

## Exemples

### Exemple 1

Structure modèle

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <extent>
        <dimensions type="leaves">
            <height unit="cm" quantity="16.0" />
            <width unit="cm" quantity="23.0" />
        </dimensions>
        <dimensions type="plica">
            <width unit="cm" quantity="4.0" />
        </dimensions>
    </extent>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)