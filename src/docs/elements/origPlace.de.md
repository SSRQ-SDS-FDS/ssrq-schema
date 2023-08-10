---
title: origPlace
---



# `<origPlace/>`

## Beschreibung

Enthält den Austellungs- oder Druckort einer Quelle.

## Erläuterung

In [@ref](#ref)  wird mit einer ID (locNNNNNN) auf den Ort in der Ortsdatenbank verwiesen, in der alle Angaben zu einem Ort zu finden sind.

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

Verknüpfung des Ortes mit der ID der Ortsdatenbank. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `loc\d{6}(\.\d{2})?`

## Beispiele

### Beispiel 1

Auszeichnung eines Druckorts

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />Getruckt zuͦ
            <origPlace>Zürich</origPlace>
</egXML>
               
```

### Beispiel 2

Als Teil des Header

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <history>
        <origin>
            <origPlace>Rheineck</origPlace>
        </origin>
    </history>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.3.1. Origination](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdates)