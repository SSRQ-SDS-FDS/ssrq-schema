---
title: abbr
---



# `<abbr/>` (Abkürzung)

## Beschreibung

Enthält eine Abkürzung.

## Erläuterung

Es werden keine Kürzungspunkte verwendet, da die Abkürzungen durch die Auszeichnung bereits als solche gekennzeichnet sind. 

Orthographische Gepflogenheiten des Schreibers werden ohne besondere Kennzeichnung berücksichtigt. Selbstverständliches wird stillschweigend aufgelöst, z. B. Nasalstriche, Affixe («-er», «con-», «per-»). Xsti wird stillschweigend aufgelöst in Christi, ebenso Ao = anno, wz = was oder dz = das. 

Abkürzungen in der Textvorlage werden, wenn es möglich und sinnvoll ist, mit Hilfe von [`<choice/>`](choice.md)  und[`<expan/>`](expan.md)  aufgelöst.

Abkürzungen von Mass- und Münzbezeichnungen werden ausser in Fliesstexten (Kommentaren, Bemerkungen) nicht aufgelöst. Es werden die entsprechenden Sonderzeichen verwendet. 

## Inhaltsmodell

- **core**: [hi](hi.md) [lb](lb.md) [sic](sic.md) [unclear](unclear.md)
- Beliebiger Textinhalt

## Beispiele

### Beispiel 1

Beispiel für eine Abkürzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <abbr>sabbo</abbr>
        <expan>sabbato</expan>
    </choice>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.6.5. Abbreviations and Their Expansions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONAAB)