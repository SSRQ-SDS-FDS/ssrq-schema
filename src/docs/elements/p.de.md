---
title: p
---



# `<p/>` (Absatz)

## Beschreibung

Beschreibt einen Absatz.

## Erläuterung

In der Transkription werden damit originale Absätze ausgezeichnet. Eine inhaltliche Gliederung des Textes durch den Bearbeitenden erfolgt mit [`<seg/>`](seg.md). Vgl. dazu auch die Ausführungen "Strukturierung der Texte" in den SSRQ-Transkriptionsrichtlinien und die Beschreibung von[`<div/>`](div.md). Wird in einer Urkunde der Text durch einen Abstand oder eine Initiale inhaltlich strukturiert, kann der Absatz mit[`<p/>`](p.md)  ausgezeichnet werden. Paragraphenzeichen allerdings werden nicht speziell ausgezeichnet.

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [list](list.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [ref](ref.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @xml:lang

ISO-639-1-Sprachkürzel

*Mögliche Werte*

- de – *Deutsch*
- fr – *Französisch*
- he – *Hebräisch*
- it – *Italienisch*
- la – *Latein*
- rm – *Bündnerromanisch*

## Beispiele

### Beispiel 1

Beispielhafte Verwendung in Kombination mit seg

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <seg>
            <lb />Man sol ôch zuͦ den selben meyen oder herbst taͤding richten<lb />umb
                    eigen oder umb erb und von keiner sunderbaren sache,<lb />es sy denn beider teil
                    wille.
                </seg>
    </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.1. Paragraphs](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COPA)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)