---
title: width
---



# `<width/>` (largeur)

## Description

Décrit la largeur d'une feuille ou d'un livre et la largeur du plica. 

## Explication

L'unité de mesure pour [@unit](#unit)  est le centimètre (cm).

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @quantity

Spécifie la taille de l'unité spécifiée avec [@unit](#unit)

*Valeurs possibles*

- Nombre à virgule flottante
- Nombre
- unknown – *inconnu*

### @unit

Unité de mesure

*Valeurs possibles*

- unknown – *inconnu*
- cm – *cm*

## Exemples

### Exemple 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <width unit="cm" quantity="23.0" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)