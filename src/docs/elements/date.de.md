---
title: date
---



# `<date/>` (Datum)

## Beschreibung

Enthält ein Datum im Text des Editors.

## Erläuterung

Datierungen in Quelltexten (Originaldaten) werden mit [`<origDate/>`](origDate.md)  ausgezeichnet. Die Datierungsrichtlinien sind zu beachten.

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

### @datingMethod

Verwendeter Kalender (in den Attributen der Klasse att.datable.custom) 

*Mögliche Werte*

- annunciation – *Annuntiationsstil*
- circumcision – *Circumcisionsstil*
- gregorian – *Gregorianischer Kalender*
- julian – *Julianischer Kalender*
- natal – *Natalstil*
- unknown – *Unbekannt*

### @dur-iso

Erfassung Zeitspanne nach [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen). Beginnt mit dem Kürzel P (Periode) gefolgt von arabischen Ziffern. Sich wiederholende Zeitspannenden werden im vollen Format ausgedrückt und beginnen mit dem Kürzel R (Repeated). Ansonsten werden folgende Werte vergeben

- Y = year
- M = month
- W = week
- D = day
- H = hour

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(R/)?P(\d+(\.\d+)?[YMWDH])+`

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

### @type

Nähere Charakterisierung einer Datierung – wird für Termine und Fristen verwendet sowie für Art der Publikation 

*Mögliche Werte*

- deadline – *Termin/Frist*
- deadline_floating_holiday – *beweglicher Feiertag als Termin/Frist*
- deadline_holiday – *Kirchenfest als Termin/Frist*
- electronic – *elektronische Publikation*
- floating_holiday – *beweglicher Feiertag*
- holiday – *Kirchenfest*
- print – *Druck*

### @when-custom

Gibt ein Datum gemäss ISO 8601 an.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

## Beispiele

### Beispiel 1

Beispielhafte Datierung auf den 03. März 1631

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="gregorian" when-custom="1631-03-03">März, 03, 1631</date>
</egXML>
               
```

### Beispiel 2

Beispielhafte Auszeichnung ca. 1510

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" notBefore-custom="1510-01-01" to-custom="1515-12-31">ca. 1510
            </date>
</egXML>
               
```

### Beispiel 3

Beispielhafte Auszeichnung des Zeitraums Pfingsten 1583 bis Pfingsten 1584

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" from-custom="1583-05-30" to-custom="1584-05-21">von Pfingstmontag 1583 bis Pfingstmontag 1584
            </date>
</egXML>
               
```

### Beispiel 4

Beispielhafte Auszeichnung einer Doppeldatierung. Bei Texten, die doppelt, d. h. nach dem alten und neuen Stil, datiert sind, wird nach dem neuen Stil bzw. dem Gregorianischen Kalender datiert.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date when-custom="1590-10-25" datingMethod="#Gregorian">25/15. octobris anno 90</date>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.6.4. Dates and Times](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONADA)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)
- [2.6. The Revision Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD6)
- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [15.2.3. The Setting Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAHSE)
- [13.4. Dates](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDDATE)