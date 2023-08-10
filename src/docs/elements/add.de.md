---
title: add
---



# `<add/>` (Hinzufügung)

## Beschreibung

Enthält Text, der von einem Schreiber hinzugefügt wurde.

## Erläuterung

Der Ort der Ergänzung muss zwingend in [@place](#place)  und die Hand der ergänzten Stelle kann mit[@hand](#hand)  festgehalten werden. Falls notwendig, kann innerhalb von[@rend](#rend)  angegeben werden, wie die Ergänzung (mit Bleistift, anderer Tinte etc.) vorgenommen wurde. Handelt es sich bei einer Ergänzung um die Hand des ersten Schreibers, dann wird die Hand nicht speziell angemerkt.

Es besteht die gleiche Problemlage wie im Fall von [`<del/>`](del.md). Einfügungen, die Hierarchiegrenzen überschreiten, müssen mit[`<addSpan/>`](addSpan.md)  und[`<anchor/>`](anchor.md)  ausgezeichnet werden.

Ersetzt eine Hinzufügung eine Streichung, sollte [`<subst/>`](subst.md)  verwendet werden. Damit werden keine Nachträge bzw. Zusätze aus anderen Textzeugen ausgezeichnet. Es wird nur für Hinzufügungen im selben Text verwendet. Ein Nachtrag am Schluss eines Textes von anderer Hand wird mit[`<add/>`](add.md)  und[`<handShift/>`](handShift.md)  umgesetzt.

Nachträglich hinzugefügte Titel auf Umschlägen (Heft, Doppelblatt) werden nicht in [`<ab/>`](ab.md), sondern innerhalb eines[`<head/>`](head.md)  mit[`<add/>`](add.md)  mit[@hand](#hand)  =`otherHand`  unter Angabe des Ortes in [@place](#place)  erfasst.

Hinzufügungen, die gestrichen werden, müssen mit kombinierten Tags ausgezeichnet werden, und zwar mit [`<del/>`](del.md), das ein[`<add/>`](add.md)  enthält (und nicht anders herum).

Klare Dorsualvermerke, die einen Verweis auf den Inhalt eines Drucks machen und/oder dessen Datierung aufnehmen, sind als Dorsualvermerke mit [`<ab/>`](ab.md)  zu taggen. Handelt es sich hingegen um weitere Informationen z. B. zur Versendung des gedruckten Mandats, Ergänzungen zu einzelnen Textteilen oder nicht mit dem Stück zusammenhängende Informationen ist[`<add/>`](add.md)  mit[@hand](#hand)  =`otherHand`  zu taggen. 

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

### @hand

Enthält einen Verweis auf die ID eines [`<handNote/>`](handNote.md)-Element, das im[`<teiHeader/>`](teiHeader.md)  deklariert wurde.

*Mögliche Werte*

- Verweis auf Identifikator

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

### @rend



*Mögliche Werte*

- other_ink – *mit anderer Tinte*
- pencil – *mit Bleistift*

### @type



*Mögliche Werte*

- sign – *Hinzufügung durch spezielles Zeichen markiert.*

## Beispiele

### Beispiel 1

Beispiel für eine beschädigte Stelle, in die eine andere Hand Text eingetragen hat

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <add hand="otherHand" place="overwritten">zuͦ trincken</add>
    </damage>
</egXML>
               
```

### Beispiel 2

Beispiel für eine Ersetzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <subst>
        <del>zugeschafft</del>
        <add place="above">angethan</add>
    </subst>
</egXML>
               
```

### Beispiel 3

Beispiel für eine Hinzufügung am linken Rand

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <add place="left_margin" type="sign" rend="other_ink" hand="otherHand">
            <lb />zuͦ unnd be
                    <lb break="no" />schlossen
                </add>
                zuͦ halten
            </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)