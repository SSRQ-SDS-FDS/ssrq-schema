---
title: pubPlace
---



# `<pubPlace/>` (Verlagsort)

## Beschreibung

Enthält den Publikationsort.

## Erläuterung

Dies kann sowohl der Publikationsort der elektronischen Edition sein als auch der Publikationsort des in der Literaturliste aufgeführten Artikels oder Buches. Bei Druckschriften wird innerhalb von [`<docImprint/>`](docImprint.md)  der Druckort mit[`<pubPlace/>`](pubPlace.md)  genannt.

## Inhaltsmodell

- Beliebiger Textinhalt

## Attribute

### @cert

Angabe des Grads der Sicherheit

*Mögliche Werte*

- high – *hoch*
- medium – *mittel*
- low – *niedrig*

## Beispiele

### Beispiel 1

Beispiel für ein Impressum mit Druckort und Druckerei

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)