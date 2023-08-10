---
title: handNote
---



# `<handNote/>` (note sur une main)

## Description

Décrit une main et, le cas échéant, identifie un scribe.

## Modèle de contenu

- **core**: [date](date.md) [p](p.md)

## Attributs

### @n

Donne un nombre (ou une autre étiquette) pour un élément, qui n'est pas nécessairement unique dans le document TEI.

*Valeurs possibles*

- firstHand – *main principale (A)*
- secondHand – *main secondaire (B)*
- thirdHand – *main secondaire (C)*
- fourthHand – *main secondaire (D)*
- fifthHand – *main secondaire (E)*
- sixthHand – *main secondaire (F)*
- seventhHand – *main secondaire (G)*
- eighthHand – *main secondaire (H)*
- ninthHand – *main secondaire (I)*
- laterHand – *d’une main plus récente*
- otherHand – *par une autre main*

### @scribe

Étiquettes de l'écrivain avec le numéro d'identification de la personne. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `per\d{6}[abc]?(\.\d{2})?`

### @xml:id

Fournit un identifiant unique pour l'élément qui porte l'attribut

*Valeurs possibles*

- Identificateur

## Exemples

### Exemple 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <physDesc>
        <handDesc>
            <handNote xml:id="hand1" n="firstHand" scribe="per123456">
                <date from-custom="1001-01-01" to-custom="1100-12-31">
                    <precision precision="low" match="@from-custom" />
                </date>
            </handNote>
            <handNote xml:id="hand2" n="secondHand" />
            <handNote xml:id="hand3" n="otherHand" />
            <handNote xml:id="hand4" n="laterHand" />
        </handDesc>
    </physDesc>
    <delSpan rend="crossout" hand="hand1" spanTo="del1" />
            Item ein hoffstatt ...
            <anchor xml:id="del1" />
    <addSpan place="left_margin" spanTo="add1" hand="hand4" />
            Item ...
            <anchor xml:id="add1" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.2. Writing, Decoration, and Other Notations](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph2)