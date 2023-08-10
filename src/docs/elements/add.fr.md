---
title: add
---



# `<add/>` ( ajout)

## Description

Contient du texte ajouté par un rédacteur.

## Explication

La place de l'addition doit être en [@place](#place)  et la main de la place ajoutée peut être tenue avec la[@main](#main). Si nécessaire,[@rend](#rend)  peut indiquer comment l'ajout (crayon, autre encre, etc.) a été effectué. Si un ajout est la main du premier scribe, alors la main n'est pas spécifiquement notée.

Le problème est le même que dans le cas de [`<del/>`](del.md). Les insertions qui traversent les limites de la hiérarchie doivent être balisées avec[`<addSpan/>`](addSpan.md)  et[`<anchor/>`](anchor.md).

Si un ajout remplace une suppression, [`<subst/>`](subst.md)  doit être utilisé. Aucun supplément ou ajout d'autres témoins de texte n'est marqué avec cela. Il n'est utilisé que pour les ajouts dans le même texte. Un addendum à la fin d'un texte d'une autre main est converti avec[`<add/>`](add.md)  et[`<handShift/>`](handShift.md).

Les titres ajoutés ultérieurement sur les couvertures (livret, double page) ne sont pas en [`<ab/>`](ab.md), mais à l'intérieur d'un[`<head/>`](head.md)  avec[`<add/>`](add.md)  avec[@hand](#hand)  =`otherHand`  indiquant l'emplacement à [@place](#place).

Les ajouts qui sont supprimés doivent être balisés avec des balises combinées, à savoir [`<del/>`](del.md)  contenant un[`<add/>`](add.md)  (et non l'inverse).

Les annotations dorsales claires qui font référence au contenu d'une empreinte et/ou enregistrent sa datation doivent être marquées comme des annotations dorsales avec [`<ab/>`](ab.md). Si, en revanche, il s'agit de plus d'informations, par ex. Pour envoyer le mandat imprimé, des ajouts à des parties individuelles du texte ou des informations non liées à la pièce,[`<add/>`](add.md)  doit être marqué avec[@hand](#hand)  =`otherHand `. 

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

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

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

### @rend

Indique comment l'élément en question a été rendu ou présenté dans le texte source

*Valeurs possibles*

- other_ink – *avec une autre encre*
- pencil – *au crayon*

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- sign – *Ajout signalé par un signe spécial.*

## Exemples

### Exemple 1

Exemple d'une zone endommagée où le texte a été écrit par une autre main

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <add hand="otherHand" place="overwritten">zuͦ trincken</add>
    </damage>
</egXML>
               
```

### Exemple 2

Exemple de remplacement

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <subst>
        <del>zugeschafft</del>
        <add place="above">angethan</add>
    </subst>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)