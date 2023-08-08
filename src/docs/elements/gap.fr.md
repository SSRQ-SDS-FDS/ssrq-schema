---
title: gap
---



# `<gap/>` (omission)

## Description

Décrit une omission par l'éditeur.

## Explication

Cela s'applique principalement aux passages complètement illisibles. La raison d'une omission peut être spécifiée avec [@reason](#reason). Cependant, si la cause de l'illisibilité est un dommage,[@reason](#reason)  n'est pas utilisé - à la place, la balise est entourée de[`<damage/>`](damage.md). Si la raison de l'illisibilité est un rasage ou une suppression (lourde), la balise est imbriquée dans un[`<del/>`](del.md).

La taille de l'omission est spécifiée avec [@unit](#unit)  et[@quantity](#quantity). Les mesures sont arrondies vers le haut ou vers le bas à 0,5.

Si les suppléments ultérieurs ne sont pas édités avec l'original mais comme une pièce séparée, les parties qui ont déjà été éditées dans un original antérieur peuvent être omises avec [`<gap/>`](gap.md). La pièce éditée est référencée avec[@source](#source). Dans ce cas, un commentaire est ajouté en[`<note/>`](note.md)  ou en[`<back/>`](back.md).

Pour les sauts de ligne dans le modèle, [`<gap/>`](gap.md)  n'est pas utilisé, mais[`<supplied/>`](supplied.md).

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @quantity

Spécifie la taille de l'unité spécifiée avec [@unit](#unit)

*Valeurs possibles*

- Nombre à virgule flottante
- Nombre
- unknown – *inconnu*

### @reason

Raison de l'écart

*Valeurs possibles*

- illegible – *illisible*
- irrelevant – *insignifiant*
- missing – *manquant*

### @source

Renvoi à une autre pièce (par ex. en cas de livraison multiple) ou à un système d'information archivistique. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `urn:ssrq:(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)(-((([A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)))?(#[A-Za-z0-9_]+)?`
- anyURI – Restriction: expression régulière `(https?|ftp)://[^\s/$.?#].[^\s]*`

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

Exemple d'endroit endommagé où le texte est illisible

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <gap quantity="9" unit="cm" />
    </damage>
</egXML>
               
```

### Exemple 2

Ligne illisible sans rature ou détérioration

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <gap reason="illegible" unit="line" quantity="1.0" />
</egXML>
               
```

### Exemple 3

Trou dans un modèle d'édition pour lequel aucun ajout n'est possible - les mesures sont arrondies à 0,5.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            und sol och der w
            <damage agent="hole">
        <gap unit="cm" quantity="3.5" />
    </damage>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)