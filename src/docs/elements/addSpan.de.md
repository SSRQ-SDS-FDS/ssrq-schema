---
title: addSpan
---



# `<addSpan/>`

## Beschreibung

Bezeichnet größere Hinzufügungen.

## Erläuterung

Mit [@spanTo](#spanTo)  wird zwingend auf den Endpunkt der Hinzufügung verwiesen, der mit[`<anchor/>`](anchor.md)  markiert wird.

Der Ort der Hinzufügung muss zwingend in [@place](#place)  und die Hand der ergänzten Stelle kann mit[@hand](#hand)  festgehalten werden. Falls notwendig, kann innerhalb von[@rend](#rend)  angegeben werden, wie die Hinzufügung (mit Bleistift, anderer Tinte etc.) vorgenommen wurde. Handelt es sich bei einer Ergänzung um die Hand des ersten Schreibers, dann wird die Hand nicht speziell angemerkt.

## Inhaltsmodell

Enhält keine Elemente oder Text.

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

### @rend



*Mögliche Werte*

- other_ink – *mit anderer Tinte*
- pencil – *mit Bleistift*

### @spanTo

Verweist auf die [@xml:id](#xml:id)  eines Endpunktes

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für eine umfangreichere Hinzufügung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <addSpan spanTo="add1" hand="otherHand" place="bottom" rend="pencil" />
    <lb />Presentibus
    <lb />Antonio nepote domini officialis, fratre Germano ordinis Predicatorum; dominus
    <lb />officialis prefatus monuit dictam Jordanam pro secunda dilatione
    <lb />et assignata est ad cras pro tertia.
    <lb />Delayens
    <anchor xml:id="add1" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.1.4. Additions and Deletions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)