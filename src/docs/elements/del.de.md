---
title: del
---



# `<del/>` (Streichung)

## Beschreibung

Enthält Text, der von einem Schreiber getilgt wurde.

## Erläuterung

Mit [`<del/>`](del.md)  werden keine Streichungen, die vom Editor stammen, ausgezeichnet, sondern nur solche, die sich in der Quelle befinden. Bei mehrfach gestrichenen Texten, oder wenn Streichungen Hierarchiegrenzen überschreiten, müssen[`<delSpan/>`](delSpan.md)  und[`<anchor/>`](anchor.md)  benutzt werden.

Rasuren werden mit dem Attribut [@rend](#rend)  =`rubbing`  ausgezeichnet. Wenn bei Rasuren oder auch bei heftigen Streichungen gar nichts mehr lesbar ist, wird ein leeres [`<gap/>`](gap.md)  innerhalb von[`<del/>`](del.md)  verwendet.

Das Attribut [@hand](#hand)  wird für Streichungen mit anderer Tinte verwendet. Bei späteren Texteingriffen (Streichung mit Korrektur) wird[@hand](#hand)  bei[`<add/>`](add.md)  innerhalb von[`<subst/>`](subst.md)  nachgewiesen.

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



*Mögliche Werte*

- blackened – *Streichung durch Schwärzen*
- bracketed – *Streichung durch Verwendung von Klammern*
- crossout – *Streichung durch gekreuzte Linien*
- overwritten – *Streichung durch direkte Überschreibung*
- rubbing – *Streichung durch Textlöschung/Rasur*
- strikethrough – *Streichung durch einfache Durchstreichung*
- subpunction – *Streichung durch Unterpunktung*
- underline – *Streichung mit Unterstreichen*

## Beispiele

### Beispiel 1

Beispiel für eine Ersetzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <subst>
        <del>zugeschafft</del>
        <add place="above">angethan</add>
    </subst>
</egXML>
               
```

### Beispiel 2

Beispiel für eine Tilgung.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>Item ein <del rend="crossout" hand="otherHand">ein</del> hofstatt
            </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)