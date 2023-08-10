---
title: docImprint
---



# `<docImprint/>` (Impressum)

## Beschreibung

Enthält bei Druckschriften den Druckort ([`<pubPlace/>`](pubPlace.md) ) und den Namen der Druckerei ([`<publisher/>`](publisher.md) ).

## Inhaltsmodell

- **core**: [pubPlace](pubPlace.md) [pubPlace](pubPlace.md) [publisher](publisher.md) [publisher](publisher.md)

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

### Beispiel 2

Beispiel für ein Impressum mit mehreren Druckorten

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <pubPlace>Bern</pubPlace>
    </docImprint>
</egXML>
               
```

### Beispiel 3

Beispiel für ein Impressum mit einer Druckerei

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4.6. Title Pages](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSTITL)