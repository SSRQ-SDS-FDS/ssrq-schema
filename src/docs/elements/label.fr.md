---
title: label
---



# `<label/>` (étiquette)

## Description

Contient des notes marginales qui sont intégrées dans le texte de l'édition. 

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

Emplacement de la note marginale

*Valeurs possibles*

- left_margin – *dans la marge de gauche*
- right_margin – *dans la marge de droite*

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- keyword – *mot-clé*

## Exemples

### Exemple 1

Indication d'une note marginale

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <label type="keyword" place="left margin">Complices</label>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.8. Lists](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COLI)