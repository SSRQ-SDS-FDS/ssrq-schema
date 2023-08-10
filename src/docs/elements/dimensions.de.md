---
title: dimensions
---



# `<dimensions/>`

## Beschreibung

Masse einer Quelle

## Erläuterung

Wenn [@type](#type)  den Wert`plica`  hat, dann ist nur ein [`<width/>`](width.md)-Element als Inhalt erlaubt.

## Inhaltsmodell

- **msdescription**: [height](height.md) [width](width.md)

## Attribute

### @type



*Mögliche Werte*

- leaves – *Ausmass der Blätter*
- plica – *Ausmass der Plica*

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <extent>
        <dimensions type="leaves">
            <height unit="cm" quantity="16.0" />
            <width unit="cm" quantity="23.0" />
        </dimensions>
        <dimensions type="plica">
            <width unit="cm" quantity="4.0" />
        </dimensions>
    </extent>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.3.4. Dimensions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdim)