---
title: figure
---



# `<figure/>` (Abbildung)

## Beschreibung

Enthält Elemente, die grafische Informationen beschreiben.

## Erläuterung

Enthält Notarzeichen (= Notariatszeichen, Notariatssignet, Signum), Federzeichnungen, Holzschnitte, Verweiszeichen oder bei Kopien von Urkunden die Stelle, an der sich in der Originalurkunde das Siegel befindet (L. S. = Locus sigilli) oder Abbildungen, die mit [`<graphic/>`](graphic.md)  referenziert werden.

## Inhaltsmodell

- **core**: [graphic](graphic.md) [head](head.md)

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

### @type

Zwingende Zuordnung zu einem Typ

*Mögliche Werte*

- copper_engraving – *Kupferstich*
- drawing – *Federzeichnung*
- illustration – *Abbildung*
- locus_sigilli – *Locus sigilli*
- monogram – *Monogramm*
- notarial_sign – *Notarzeichen*
- sign – *Verweiszeichen*
- stamp – *Stempel*
- woodcut – *Holzschnitt*

## Beispiele

### Beispiel 1

Beispiel für ein Notariatszeichen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <signed>
        <figure type="notarial_sign" />
        <lb />Et ego Hainricus Jacobi de Augiamaiori ...
        </signed>
</egXML>
               
```

### Beispiel 2

Beispiel eines Stammbaums

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [14.4. Specific Elements for Graphic Images](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/FT.html#FTGRA)