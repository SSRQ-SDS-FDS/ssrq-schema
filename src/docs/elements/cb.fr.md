---
title: cb
---



# `<cb/>` (Début de colonne)

## Description

Décrit le début d'une nouvelle colonne.

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @n

Contient des informations sur le nombre de colonnes d'origine. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[a-z]{1}`

## Exemples

### Exemple 1

Exemple de démarrage d'une nouvelle colonne.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="1r" />
    <cb n="a" />
    <p>...</p>
    <p>...</p>
    <cb n="b" />
    <p>...</p>
    <p>...</p>
    <pb n="1v" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)