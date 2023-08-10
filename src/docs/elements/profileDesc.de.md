---
title: profileDesc
---



# `<profileDesc/>` (Beschreibung des Textprofils)

## Beschreibung

Enthält Elemente zur Beschreibung des Textes mithilfe von Schlagworten. 

## Inhaltsmodell

- **header**: [textClass](textClass.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <profileDesc>
        <textClass>
            <keywords>
                <term ref="key000192" />
                <term ref="key000097" />
                <term ref="key000049" />
                <term ref="key000193" />
            </keywords>
        </textClass>
    </profileDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.4. The Profile Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD4)
- [2.1.1. The TEI Header and Its Components](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD11)