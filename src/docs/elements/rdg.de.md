---
title: rdg
---



# `<rdg/>`

## Beschreibung

Enthält eine von der Editionsvorlage abweichende Textvariante.

## Erläuterung

Der Inhalt von [@wit](#wit)  besteht aus der Archivsignatur des Dokuments oder der Sigle des edierten Stücks, auf dem die Lesart basiert. Nach der Archivsignatur kann nach einem Separator (/) die URL/URI des Dokuments eingefügt werden, wenn es in einem Archivinformationssystem verzeichnet ist. Weisen mehrere Dokumente die gleiche Lesart auf, können auch mehrere Signaturen, getrennt von einem Separator (Strichpunkt), als Wert angegeben werden. Bei Auslassungen kann ein leeres[`<rdg/>`](rdg.md)  verwendet werden.

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

### @wit

Enthält Verweise auf die IDs anderer Textzeugen, die mit [`<witness/>`](witness.md)  im[`<teiHeader/>`](teiHeader.md)  deklariert wurden.

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für einen Apparateintrag

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <app>
        <lem>lxxxvij</lem>
        <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e">
            quadringentesimo
        </rdg>
        <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">lxxxiiij</rdg>
    </app>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [12.1. The Apparatus Entry, Readings, and Witnesses](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TCAPLL)