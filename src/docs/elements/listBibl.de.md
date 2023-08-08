---
title: listBibl
---



# `<listBibl/>` (Liste bibliografischer Angaben)

## Beschreibung

Enthält mit [`<bibl/>`](bibl.md)  kodierte bibliographische Angaben.

## Inhaltsmodell

- **core**: [bibl](bibl.md)

## Attribute

### @type



*Mögliche Werte*

- edition – *Edition*
- literature – *Literatur*
- summary – *Regest*
- translation – *Übersetzung*
- url – *URL*

## Beispiele

### Beispiel 1

Verweise auf Regsten

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <listBibl type="summary">
        <bibl>Rigendinger 2007, S. 221–223</bibl>
    </listBibl>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.1. Methods of Encoding Bibliographic References and Lists of References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBITY)
- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)
- [15.3.2. Declarable Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAS2)