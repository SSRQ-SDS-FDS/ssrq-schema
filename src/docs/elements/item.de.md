---
title: item
---



# `<item/>` (Listenpunkt)

## Beschreibung

Enthält einen Listeneintrag.

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

## Beispiele

### Beispiel 1

Einzelner Listeneintrag

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <item>Einzelner Listeneintrag mit beliebigem Inhalt</item>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.8. Lists](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COLI)
- [2.6. The Revision Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD6)