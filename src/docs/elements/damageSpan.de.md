---
title: damageSpan
---



# `<damageSpan/>`

## Beschreibung

Bezeichnet größere Abschnitte, die beschädigt sind.

## Erläuterung

Mit [@spanTo](#spanTo)  wird zwingend auf den Endpunkt der Beschädigung verwiesen, der mit[`<anchor/>`](anchor.md)  markiert wird. Die Art der Beschädigung wird analog zu[`<damage/>`](damage.md)  mit[@agent](#agent)  näher beschrieben.

## Inhaltsmodell

Enhält keine Elemente oder Text.

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

### @spanTo

Verweist auf die [@xml:id](#xml:id)  eines Endpunktes

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für einen umfangreicheren Schaden

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damageSpan agent="faded_ink" spanTo="damage1" />
    <lb />geschwüsterige, einandern erben und im fahl die
    <lb />mutter im leben wär, soll die mutter den dritten
    <lb />theil und die geschwüsterte die zwenn theil erben.
    <anchor xml:id="damage1" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)