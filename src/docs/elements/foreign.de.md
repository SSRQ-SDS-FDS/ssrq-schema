---
title: foreign
---



# `<foreign/>` (fremd)

## Beschreibung

Enthält Text, der in einer anderen Sprache als der Haupttext vorliegt. 

## Erläuterung

«Actum», «datum» oder «etc.» werden nicht mit [`<foreign/>`](foreign.md)  ausgezeichnet. Längere fremdsprachige Textpassagen werden zusätzlich auch in den Metadaten unter[`<textLang/>`](textLang.md)  vermerkt. Handelt es sich um einen anderweitig mit einem TEI-Element kennzeichenbaren Satzbestandteil, ist das entsprechende Element mit[@xml:lang](#xml:lang)  zu versehen. Beispielsweise wird bei einem fremdsprachigen Buchtitel[`<title/>`](title.md)  mit[@xml:lang](#xml:lang)  verwendet.

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

Absatz mit fremdsprachigen Einschüben

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>Versigleter <foreign xml:lang="rm">scütt</foreign> entzwischen der gmeindt Langnetz
                und der gmeind Fallß <foreign xml:lang="la">ut jntus</foreign> zu sechen.
            </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.3.2.1. Foreign Words or Expressions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQHF)