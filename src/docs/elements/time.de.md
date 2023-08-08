---
title: time
---



# `<time/>` (Zeit)

## Beschreibung

Enthält eine Zeitangabe.

## Erläuterung

Mithilfe der zugelassenen Attribute können die Angaben in einem normalisierten Format maschinenlesbar ausgedrückt werden. Das Format ist die vom W3C definierte Untermenge von ISO 8601. Zeitpunkte werden mit [@when-custom](#when-custom)  bzw.[@notBefore-custom](#notBefore-custom)  und[@notAfter-custom](#notAfter-custom)  angegeben, Zeiträume mit[@from-custom](#from-custom)  und[@to-custom](#to-custom). Zeitspannen ohne Angabe von Anfang und Ende können mit[@dur-iso](#dur-iso)  näher bezeichnet werden. Unbestimmte Tageszeiten, wie z. B. nachts, werden mit[@period](#period)  getaggt.

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

### @dur-iso

Erfassung Zeitspanne nach [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen). Beginnt mit dem Kürzel P (Periode) gefolgt T (Time) und arabischen Ziffern. Sich wiederholende Zeitspannenden werden im vollen Format ausgedrückt und beginnen mit dem Kürzel R (Repeated). Ansonsten werden folgende Werte vergeben

- H = hour
- M = minute
- S = second

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(R/)?PT(\d+(\.\d+)?[HMS])+`

### @from-custom

Gibt den Startpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @notAfter-custom

Gibt den Endpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @notBefore-custom

Gibt den Startpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @period

Verweist auf eine benannte Periode wie Jahreszeiten oder Wochentage. Für Zeitspannen wie „vier Wochen“ wird hingegen das Attribut [@dur-iso](#dur-iso)  verwendet.

*Mögliche Werte*

- afternoon – *nachmittags*
- byNight – *nachts*
- byDay – *tags*
- evening – *abends*
- morning – *morgens*
- noon – *mittags*

### @to-custom

Gibt den Endpunkt eines Zeitraums gemäss ISO 8601 an. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @when-custom

Gibt ein Datum gemäss ISO 8601 an.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

## Beispiele

### Beispiel 1

Erfassung eines Zeitpunkts

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <time when-custom="08:48:00">8 Uhr 48</time>
</egXML>
               
```

### Beispiel 2

Erfassung von Zeitperioden, die nicht mit ISO 8601 beschrieben werden können

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            ...
            <time period="byNight">nachtz</time>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.6.4. Dates and Times](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONADA)