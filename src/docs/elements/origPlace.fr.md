---
title: origPlace
---



# `<origPlace/>` (lieu de création)

## Description

Contient le lieu d'émission ou d'impression d'une source.

## Explication

Dans [@ref](#ref), un ID (locNNNNNN) fait référence au lieu dans la base de données des lieux, dans laquelle toutes les informations sur un lieu peuvent être trouvées.

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

Distinction d'un lieu d'impression

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />Getruckt zuͦ
            <origPlace>Zürich</origPlace>
</egXML>
               
```

### Exemple 2

Dans le cadre de l'en-tête

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <history>
        <origin>
            <origPlace>Rheineck</origPlace>
        </origin>
    </history>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.3.1. Origination](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdates)