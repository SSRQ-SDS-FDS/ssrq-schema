---
title: textLang
---



# `<textLang/>` (langues du texte)

## Description

Décrit une langue de texte d'une source.

## Explication

Un élément [`<textLang/>`](textLang.md)  séparé est créé pour chaque langue de texte.

## Modèle de contenu

Ne contient aucun élément ou texte.

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

Exemple simple

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <textLang xml:lang="de" />
</egXML>
               
```

### Exemple 2

Plusieurs langues

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msItem>
        <textLang xml:lang="de" />
        <textLang xml:lang="fr" />
    </msItem>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [10.6.6. Languages and Writing Systems](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mslangs)