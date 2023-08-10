---
title: q
---



# `<q/>` (séparé du texte environnant par des guillemets)

## Description

Contient du texte au discours direct dans la transcription.

## Explication

 [`<q/>`](q.md)  devient par ex. utilisé dans les déclarations de témoins. Dans l'affichage, la balise est mise en surbrillance avec des guillemets. Les citations et les insertions dans un texte source, en revanche, sont signalées par[`<quote/>`](quote.md).

Lorsqu'une pièce source mentionne le nom d'un document ou d'une prière, elle n'est pas marquée de la balise [`<q/>`](q.md)  ou[`<quote/>`](quote.md), mais le titre est en majuscule. Il en va de même pour les titres d'œuvres historiques dans les paratextes.

Dans les paratextes (notes, commentaires, introduction), la balise [`<q/>`](q.md)  peut être utilisée avec une fonction modalisante, i. e. ironique, distanciant, transféré etc., ou utilisé pour l'emphase.

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

Distinction exemplaire du discours direct

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Der ander spricht:
            <q>Richt mich uß oder
                ich will dirs stellen bey der buß.
            </q>
</egXML>
               
```

### Exemple 2

Mise en évidence dans les paratextes éditoriaux (commentaires, introduction, etc.)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Der Buchstabe <q>v</q> wird in vokalischer
            Position stets als <q>u</q> transkribiert.
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [3.3.3. Quotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQQ)