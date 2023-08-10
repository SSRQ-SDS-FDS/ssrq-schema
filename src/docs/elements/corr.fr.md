---
title: corr
---



# `<corr/>`

## Description

Contient une correction faite par un éditeur.

## Explication

Contient le formulaire correct, par exemple, d'un prescripteur, identifié par [`<sic/>`](sic.md). La correction vient toujours de l'éditeur et non de la main du rédacteur du document. Pour les répétitions erronées de mots,[`<corr/>`](corr.md)  contient la forme correcte. Un[`<corr/>`](corr.md)  vide est possible si un mot superflu est supprimé par l'éditeur.

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

### @resp

Indique l'agent responsable de l'intervention ou de l'interprétation, par exemple un éditeur ou un transcripteur.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

## Exemples

### Exemple 1

Exemple de correction.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <sic>digintates</sic>
        <corr>dignitates</corr>
    </choice>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5.1. Apparent Errors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDCOR)