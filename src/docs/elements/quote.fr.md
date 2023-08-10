---
title: quote
---



# `<quote/>` (citation)

## Description

Contient une citation dans un texte original.

## Explication

Contient par ex. un document annoncé ou un passage de la Bible. Idéalement, la citation doit être suivie d'un commentaire factuel avec [`<note/>`](note.md)  avec une référence au texte original ou à une édition de celui-ci.

Pour la parole directe dans les textes sources, nous utilisons [`<q/>`](q.md). Si le nom d'un document ou d'une prière est mentionné dans une pièce source, cela n'est pas marqué avec la balise q ou une citation, mais le titre est en majuscule. Il en va de même pour les titres d'œuvres historiques dans les paratextes. Dans les paratextes (notes, commentaire, introduction), nous utilisons[`<quote/>`](quote.md)  pour les citations de la littérature de recherche.

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

Structure exemplaire

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Originaltext enthält
            <quote>Bibelzitat</quote>
            .
            <note>[Belegstelle]</note>
</egXML>
               
```

### Exemple 2

Citation d'un document inséré dans le texte original

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <add place="below" hand="otherHand">Hinfûr soll man leßen des banholtzes halb ein
                gschrift, stât ze end dis buchs, fahent an:
                <quote>Wir Johannes Mantss.</quote>
        <note>Mit
                    dem Verweis betreffend Bannholz ist StAZH G I 102, fol. 33r-v gemeint.
                </note>
    </add>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.3.3. Quotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQQ)
- [4.3.1. Grouped Texts](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSGRP)