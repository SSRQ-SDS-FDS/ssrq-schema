---
title: persName
---



# `<persName/>`

## Beschreibung

Zeichnet eine Person aus und umfasst in der Regel nur den Vor- und Nachnamen. 

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @ref

Verknüpfung der Person mit der ID der Personen- und Organisationsdatenbank. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `per\d{6}[abc]?(\.\d{2})?`

### @role

Auszeichnung der Rolle einer Person im Quellentext. 

*Mögliche Werte*

- audentiaprocurator – *Audentiaprokurator*
- biblical – *biblische Figur, keine Heilige*
- computator – *Komputator*
- corrector – *Korrektor*
- issuer – *Aussteller*
- mythological – *mythologische Figur*
- procurator – *Prokurator*
- protonotary – *Protonotar*
- recipient – *Empfänger*
- rescribendary – *Reskribendar*
- saint – *Heilige*
- scribe – *Schreiber*
- sigillant – *Siegler*
- witness – *Zeuge*

## Beispiele

### Beispiel 1

Beispiel für einen einfachen Personennamen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <persName ref="per008949a">Hans Gullisen</persName>
</egXML>
               
```

### Beispiel 2

Auszeichnung eines Heiligen – nur der Name wird erfasst

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
        sant
        <persName ref="per000351">Pauls</persName>
</egXML>
               
```

### Beispiel 3

Verwendung mit [@role](#role)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <persName role="sigillant" ref="per002744a">Johann Jakob Escher</persName>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [13.2.1. Personal Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPER)