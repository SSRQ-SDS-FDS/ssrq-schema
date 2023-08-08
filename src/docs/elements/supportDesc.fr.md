---
title: supportDesc
---



# `<supportDesc/>` (description du support)

## Description

Contient des éléments pour décrire le matériau, les masses, nombre de feuilles et l'état de conservation d'une source. 

## Modèle de contenu

- **header**: [extent](extent.md)
- **msdescription**: [condition](condition.md) [foliation](foliation.md) [support](support.md)

## Exemples

### Exemple 1

Description du matériau et des dimensions

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

## Sections des Guidelines de la TEI

- [10.7.1. Object Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph1)