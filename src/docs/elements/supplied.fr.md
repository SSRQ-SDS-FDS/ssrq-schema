---
title: supplied
---



# `<supplied/>` (texte restitué)

## Description

Contient un ajout de l'éditeur.

## Explication

Si un éditeur ajoute librement un passage, il s'identifie en [@resp](#resp)  avec son abréviation. Si un texte est complété à l'aide d'un autre modèle de texte, celui-ci est référencé par[@source](#source). La raison d'un ajout peut être spécifiée avec[@reason](#reason). Une note dans[`<note/>`](note.md)  ou un commentaire dans[`<back/>`](back.md)  est requis.

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

### @reason

Raison de l'ajout

*Valeurs possibles*

- omitted – *omis*

### @resp

Indique l'agent responsable de l'intervention ou de l'interprétation, par exemple un éditeur ou un transcripteur.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

### @source

Renvoi à une autre pièce (par ex. en cas de livraison multiple) ou à un système d'information archivistique. 

*Valeurs possibles*

- Référence à l'identifiant

## Exemples

### Exemple 1

Exemple d'ajout

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <lb />Item so sollend die <supplied reason="omitted" resp="rhr">von</supplied> Mure,
        <lb /> von Bintz und von Egmatingen den weg gen.
    </p>
</egXML>
               
```

### Exemple 2

Exemple de passage endommagé dont le texte a été ajouté

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <supplied source="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">verthruwen</supplied>
    </damage>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)