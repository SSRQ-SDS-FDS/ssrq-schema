---
title: cell
---



# `<cell/>` (cellule)

## Description

Décrit une cellule dans un tableau.

## Explication

Est requis dans [`<table/>`](table.md)  avec[`<row/>`](row.md)  (ligne) pour afficher les tableaux. Avec[@role](#role)  =`label`  un en-tête de colonne, par ex. B. une devise d'une entrée de colonne spécifiée. 

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

### @rend

Alignement du texte dans une cellule de tableau du document source

*Valeurs possibles*

- align-bottom – *Aligné au bas de la cellule*

### @role

Utilisation particulière d'une cellule de tableau 

*Valeurs possibles*

- label – *en-tête de colonne*

## Exemples

### Exemple 1

Exemple simple de cellules dans un tableau

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