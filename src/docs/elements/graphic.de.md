---
title: graphic
---



# `<graphic/>` (Abbildung)

## Beschreibung

Enthält Informationen zu einem Bild oder einer graphischen Illustration als Teil des Textes oder externe Referenz. 

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @mimeType

MimeType der eingebundenen Bilddatei

*Mögliche Werte*

- image/jpg
- image/png
- image/svg

### @type

Typ der Grafik

*Mögliche Werte*

- familytree – *Stammbaum*
- figure – *Visualisierung*
- graphic – *Illustration*
- map – *Karte*

### @url

Verknüpfung mit einer Bilddatei.

*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

## Beispiele

### Beispiel 1

Beispiel eines Stammbaums

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

### Beispiel 2

Definition der Identifikationsnummer des Stücks:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <graphic type="graphic" mimeType="image/jpg" url="SSRQ-FR-I_2_8-graphic-6.jpg" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.10. Graphics and Other Non-textual Components](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COGR)
- [11.1. Digital Facsimiles](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHFAX)