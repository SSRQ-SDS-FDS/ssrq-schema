---
title: signed
---



# `<signed/>`

## Description

Comprend des signatures et des signatures avec des marques de notaire et se trouve généralement à la fin d'un texte. 

## Explication

Si une signature est suivie de divers commentaires ([`<ab/>`](ab.md) ), alors[`<signed/>`](signed.md)  doit être dans un[`<div/>`](div.md).

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

## Exemples

### Exemple 1

Exemple de signature avec marque de notaire

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <signed>
        <figure type="notarial_sign" />
        <lb />Et ego Hainricus Jacobi de Augiamaiori ...
        </signed>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [4.2.2. Openers and Closers](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSOC)