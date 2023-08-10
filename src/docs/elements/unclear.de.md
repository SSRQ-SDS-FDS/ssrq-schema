---
title: unclear
---



# `<unclear/>`

## Beschreibung

Enthält eine unsichere Lesung.

## Erläuterung

Ist die Ursache eine Beschädigung, dann wird diese durch [`<damage/>`](damage.md)  angegeben. Mit[@cert](#cert)  kann angegeben werden, wie sicher die Lesung ist. Erweist sich eine Stelle als absolut unlesbar, so wird sie mit[`<gap/>`](gap.md)  ausgezeichnet.

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

### @cert

Angabe des Grads der Sicherheit

*Mögliche Werte*

- high – *hoch*
- medium – *mittel*
- low – *niedrig*

## Beispiele

### Beispiel 1

Beispiel für eine beschädigte Stelle, deren Lesung unsicher ist

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="ink_blot">
        <unclear>die</unclear>
    </damage>
</egXML>
               
```

### Beispiel 2

Unsichere Lesung ohne Beschädigung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">ve<unclear cert="high">stik</unclear>lich
        </egXML>
               
```

### Beispiel 3

Verblasste Tinte in einer Editionsvorlage, bei der eine unsichere Lesung durch den Bearbeitenden möglich ist

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">und sol och der w
            <damage agent="faded_ink">
        <unclear>eib</unclear>
    </damage>
            el
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)
- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)