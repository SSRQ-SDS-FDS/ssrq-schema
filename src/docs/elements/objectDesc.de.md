---
title: objectDesc
---



# `<objectDesc/>`

## Beschreibung

Enthält Elemente zur Beschreibung des Materials, der Masse, des Erhaltungszustands sowie Aussehens der Quelle. 

## Inhaltsmodell

- **msdescription**: [supportDesc](supportDesc.md)

## Attribute

### @form

Beschreibung der (physischen) Überlieferungsform.

*Mögliche Werte*

- book – *Buch*
- booklet – *Heft*
- copy – *Abschrift*
- draft – *Entwurf*
- entry – *Eintrag*
- excerpt – *Auszug*
- fragment – *Fragment*
- insert – *Insert*
- original – *Original*
- partial_copy – *Teilabschrift*
- photocopy – *Fotokopie*
- print – *Druck*
- rotulus – *Rotulus*
- summary – *Regest*
- translation – *Übersetzung*
- vidimus – *Vidimus*

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <objectDesc form="original">
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
                <measure type="text_scope" unit="leaf" quantity="2" />
                <measure type="text_scope" unit="page" quantity="4" />
            </extent>
        </supportDesc>
    </objectDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.1. Object Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph1)