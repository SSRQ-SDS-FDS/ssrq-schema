---
title: idno
---



# `<idno/>` (Numéro d'identification)

## Description

Contient un UUID en [`<seriesStmt/>`](seriesStmt.md)  (avec[@type](#type)  =` UUID` ), l'abréviation de volume (canton, partie, numéro d'article) de la collection des sources juridiques suisses ou contient dans [`<msIdentifier/>`](msIdentifier.md)  la signature d'archive d'une source.

## Explication

Si [`<idno/>`](idno.md)  contient la signature d'une archive, elle doit être conforme au système de l'archive respective.

Si [`<idno/>`](idno.md)  contient un UUID, alors il doit correspondre à l'expression régulière suivante:`^[0-9A-Fa-f]{8}-[0-9A-Fa - f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$`. L'UUID est structuré comme suit: 

- Exactement huit caractères parmi l'ensemble suivant: les chiffres "0-9", les lettres majuscules "A-F" ou les lettres minuscules "a-f". 
- Un trait d'union.
- Exactement quatre caractères de l'ensemble ci-dessus.
- Un trait d'union.
- Le chiffre "4" suivi de trois caractères du jeu ci-dessus.
- Un trait d'union.
- Exactement un caractère du jeu suivant: "8", "9", "A", "B", "a", "b" suivi d'exactement trois caractères de l'ensemble ci-dessus. 
- Un trait d'union.
- Exactement douze caractères de l'ensemble ci-dessus.

Contient [`<idno/>`](idno.md)  a abréviation de bande du SSRQ, cela doit correspondre à l'expression régulière suivante:`^(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)-(?: ( (?:[A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)|([a-z]{3,}))$`. Les abréviations de bande sont structurées comme suit: 

- Le préfixe "SSRQ" ou "SDS" ou "FDS".
- Un trait d'union.
- L'abréviation du canton composé de deux lettres majuscules.
- Un trait d'union.
- Une abréviation du volume composée d'un nombre quelconque de lettres majuscules, de lettres minuscules, de chiffres et de traits de soulignement. 
- Un trait d'union.
- La division du chapitre du volume (facultatif) consistant en un nombre quelconque de lettres majuscules, minuscules, chiffres et points. 
- Une abréviation de la pièce composée d'un nombre quelconque de chiffres.
- Un trait d'union.
- Un identifiant final composé d'un nombre quelconque de chiffres ou d'au moins trois lettres minuscules (par exemple B. pour nommer une pièce spéciale comme "lit", "intro" ou "huissier"). 

## Modèle de contenu

- Contenu de texte au choix

## Attributs

### @source

Renvoi à une autre pièce (par ex. en cas de livraison multiple) ou à un système d'information archivistique. 

*Valeurs possibles*

- anyURI – Restriction: expression régulière `(https?|ftp)://[^\s/$.?#].[^\s]*`

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- uuid – *Universally Unique Identifier*

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

Définition du numéro d'identification d'une pièce:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seriesStmt>
        <title>Sammlung Schweizerischer Rechtsquellen</title>
        <respStmt>
            <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
            <resp>Herausgabe</resp>
        </respStmt>
        <idno>SSRQ-FR-I_2_8-1-1</idno>
        <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
    </seriesStmt>
</egXML>
               
```

### Exemple 2

Référence à une cote avec lien vers le système d'information des archives:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <idno xml:lang="de" source="http://scope.stiftsarchiv.sg.ch/detail.aspx?id=30146">StiASG Urk. GG2 T2
                </idno>
    </msIdentifier>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [13.3.1. Basic Principles](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPERSbp)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)
- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)