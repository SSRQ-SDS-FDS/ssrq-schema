---
title: objectDesc
---



# `<objectDesc/>` (description d'objet)

## Description

Contient des éléments décrivant le matériau, la masse, l'état de conservation et l'apparence de la source. 

## Modèle de contenu

- **msdescription**: [supportDesc](supportDesc.md)

## Attributs

### @form

Description de la forme (physique) de transmission.

*Valeurs possibles*

- book – *Livre*
- booklet – *Cahier*
- copy – *Copie*
- draft – *Brouillon*
- entry – *Entrée*
- excerpt – *Extrait*
- fragment – *Fragment*
- insert – *Insert*
- original – *Original*
- partial_copy – *Copie partielle*
- photocopy – *Photocopie*
- print – *Impression*
- rotulus – *Rotulus*
- summary – *Regeste*
- translation – *Traduction*
- vidimus – *Vidimus*

## Exemples

### Exemple 1

Structure modèle

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

## Sections des Guidelines de la TEI

- [10.7.1. Object Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph1)