---
title: handShift
---



# `<handShift/>` (Changement de main)

## Description

Indique le changement d'une main.

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

## Exemples

### Exemple 1

Exemple de changement de main

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <lb />mutter im leben wär, soll die mutter den dritten
        <handShift hand="otherHand" />
        <lb />theil und die geschwüsterte die zwenn theil erben.
    </p>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.2.1. Document Hands](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDH)