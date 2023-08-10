---
title: note
---



# `<note/>`

## Description

Contient soit un commentaire factuel sur un seul passage du texte de l'édition, soit un commentaire dans l'original. 

## Explication

Un élément [`<note/>`](note.md)  suit immédiatement le mot de référence dans le texte de l'édition. Si le texte original est cité, il est marqué avec[`<orig/>`](orig.md).

S'il s'agit d'une annotation dans l'original, l'attribut [@type](#type)  avec la valeur`original`  est utilisé. 

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [ref](ref.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

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

### @type

Type d'annotation; si cet attribut n'est pas attribué, il s'agit d'une annotation de l'éditeur. 

*Valeurs possibles*

- original – *note dans l'original*

## Exemples

Aucun exemple pour la langue sélectionnée.

## Sections des Guidelines de la TEI

- [3.9.1. Notes and Simple Annotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONONO)
- [2.2.6. The Notes Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD27)
- [3.12.2.8. Notes and Statement of Language](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICON)
- [9.3.5.4. Notes within Entries](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DI.html#DITPNO)