---
title: table
---



# `<table/>` (tableau)

## Description

Décrit un tableau.

## Explication

Est nécessaire avec [`<row/>`](row.md)  (ligne) et[`<cell/>`](cell.md)  (cellule) pour afficher les tableaux. Il est compté de haut en bas et de gauche à droite. Dans la mesure du possible, un tableau peut être présenté sous forme de texte continu, il ne doit pas être présenté sous forme de tableau. Dans les tableaux et les listes - en particulier dans les mandats imprimés - les guillemets sont utilisés comme traits de soulignement pour répéter des mots ou des chiffres à partir de la ligne supérieure (voir l'exemple ci-dessous). Dans de tels cas, le "Ditto-Mark" (U+0022) est utilisé (à transcrire avec la chaîne de caractères "). Une barre oblique apparaît également dans les tableaux comme valeur nulle (voir exemple ci-dessous). Dans la transcription, le chiffre -tiret demi-cadratin large - (U+2012) utilisé (à translittérer avec la chaîne de caractères ‒).

## Modèle de contenu

- **core**: [head](head.md) [pb](pb.md)
- **figures**: [row](row.md)

## Exemples

### Exemple 1

Exemple d'une liste de prix pour un vin à quatre colonnes, dont les trois dernières colonnes sont intitulées "gbz", "xr" et "dn"

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <table>
        <head>Von dem wein</head>
        <row>
            <cell />
            <cell role="label">gbz</cell>
            <cell role="label">xr</cell>
            <cell role="label">₰</cell>
        </row>
        <row>
            <cell>für j saum wein</cell>
            <cell>–</cell>
            <cell>1</cell>
            <cell>–</cell>
        </row>
        <pb />
        <head>item</head>
        <row>
            <cell>für j lägelen wein</cell>
            <cell>–</cell>
            <cell>–</cell>
            <cell>2</cell>
        </row>
    </table>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [14.1.1. TEI Tables](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/FT.html#FTTAB1)