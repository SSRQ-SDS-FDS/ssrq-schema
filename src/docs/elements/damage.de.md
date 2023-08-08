---
title: damage
---



# `<damage/>`

## Beschreibung

Bezeichnet einen beschädigten Abschnitt.

## Erläuterung

Die Art der Beschädigung wird mit [@agent](#agent)  näher beschrieben. Soweit möglich, wird der fehlende Text mit[`<supplied/>`](supplied.md)  oder bei unsicherer Lesung mit[`<unclear/>`](unclear.md)  ergänzt. Wenn kein Text ergänzt werden kann, wird[`<gap/>`](gap.md)  verwendet. Je nach Stärke der Beschädigung kann auch eine Kombination der Tags[`<unclear/>`](unclear.md),[`<supplied/>`](supplied.md)  und[`<gap/>`](gap.md)  verwendet werden. Bei längeren Textpassagen, wenn[`<damage/>`](damage.md)  alleine nicht mehr reicht, ist[`<damageSpan/>`](damageSpan.md)  zu verwenden.

In der Regel werden mit [`<damage/>`](damage.md)  physikalische Zerstörungen und nicht mutwillige Eingriffe ausgezeichnet. Eine Rasur wird mit[`<del/>`](del.md)  ausgezeichnet. Eine Beschreibung von grösseren Schäden erfolgt zusätzlich pauschal in den Metadaten.

## Inhaltsmodell

- **core**: [add](add.md) [gap](gap.md) [unclear](unclear.md)
- **transcr**: [supplied](supplied.md)

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

Beispiel für eine beschädigte Stelle, in die eine andere Hand Text eingetragen hat

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <add hand="otherHand" place="overwritten">zuͦ trincken</add>
    </damage>
</egXML>
               
```

### Beispiel 2

Beispiel für eine beschädigte Stelle, deren Text unlesbar ist

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <gap quantity="9" unit="cm" />
    </damage>
</egXML>
               
```

### Beispiel 3

Beispiel für eine beschädigte Stelle, deren Text ergänzt wurde

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <supplied source="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">verthruwen</supplied>
    </damage>
</egXML>
               
```

### Beispiel 4

Beispiel für eine beschädigte Stelle, deren Lesung unsicher ist

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="ink_blot">
        <unclear>die</unclear>
    </damage>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)