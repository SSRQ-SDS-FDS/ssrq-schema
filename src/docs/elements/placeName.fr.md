---
title: placeName
---



# `<placeName/>` (nom de lieu)

## Description

Distingue les désignations topographiques (un lieu ou un lieu-dit). 

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

### @ref

Relier le lieu à l'ID de la base de données des lieux. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `loc\d{6}(\.\d{2})?`

## Exemples

### Exemple 1

Saisie d'un nom de lieu (historique) (avec référence à la base de données SSRQ)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <placeName ref="loc000284">Frybourg</placeName>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [13.2.3. Place Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPLAC)