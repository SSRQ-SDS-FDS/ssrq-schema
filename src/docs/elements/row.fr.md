---
title: row
---



# `<row/>` (rangée)

## Description

Décrit une ligne d'un tableau.

## Explication

Est nécessaire avec [`<table/>`](table.md)  (table) et[`<cell/>`](cell.md)  (cellule) pour afficher les tableaux.

## Modèle de contenu

- **core**: [measureGrp](measureGrp.md)
- **figures**: [cell](cell.md)

## Exemples

### Exemple 1

Exemple simple de lignes dans un tableau

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