---
title: title
---



# `<title/>` (titre)

## Description

Contient le titre du volume des sources juridiques ou l'unité d'édition dans le cadre du [`<titleStmt/>`](titleStmt.md), et le titre de la série dans le cadre du[`<seriesStmt/>`](seriesStmt.md).

## Explication

Un titre de livre cité dans une source est également marqué par [`<title/>`](title.md)  et[@xml:lang](#xml:lang).

## Modèle de contenu

- **core**: [hi](hi.md)
- Contenu de texte au choix

## Attributs

### @type

Caractérise le titre selon une typologie adaptée.

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[^\p{C}\p{Z}]+`

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

Titre simple

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <title>Rechtsquellen der Stadt und Herrschaft Rapperswil (mit den Höfen Busskirch/Jona,
                Kempraten und Wagen)
            </title>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)