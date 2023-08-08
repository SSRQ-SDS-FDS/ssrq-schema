---
title: condition
---



# `<condition/>`

## Beschreibung

Beschreibt den Erhaltungszustand und Schäden einer Quelle. Detailbeschreibungen, wie Lücken, Löcher etc., erfolgen an der entsprechenden Stelle. 

## Inhaltsmodell

- **core**: [p](p.md)

## Attribute

### @agent

Beschreibt die Art einer Beschädigung gemäss einer fest definierten Werteliste. 

*Mögliche Werte*

- cancelled – *Kassation*
- clipping – *Beschneidung am Blattrand*
- covered_by_seal – *verdeckendes Siegel*
- crack – *Riss*
- faded_ink – *verblasste Tinte*
- fold – *Falte*
- folio_lost – *fehlende Seite/fehlendes Blatt*
- glued_page – *zusammengeklebte Seiten*
- hairline – *feiner Riss*
- hole – *Loch*
- ink_blot – *Tintenklecks*
- ink_hole – *Tintenfrass*
- insects – *Insektenfrass*
- mice – *Mäusefrass*
- mildew – *Pilzbefall/Schimmel*
- overbinding – *verdeckender Einband*
- part_of_the_folio_lost – *fehlender Teil der Seite oder des Blatts*
- restoration – *Restauration*
- smoke – *Rauch/Brandschaden*
- stapling – *Heftklammer*
- water_spot – *wasserfleck*

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <condition agent="mice">
        <p>Mäusefrass</p>
    </condition>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.1.5. Condition](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphco)