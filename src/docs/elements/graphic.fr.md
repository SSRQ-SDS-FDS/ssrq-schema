---
title: graphic
---



# `<graphic/>`

## Description

Contient des informations sur une image ou une illustration graphique faisant partie du texte ou référence externe. 

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @mimeType

MimeType du fichier d'image intégré

*Valeurs possibles*

- image/jpg
- image/png
- image/svg

### @type

Type de graphique

*Valeurs possibles*

- familytree – *pédigrée*
- figure – *visualisation*
- graphic – *illustration*
- map – *carte*

### @url

Lien vers un fichier image.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

## Exemples

### Exemple 1

Exemple d'arbre généalogique

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

### Exemple 2

Définition du numéro d'identification de la pièce:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <graphic type="graphic" mimeType="image/jpg" url="SSRQ-FR-I_2_8-graphic-6.jpg" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.10. Graphics and Other Non-textual Components](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COGR)
- [11.1. Digital Facsimiles](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHFAX)