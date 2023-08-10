---
title: placeName
---



# `<placeName/>`

## Beschreibung

Zeichnet topographische Bezeichnungen (einen Ort oder einen Flurnamen) aus. 

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

Erfassung eines (historischen) Ortsnamens (mit Verweis auf die SSRQ-Datenbank)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <placeName ref="loc000284">Freiburg</placeName>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [13.2.3. Place Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPLAC)