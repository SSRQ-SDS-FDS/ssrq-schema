---
title: row
---



# `<row/>` (Tabellenzeile)

## Beschreibung

Beschreibt eine Zeile einer Tabelle.

## Erläuterung

Wird zusammen mit [`<table/>`](table.md)  (Tabelle) und[`<cell/>`](cell.md)  (Zelle) für die Darstellung von Tabellen benötigt.

## Inhaltsmodell

- **core**: [measureGrp](measureGrp.md)
- **figures**: [cell](cell.md)

## Beispiele

### Beispiel 1

Einfaches Beispiel für Zeilen in einer Tabelle

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