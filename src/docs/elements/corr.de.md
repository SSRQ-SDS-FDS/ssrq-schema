---
title: corr
---



# `<corr/>` (Korrektur)

## Beschreibung

Enthält eine durch einen Editor vorgenommene Korrektur.

## Erläuterung

Enthält die korrekte Form zum Beispiel eines Verschreibers, der mit [`<sic/>`](sic.md)  kenntlich gemacht wird. Die Korrektur stammt immer vom Editor und nicht aus der Hand des Schreibers des Dokuments. Bei irrtümlichen Wiederholungen von Wörtern enthält[`<corr/>`](corr.md)  die korrekte Form. Ein leeres[`<corr/>`](corr.md)  ist möglich, wenn ein überflüssiges Wort durch den Editor getilgt wird.

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

### @resp



*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

## Beispiele

### Beispiel 1

Beispiel für eine Korrektur.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <sic>digintates</sic>
        <corr>dignitates</corr>
    </choice>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5.1. Apparent Errors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDCOR)