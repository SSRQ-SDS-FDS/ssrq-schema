---
title: text
---



# `<text/>` (texte)

## Description

Contient tous les signes qui se trouvent physiquement sur une pièce source ou un livre (transcription / édition, cet-à-dire données primaires) ainsi que le commentaire de la pièce éditée. 

## Modèle de contenu

- **textstructure**: [back](back.md) [body](body.md)

## Attributs

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- summary – *Enregistrement du document source*
- transcript – *Transcription du document source*

## Exemples

### Exemple 1

Exemple de transcription avec une section de commentaires facultative

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <text type="transcript">
        <body>
                ...
            </body>
        <back>
                ...
            </back>
    </text>
</egXML>
               
```

### Exemple 2

Exemple de registre sans section de commentaire

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <text type="summary">
        <body>
                ...
            </body>
    </text>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)
- [15.1. Varieties of Composite Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCDEF)