---
title: supplied
---



# `<supplied/>`

## Beschreibung

Enthält eine Ergänzung durch den Bearbeitenden.

## Erläuterung

Wenn ein Bearbeitender eine Passage frei ergänzt, weist er sich in [@resp](#resp)  mit seinem Kürzel aus. Erfolgt eine Textergänzung anhand einer weiteren Textvorlage, wird auf diese mit[@source](#source)  referenziert. Der Grund für eine Ergänzung kann mit[@reason](#reason)  angegeben werden. Eine Anmerkung in[`<note/>`](note.md)  oder eine Bemerkung in[`<back/>`](back.md)  ist nötig.

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

### @reason

Grund der Ergänzung

*Mögliche Werte*

- omitted – *weggelassen*

### @resp



*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

### @source

Verweis auf ein anderes Stück (bspw. im Falle der Mehrfachüberlieferung) oder auf ein Archivinformationssystem. 

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für eine Ergänzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <lb />Item so sollend die <supplied reason="omitted" resp="rhr">von</supplied> Mure,
        <lb /> von Bintz und von Egmatingen den weg gen.
    </p>
</egXML>
               
```

### Beispiel 2

Beispiel für eine beschädigte Stelle, deren Text ergänzt wurde

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <supplied source="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">verthruwen</supplied>
    </damage>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)