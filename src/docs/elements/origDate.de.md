---
title: origDate
---



# `<origDate/>`

## Beschreibung

Enthält Originaldaten des edierten Quellentexts (Ausstellungdatum). 

## Erläuterung

Es können auch mehrere Originaldatierungen innerhalb einer Editionsvorlage vorhanden sein. Mit [@when-custom](#when-custom)  und[@datingMethod](#datingMethod)  wird das Datum gemäss den Datierungsrichtlinien erfasst. Zum Umgang mit Heiligenfesten und anderen kirchlichen Feiertagen vgl.[`<date/>`](date.md). In den Kommentaren und Anmerkungen wird[`<date/>`](date.md)  verwendet. Das normalisierte Datum eines edierten Stücks wird in den Metadaten erfasst. Der Tag wird in der Retrodigitalisierung für das normalisierte Originaldatum eines Dokuments gemäss den Datierungsrichtlinien verwendet. Bei Regesten muss mit[`<orig/>`](orig.md)  hinter dem normalisierten Datum das Datum in Originalsprache angefügt werden.

## Inhaltsmodell

- **certainty**: [precision](precision.md)
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

### @calendar

Verwendeter Kalender (im Inhalt des Elements)

*Mögliche Werte*

- annunciation – *Annuntiationsstil*
- circumcision – *Circumcisionsstil*
- gregorian – *Gregorianischer Kalender*
- julian – *Julianischer Kalender*
- natal – *Natalstil*
- unknown – *Unbekannt*

### @from-custom

Gibt den Startpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @notAfter-custom

Gibt den Endpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @notBefore-custom

Gibt den Startpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @period

Verweist auf eine benannte Periode wie Jahreszeiten oder Wochentage. Für Zeitspannen wie „vier Wochen“ wird hingegen das Attribut [@dur-iso](#dur-iso)  verwendet.

*Mögliche Werte*

- P1WD – *Sonntag*
- P2WD – *Montag*
- P3WD – *Dienstag*
- P4WD – *Mittwoch*
- P5WD – *Donnerstag*
- P6WD – *Freitag*
- P7WD – *Samstag*
- spring – *Frühling*
- summer – *Sommer*
- fall – *Herbst*
- winter – *Winter*

### @to-custom

Gibt den Endpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @when-custom

Gibt ein Datum gemäss ISO 8601 an.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

## Beispiele

### Beispiel 1

Originaldatierung bei Urkunden

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <origDate when-custom="1448-05-25" calendar="gregorian">uf sant Urbans tag in dem jár,
                do man zalt nach Cristi unsers herren gepurt tusend vierhundert und im acht und
                viertzigosten jâr
            </origDate>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.3.1. Origination](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdates)