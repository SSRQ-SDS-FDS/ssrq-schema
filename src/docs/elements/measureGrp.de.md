---
title: measureGrp
---



# `<measureGrp/>`

## Beschreibung

Enthält eine Gruppe von Massen.

## Inhaltsmodell

- **core**: [lb](lb.md) [measure](measure.md)
- **figures**: [cell](cell.md)
- **textcrit**: [app](app.md)

## Beispiele

### Beispiel 1

Währungsbezeichnungen, die man auf Anhieb nicht umrechnen kann:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">... buͦß verfallen sin
            <measureGrp>
        <measure quantity="3" unit="lb" type="currency">druͤ pfund
                </measure>
        <measure quantity="5" unit="ß" type="currency">fuͤnf schilling
                    pfenig
                </measure>
    </measureGrp>
            .
        </egXML>
               
```

### Beispiel 2

Verschiedene Mengenangaben von Getreide:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <measureGrp>
        <measure commodity="wheat" unit="Scheffel" quantity="10" type="volume">zehen schoͤffel</measure>
                und
                <measure commodity="wheat" unit="Viertel" quantity="1" type="volume">ain viertail waissen</measure>
    </measureGrp>
            und ...
        </egXML>
               
```

### Beispiel 3

Verschiedene Flächenangaben:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <measureGrp>
        <measure type="area" unit="Juchart" quantity="3" commodity="field">dryg juchart akkers</measure>
        <measure type="area" unit="Mitmal" quantity="0.5" commodity="field">ains halben mitmels</measure>minder
            </measureGrp>
    <note>Es sind 3 Jucharten weniger 0.5 Mitmal (= 1/8 Juchart) = 2 7/8 Jucharten.</note>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)