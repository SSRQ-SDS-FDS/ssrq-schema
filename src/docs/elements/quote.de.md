---
title: quote
---



# `<quote/>`

## Beschreibung

Enthält ein Zitat innerhalb eines Originaltextes.

## Erläuterung

Enthält z. B. eine inserierte Urkunde oder eine Bibelstelle. Idealerweise folgt am Schluss des Zitats eine sachkritische Anmerkung mit [`<note/>`](note.md)  mit einem Verweis auf den Originaltext oder eine Edition desselben.

Für direkte Rede in Quellentexten verwenden wir [`<q/>`](q.md). Wird in einem Quellenstück der Name eines Dokuments oder eines Gebets genannt, dann wird dieses nicht mit dem Tag q oder quote ausgezeichnet, aber der Titel grossgeschrieben. Das Gleiche gilt für historische Werktitel innerhalb der Paratexte. Innerhalb der Paratexte (Anmerkungen, Kommentar, Einleitung) benutzen wir[`<quote/>`](quote.md)  für Zitate aus der Forschungsliteratur.

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

Exemplarischer Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Originaltext enthält
            <quote>Bibelzitat</quote>
            .
            <note>[Belegstelle]</note>
</egXML>
               
```

### Beispiel 2

Zitat einer im Originaltext inserierten Urkunde

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <add place="below" hand="otherHand">Hinfûr soll man leßen des banholtzes halb ein
                gschrift, stât ze end dis buchs, fahent an:
                <quote>Wir Johannes Mantss.</quote>
        <note>Mit
                    dem Verweis betreffend Bannholz ist StAZH G I 102, fol. 33r-v gemeint.
                </note>
    </add>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.3.3. Quotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQQ)
- [4.3.1. Grouped Texts](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSGRP)