---
title: note
---



# `<note/>` (Anmerkung)

## Beschreibung

Enthält entweder eine sachkritische Anmerkung zu einer Einzelstelle im Editionstext oder eine Anmerkung im Original. 

## Erläuterung

Ein [`<note/>`](note.md)-Element folgt unmittelbar auf das Bezugswort im Editionstext. Wird Originaltext zitiert, wird dieser mit[`<orig/>`](orig.md)  ausgezeichnet.

Handelt es sich um eine Anmerkung im Original wird das Attribut [@type](#type)  mit dem Wert`original`  verwendet. 

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [ref](ref.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @place

Gibt eine Stelle auf einem Textzeugen gemäß einer fest definierten Liste an. 

*Mögliche Werte*

- above – *oberhalb der Zeile*
- below – *unterhalb der Zeile*
- bottom – *am unteren Rand*
- cover – *auf dem Umschlag*
- cover_above – *auf dem Umschlag oben*
- cover_bottom – *auf dem Umschlag unten*
- cover_middle – *auf dem Umschlag in der Mitte*
- left_margin – *am linken Rand*
- next_page – *auf der nächsten Seite*
- right_margin – *am rechten Rand*
- verso – *auf der Rückseite*

### @type

Art der Anmerkung; wird dieses Attribut nicht vergeben, dann handelt es sich um eine Anmerkung der Editor:innen. 

*Mögliche Werte*

- original – *Anmerkung im Original*

## Beispiele

Keine Beispiele für ausgewählte Sprache vorhanden.

## Abschnitte in den Guidelines der TEI

- [3.9.1. Notes and Simple Annotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONONO)
- [2.2.6. The Notes Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD27)
- [3.12.2.8. Notes and Statement of Language](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICON)
- [9.3.5.4. Notes within Entries](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DI.html#DITPNO)