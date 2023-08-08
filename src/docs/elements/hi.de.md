---
title: hi
---



# `<hi/>` (hervorgehoben)

## Beschreibung

Beschreibt die graphische Hervorhebung von Text.

## Erläuterung

Die Rechtsquellenstiftung macht keine faksimilierenden Transkriptionen, weshalb Versalien, Einzüge etc. nicht dargestellt werden. Punkte vor hochgestellten Buchstaben bei Aufzählungen, Datierungen, Abkürzungen usw. werden nicht berücksichtigt. 

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

### @rend

Zeigt an, wie ein fragliches Zeichen im Originaltext aussieht. 

*Mögliche Werte*

- center – *zentriert*
- framed – *umrandet*
- font_change – *Schriftwechsel*
- italic – *kursiv*
- left – *linksbündig*
- outdent – *hängender Einzug*
- right – *rechtssbündig*
- rubricated – *rubriziert*
- sup – *hochgestellt*
- underline – *unterstrichen*

## Beispiele

### Beispiel 1

Auszeichnung hochgestellter Buchstaben

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">deß 1729<hi rend="sup">ten</hi> jahrs
        </egXML>
               
```

### Beispiel 2

Beispiele einer Unterstreichung von späterer Hand – das Attribut hand ist ein Verweis auf eine handNote

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <hi rend="underline" hand="laterHand">unterstrichener Text mit anderer Tinte</hi>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.3.2.2. Emphatic Words and Phrases](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQHE)
- [3.3.2. Emphasis, Foreign Words, and Unusual Language](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQH)