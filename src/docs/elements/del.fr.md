---
title: del
---



# `<del/>` (suppression)

## Description

Contient du texte effacé par un scribe.

## Explication

Avec [`<del/>`](del.md), aucune suppression provenant de l'éditeur n'est marquée, seules celles qui se trouvent dans la source. Si le texte est supprimé plusieurs fois ou si les suppressions franchissent les limites hiérarchiques,[`<delSpan/>`](delSpan.md)  et[`<anchor/>`](anchor.md)  doivent être utilisés.

Les rasages sont marqués avec l'attribut [@rend](#rend)  =`rubbing`. Si rien n'est lisible après le rasage ou les coups lourds, un [`<gap/>`](gap.md)  vide est utilisé dans[`<del/>`](del.md).

L'attribut [@hand](#hand)  est utilisé pour les traits avec une autre encre. Dans les interventions textuelles ultérieures (suppression avec correction),[@hand](#hand)  se trouve à[`<add/>`](add.md)  dans[`<subst/>`](subst.md).

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

### @rend

Indique comment l'élément en question a été rendu ou présenté dans le texte source

*Valeurs possibles*

- blackened – *caviardage*
- bracketed – *la suppression se trouve entre parenthèses*
- crossout – *suppression en croisant la ligne*
- overwritten – *la suppression a été remplacée directement*
- rubbing – *suppression par grattage*
- strikethrough – *suppression par biffage*
- subpunction – *suppression par exponctuation*
- underline – *la suppression a été soulignée*

## Exemples

### Exemple 1

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