---
title: gap
---



# `<gap/>` (Auslassung)

## Beschreibung

Beschreibt eine Auslassung durch den Editor.

## Erläuterung

Dies betrifft vor allem gänzlich unleserliche Stellen. Der Grund für eine Auslassung kann mit [@reason](#reason)  angegeben werden. Wenn die Ursache einer Unlesbarkeit aber eine Beschädigung ist, so wird auf[@reason](#reason)  verzichtet – stattdessen wird der Tag mit[`<damage/>`](damage.md)  umschlossen. Ist der Grund für eine Unlesbarkeit eine Rasur oder eine (heftige) Streichung, wird der Tag in ein[`<del/>`](del.md)  verschachtelt.

Die Grösse der Auslassung wird mit [@unit](#unit)  und[@quantity](#quantity)  angegeben. Massangaben werden auf 0.5 auf- oder abgerundet.

Werden spätere Nachträge nicht beim Original, sondern als eigenständiges Stück ediert, können die Teile, die bereits in einem früheren Original ediert wurden, mit [`<gap/>`](gap.md)  weggelassen werden. Auf das edierte Stück wird mit[@source](#source)  verwiesen. In diesem Fall wird eine Anmerkung in[`<note/>`](note.md)  oder eine Bemerkung in[`<back/>`](back.md)  ergänzt.

Für Zeilensprünge in der Vorlage wird nicht [`<gap/>`](gap.md), sondern[`<supplied/>`](supplied.md)  verwendet.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @quantity

Gibt die Grösse der mit [@unit](#unit)  angegebenen Einheit an

*Mögliche Werte*

- Gleitkommazahl
- Zahl
- unknown – *unbekannt*

### @reason

Grund der Lücke

*Mögliche Werte*

- illegible – *unleserlich*
- irrelevant – *irrelevant*
- missing – *fehlt*

### @source

Verweis auf ein anderes Stück (bspw. im Falle der Mehrfachüberlieferung) oder auf ein Archivinformationssystem. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `urn:ssrq:(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)(-((([A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)))?(#[A-Za-z0-9_]+)?`
- anyURI – Einschränkung: regulärer Ausdruck `(https?|ftp)://[^\s/$.?#].[^\s]*`

### @unit

Masseinheit

*Mögliche Werte*

- cm – *cm*
- line – *Zeile*
- character – *Buchstabe*
- page – *Seite*
- word – *Wort*

## Beispiele

### Beispiel 1

Beispiel für eine beschädigte Stelle, deren Text unlesbar ist

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <gap quantity="9" unit="cm" />
    </damage>
</egXML>
               
```

### Beispiel 2

Unlesbare Zeile ohne Streichung oder Beschädigung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <gap reason="illegible" unit="line" quantity="1.0" />
</egXML>
               
```

### Beispiel 3

Loch in einer Editionsvorlage, bei dem keine Ergänzung möglich ist – Masse werden auf 0.5 auf- oder abgerundet.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            und sol och der w
            <damage agent="hole">
        <gap unit="cm" quantity="3.5" />
    </damage>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)