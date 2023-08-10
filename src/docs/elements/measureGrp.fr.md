---
title: measureGrp
---



# `<measureGrp/>` (groupe de mesures)

## Description

Contient un groupe de mesures.

## Modèle de contenu

- **core**: [lb](lb.md) [measure](measure.md)
- **figures**: [cell](cell.md)
- **textcrit**: [app](app.md)

## Exemples

### Exemple 1

Unité monétaire qui ne peut pas être convertie:

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

### Exemple 2

Diverses quantités de blé:

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

### Exemple 3

Divers indications de surface:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <measureGrp>
        <measure type="area" unit="Juchart" quantity="3" commodity="field">dryg juchart akkers</measure>
        <measure type="area" unit="Mitmal" quantity="0.5" commodity="field">ains halben mitmels</measure>minder
            </measureGrp>
    <note>Es sind 3 Jucharten weniger 0.5 Mitmal (= 1/8 Juchart) = 2 7/8 Jucharten.</note>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)