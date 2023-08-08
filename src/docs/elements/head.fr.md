---
title: head
---



# `<head/>` (en-tête)

## Description

Contient un en-tête ou un titre.

## Explication

Contient le titre du document dans le cadre de [`<teiHeader/>`](teiHeader.md)  et la description du titre abrégé cité dans le cadre de[`<listBibl/>`](listBibl.md); en[`<body/>`](body.md)  le titre d'un chapitre ou d'un sous-chapitre, en[`<figure/>`](figure.md)  la légende d'une illustration, d'un graphique, d'un arbre généalogique etc.

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

### @n

Donne un nombre (ou une autre étiquette) pour un élément, qui n'est pas nécessairement unique dans le document TEI.

*Valeurs possibles*

- Chaîne de caractères

### @place

Indique une position sur un témoin de texte selon une liste fixe. 

*Valeurs possibles*

- above – *au-dessus de la ligne*
- below – *au-dessous de la ligne*
- bottom – *en bas de page*
- cover – *sur la couverture*
- cover_above – *en haut de la couverture*
- cover_bottom – *en bas de la couverture*
- cover_middle – *au milieu de la couverture*
- left_margin – *dans la marge de gauche*
- next_page – *sur la page suivante*
- right_margin – *dans la marge de droite*
- verso – *au verso*
- inline – *à la hauteur de la ligne*
- interlinear – *entre les lignes*
- left_top – *en haut à gauche*
- opposite – *sur la page opposée*
- overwritten – *par-dessus*
- previous_page – *sur la page précédente*
- right_top – *en haut à droite*
- top – *en haut de page*

### @resp

Indique l'agent responsable de l'intervention ou de l'interprétation, par exemple un éditeur ou un transcripteur.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- title – *titre principal*
- subtitle – *sous-titre*
- subsubtitle – *sous-sous-titre*

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

Exemple d'en-tête dans un tableau

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

### Exemple 2

Exemple de titre pour un graphique

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [4.2.1. Headings and Trailers](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSHD)