---
title: condition
---



# `<condition/>` (état matériel)

## Description

Décrit l'état de conservation et les dommages d'une source. Les descriptions détaillées, telles que les lacunes, les trous, etc. à l'endroit indiqué. 

## Modèle de contenu

- **core**: [p](p.md)

## Attributs

### @agent

Décrit le type de dommage selon une liste de valeurs bien définie. 

*Valeurs possibles*

- cancelled – *cassation*
- clipping – *écrêtage sur le bord de la feuille*
- covered_by_seal – *un sceau couvrant*
- crack – *déchirure*
- faded_ink – *l’estompage de l’encre*
- fold – *pli*
- folio_lost – *la perte de la page/feuille*
- glued_page – *pages collées*
- hairline – *légère(s) fissure(s)*
- hole – *trou*
- ink_blot – *coulure d’encre*
- ink_hole – *corrosion d’encre*
- insects – *des insectes*
- mice – *des dents de rongeurs*
- mildew – *la moisissure*
- overbinding – *la couverture de la reliure*
- part_of_the_folio_lost – *la perte d’une partie de la page/feuille*
- restoration – *la restauration*
- smoke – *la fumée/le feu*
- stapling – *une agrafe*
- water_spot – *des traces d’eau ou d’humidité*

## Exemples

### Exemple 1

Structure modèle

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <condition agent="mice">
        <p>Mäusefrass</p>
    </condition>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.1.5. Condition](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphco)