---
title: num
---



# `<num/>` (Zahl)

## Beschreibung

Enthält eine Zahl im transkribierten Quelltext.

## Erläuterung

Der Wert der Zahl wird im Attribut [@value](#value)  maschinenlesbar hinterlegt.

Bei Angaben zu Massen, Gewichten, Währungen etc., in denen innerhalb von [`<measure/>`](measure.md)  mit[@quantity](#quantity)  die Anzahl ausgezeichnet wird, wird auf[`<num/>`](num.md)  verzichtet. Ebenso wird bei Jahreszahlen, die mit[`<origDate/>`](origDate.md) und[@when](#when)  genauer beschrieben werden, auf[`<num/>`](num.md)  verzichtet. Innerhalb von einer zeitlichen Angabe mit[@dur](#dur)  wird auf[`<num/>`](num.md)  verzichtet.

## Inhaltsmodell

- **core**: [hi](hi.md) [lb](lb.md) [pb](pb.md)
- Beliebiger Textinhalt

## Attribute

### @value

Zahlenwert in arabischen Ziffern

*Mögliche Werte*

- Gleitkommazahl
- Zahl

## Beispiele

Keine Beispiele für ausgewählte Sprache vorhanden.

## Abschnitte in den Guidelines der TEI

- [3.6.3. Numbers and Measures](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONANU)