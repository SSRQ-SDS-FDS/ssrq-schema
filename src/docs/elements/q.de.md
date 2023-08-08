---
title: q
---



# `<q/>` (in Anführungszeichen)

## Beschreibung

Enthält in der Transkription Text in direkter Rede.

## Erläuterung

 [`<q/>`](q.md)  wird z. B. bei Zeugenaussagen verwendet. In der Darstellung wird der Tag mit Anführungszeichen hervorgehoben. Zitate und Inserte innerhalb eines Quellentextes werden hingegen mit[`<quote/>`](quote.md)  ausgezeichnet.

Wird in einem Quellenstück der Name eines Dokuments oder eines Gebets genannt, dann wird dieses nicht mit dem Tag [`<q/>`](q.md)  oder[`<quote/>`](quote.md)  ausgezeichnet, aber der Titel gross geschrieben. Das Gleiche gilt für historische Werktitel innerhalb der Paratexte.

Innerhalb der Paratexte (Anmerkungen, Kommentar, Einleitung) kann der Tag [`<q/>`](q.md)  bei modalisierender Funktion, d. h. ironisierend, distanzierend, übertragen etc., oder für Hervorhebungen verwendet werden.

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

Exemplarische Auszeichnung direkter Rede

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Der ander spricht:
            <q>Richt mich uß oder
                ich will dirs stellen bey der buß.
            </q>
</egXML>
               
```

### Beispiel 2

Hervorhebung in editorischen Paratexten (Kommentare, Einleitung, etc.)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Der Buchstabe <q>v</q> wird in vokalischer
            Position stets als <q>u</q> transkribiert.
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.3.3. Quotation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQQ)