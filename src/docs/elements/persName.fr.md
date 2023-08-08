---
title: persName
---



# `<persName/>` (nom de personne)

## Description

Distingue une personne et ne comprend généralement que le prénom et le nom. 

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

Relier la personne à l'ID de la base de données des personnes et des organisations. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `per\d{6}[abc]?(\.\d{2})?`

### @role

Distinction du rôle d'une personne dans le texte source. 

*Valeurs possibles*

- audentiaprocurator – *audentiaprokurator*
- biblical – *personnage biblique, mais pas un saint*
- computator – *computateur*
- corrector – *correcteur*
- issuer – *personne qui a fait un acte*
- mythological – *personnage mythologique*
- procurator – *procurateur*
- protonotary – *protonotaire*
- recipient – *personne qui a reçu l’acte*
- rescribendary – *reskribendar*
- saint – *saint*
- scribe – *scripteur*
- sigillant – *personne qui a posé un sceau*
- witness – *témoin d’une liste de témoins*

## Exemples

### Exemple 1

Exemple de nom de personne

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <persName ref="per008949a">Hans Gullisen</persName>
</egXML>
               
```

### Exemple 2

Marquage d'un saint

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
        sant
        <persName ref="per000351">Pauls</persName>
</egXML>
               
```

### Exemple 3

Utilisation avec [@role](#role)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <persName role="sigillant" ref="per002744a">Johann Jakob Escher</persName>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [13.2.1. Personal Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPER)