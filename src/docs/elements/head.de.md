---
title: head
---



# `<head/>` (Überschrift)

## Beschreibung

Enthält eine Überschrift oder einen Titel.

## Erläuterung

Enthält als Teil des [`<teiHeader/>`](teiHeader.md)  den Titel des Dokuments und als Teil von[`<listBibl/>`](listBibl.md)  die Beschreibung des zitierten Kurztitels; in[`<body/>`](body.md)  die Überschrift eines Kapitels oder Unterkapitels, in[`<figure/>`](figure.md)  die Legende einer Abbildung, einer Graphik, eines Stammbaumes etc.

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @hand

Enthält einen Verweis auf die ID eines [`<handNote/>`](handNote.md)-Element, das im[`<teiHeader/>`](teiHeader.md)  deklariert wurde.

*Mögliche Werte*

- Verweis auf Identifikator

### @n



*Mögliche Werte*

- Zeichenkette

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
- inline – *auf Zeilenhöhe*
- interlinear – *zwischen zwei Zeilen*
- left_top – *am linken oberen Rand*
- opposite – *auf der gegenüberliegenden Seite*
- overwritten – *überschrieben*
- previous_page – *auf der vorherigen Seite*
- right_top – *am rechten oberen Rand*
- top – *am oberen Rand*

### @resp



*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

### @type



*Mögliche Werte*

- title – *Haupttitel*
- subtitle – *Untertitel*
- subsubtitle – *Unteruntertitel*

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

Beispiel für eine Überschrift in einer Tabelle

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <table>
        <head>Von dem wein</head>
        <row>
            <cell />
            <cell role="label">gbz</cell>
            <cell role="label">xr</cell>
            <cell role="label">₰</cell>
        </row>
        <row>
            <cell>für j saum wein</cell>
            <cell>–</cell>
            <cell>1</cell>
            <cell>–</cell>
        </row>
        <pb />
        <head>item</head>
        <row>
            <cell>für j lägelen wein</cell>
            <cell>–</cell>
            <cell>–</cell>
            <cell>2</cell>
        </row>
    </table>
</egXML>
               
```

### Beispiel 2

Beispiel für eine Überschrift einer Graphik

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

### Beispiel 3

Titel, der vom Bearbeitenden zur besseren Strukturierung des Texts hinzugefügt wird

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <head resp="PS">Erbrecht</head>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4.2.1. Headings and Trailers](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSHD)