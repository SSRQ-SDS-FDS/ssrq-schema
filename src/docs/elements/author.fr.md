---
title: author
---



# `<author/>` (auteur)

## Description

Contient l'auteur d'une publication dans le cadre d'une déclaration bibliographique et l'auteur d'une source dans le cadre de [`<msItem/>`](msItem.md).

## Modèle de contenu

- **namesdates**: [orgName](orgName.md) [persName](persName.md)
- Contenu de texte au choix

## Attributs

### @ref

Référence aux bases de données du SDS.

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `key\d{6}$?`
- Chaîne de caractères – Restriction: expression régulière `lem\d{6}(\.1?\d{2})?`
- Chaîne de caractères – Restriction: expression régulière `org\d{6}(\.\d{2})?`
- Chaîne de caractères – Restriction: expression régulière `per\d{6}[abc]?(\.\d{2})?`
- Chaîne de caractères – Restriction: expression régulière `loc\d{6}(\.\d{2})?`

### @role

Rôle du rédacteur

*Valeurs possibles*

- scribe – *scripteur*

## Exemples

### Exemple 1

Indication de l'auteur d'une pièce avec saisie du nom de la personne

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <author role="scribe">
        <persName ref="per002336">Adam Böniger</persName>, Landschreiber
                von Glarus
            </author>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)