---
title: space
---



# `<space/>` (espace)

## Description

Désigne une lacune que l'auteur a délibérément laissée ouverte pour une réalisation ultérieure. 

## Explication

La taille de l'écart doit être spécifiée avec [@unit](#unit)  et[@quantity](#quantity). C'est une tag vide. Les lacunes dues à des sauts de ligne involontaires, en revanche, sont marquées par[`<supplied/>`](supplied.md).

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @quantity

Spécifie la taille de l'unité spécifiée avec [@unit](#unit)

*Valeurs possibles*

- Nombre à virgule flottante
- Nombre
- unknown – *inconnu*

### @resp



### @unit

Unité de mesure

*Valeurs possibles*

- cm – *cm*
- line – *ligne*
- character – *lettre*
- page – *page*
- word – *mot*

## Exemples

### Exemple 1

Exemple d'un espace libre de 5 cm

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <space quantity="5" unit="cm" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.4.1. Space](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHSP)