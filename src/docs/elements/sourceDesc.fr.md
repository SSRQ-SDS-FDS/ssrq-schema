---
title: sourceDesc
---



# `<sourceDesc/>` (description de la source)

## Description

Contient des éléments décrivant la source ou les sources.

## Explication

Le contenu (regest), le lieu de stockage, le matériel, la mise en page, le scribe, le sceau et les références bibliographiques sont décrits. Comme la plupart de ces métadonnées sont exportées depuis un AIS ou une base de données du sous-traitant et importées dans le portail, seuls les sceaux en [`<sealDesc/>`](sealDesc.md)  ou[`<seal/>`](seal.md)  sont enregistrés plus précisément ici.

## Modèle de contenu

- **msdescription**: [msDesc](msDesc.md)
- **textcrit**: [listWit](listWit.md)

## Exemples

### Exemple 1

Exemple de description de source avec un témoin de texte

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sourceDesc>
        <msDesc>
                ...
            </msDesc>
    </sourceDesc>
</egXML>
               
```

### Exemple 2

Exemple d'une description de source avec une liste de témoins de texte

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sourceDesc>
        <listWit>
                ...
            </listWit>
    </sourceDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)