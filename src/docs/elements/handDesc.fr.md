---
title: handDesc
---



# `<handDesc/>` (description des écritures)

## Description

Décrit les mains et tous les changements de mains.

## Explication

Les marges, les suppressions, les corrections, etc. sont marquées directement au point dans le texte. Seuls les auteurs "importants" sont inscrits. 

## Modèle de contenu

- **header**: [handNote](handNote.md)

## Exemples

### Exemple 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <physDesc>
        <handDesc>
            <handNote xml:id="hand1" n="firstHand" scribe="per123456">
                <date from-custom="1001-01-01" to-custom="1100-12-31">
                    <precision precision="low" match="@from-custom" />
                </date>
            </handNote>
            <handNote xml:id="hand2" n="secondHand" />
            <handNote xml:id="hand3" n="otherHand" />
            <handNote xml:id="hand4" n="laterHand" />
        </handDesc>
    </physDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.2. Writing, Decoration, and Other Notations](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph2)