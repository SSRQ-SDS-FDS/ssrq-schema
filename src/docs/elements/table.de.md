---
title: table
---



# `<table/>` (Tabelle)

## Beschreibung

Beschreibt eine Tabelle.

## Erläuterung

Wird zusammen mit [`<row/>`](row.md)  (Zeile) und[`<cell/>`](cell.md)  (Zelle) für die Darstellung von Tabellen benötigt. Es wird von oben nach unten und von links nach rechts gezählt. Wenn immer möglich eine Tabelle als Fliesstext dargestellt werden kann, soll auf die Darstellung in Form einer Tabelle verzichtet werden. In Tabellen und Listen werden – insbesondere bei den gedruckten Mandaten – Gänsefüsschen als Unterführungszeichen benutzt, um Wörter oder Zahlen aus der oberen Zeile zu wiederholen (vgl. Beispiel unten). In solchen Fällen wird das "Ditto-Mark" (U+0022) verwendet (zu transkribieren mit der Zeichenfolge "). Ebenso kommt in Tabellen ein Querstrich als Nullwert vor (vgl. Beispiel unten). Bei der Transkription wird hierfür der ziffernbreite Halbgeviertstrich – (U+2012) verwendet (zu transkribieren mit der Zeichenfolge ‒).

## Inhaltsmodell

- **core**: [head](head.md) [pb](pb.md)
- **figures**: [row](row.md)

## Beispiele

### Beispiel 1

Beispiel für eine Preisliste für Wein mit vier Spalten, wovon die letzten drei Spalten mit «gbz», «xr» bzw. «dn» überschrieben sind

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

## Abschnitte in den Guidelines der TEI

- [14.1.1. TEI Tables](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/FT.html#FTTAB1)