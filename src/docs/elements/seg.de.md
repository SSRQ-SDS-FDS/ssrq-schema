---
title: seg
---



# `<seg/>` (arbiträres Segment)

## Beschreibung

Absätze, die vom Bearbeitenden zur Strukturierung des Quellentextes eingefügt werden. 

## Erläuterung

Innerhalb von [`<p/>`](p.md) verwendet. Dagegen werden[`<div/>`](div.md)  und[`<p/>`](p.md)  nur für originale Absätze verwendet.

Bei längeren Originaltexten wie Offnungen oder Urbarien kann es sinnvoll sein, Artikel, Absätze oder Paragraphen durch [`<seg/>`](seg.md)  mit[@n](#n)  zu nummerieren. Aber bitte keine «Hyperstrukturierung»: Nummerierung nur dort, wo die Struktur des Textes es hergibt (vgl. Beispiele in den gedruckten Bänden der SSRQ). Zur Strukturierung von Schlussformeln siehe die Beispiele auf der Seite Schlussformeln.

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

### @n



*Mögliche Werte*

- Zeichenkette

### @resp



*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

## Beispiele

### Beispiel 1

Beispiel für vom Bearbeitenden eingeführte Absätze

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seg n="1" resp="CS">
        <lb />Item wann man den raut bu̍ttet an ain  unnd welcher dann nit
        <lb />kompt, der gitt zuͦ buͦß ain schilling haller
    </seg>
    <seg n="2" resp="CS">
        <lb />Item so man den raut bu̍ttet an ain marck silbers unnd welcher dann
        <lb />nit kompt, der gitt zuͦ buͦß ii .
    </seg>
    <seg n="3" resp="CS">
        <lb />Item wann man den raut bu̍tet by dem ayd unnd weder von der statt
        <lb />ze ritten noch zuͤ gon, welcher dann nit kompt, der gitt zuͦ buͦß
        <lb />v  haller.
    </seg>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [16.3. Blocks, Segments, and Anchors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SASE)
- [6.2. Components of the Verse Line](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/VE.html#VESE)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)