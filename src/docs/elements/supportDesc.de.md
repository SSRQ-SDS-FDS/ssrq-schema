---
title: supportDesc
---



# `<supportDesc/>`

## Beschreibung

Enthält Elemente zur Beschreibung von Material, Massen, Blattzählung und Erhaltungszustand einer Quelle. 

## Inhaltsmodell

- **header**: [extent](extent.md)
- **msdescription**: [condition](condition.md) [foliation](foliation.md) [support](support.md)

## Beispiele

### Beispiel 1

Beschreibung des Materials und der Abmessungen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <supportDesc>
        <support>
            <material type="paper" />
        </support>
        <extent>
            <dimensions type="leaves">
                <height unit="cm" quantity="29.0" />
                <width unit="cm" quantity="54.5" />
            </dimensions>
        </extent>
    </supportDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.1. Object Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph1)