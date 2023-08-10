---
title: physDesc
---



# `<physDesc/>` (description physique)

## Description

Décrit l'état physique de la source (matériel, masse, état de conservation, mains des scribes, décorations extraordinaires, sceaux). 

## Modèle de contenu

- **msdescription**: [bindingDesc](bindingDesc.md) [handDesc](handDesc.md) [objectDesc](objectDesc.md) [sealDesc](sealDesc.md)

## Exemples

### Exemple 1

Description simple de la source

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <physDesc>
        <objectDesc form="copy">
            <supportDesc>
                <support>
                    <material type="paper" />
                </support>
                <extent>
                    <dimensions type="leaves">
                        <height unit="cm" quantity="16.0" />
                        <width unit="cm" quantity="23.0" />
                    </dimensions>
                    <dimensions type="plica">
                        <width unit="cm" quantity="4.0" />
                    </dimensions>
                </extent>
            </supportDesc>
        </objectDesc>
    </physDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7. Physical Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph)