---
title: damage
---



# `<damage/>` (dommage)

## Description

Indique une section endommagée.

## Explication

Le type de dommage est décrit plus en détail avec [@agent](#agent). Dans la mesure du possible, le texte manquant est complété par[`<supplied/>`](supplied.md)  ou, si la lecture est incertaine, par[`<unclear/>`](unclear.md). Si aucun texte ne peut être ajouté,[`<gap/>`](gap.md)  est utilisé. Une combinaison des balises[`<unclear/>`](unclear.md),[`<supplied/>`](supplied.md)  et[`<gap/>`](gap.md)  peut également être utilisée, selon la gravité de la corruption. Pour les passages de texte plus longs, lorsque[`<damage/>`](damage.md)  seul ne suffit plus,[`<damageSpan/>`](damageSpan.md)  doit être utilisé.

En règle générale, [`<damage/>`](damage.md)  est utilisé pour marquer la destruction physique et l'interférence non gratuite. Un rasage est marqué par[`<del/>`](del.md). Une description générale des dommages majeurs est également donnée dans les métadonnées.

## Modèle de contenu

- **core**: [add](add.md) [gap](gap.md) [unclear](unclear.md)
- **transcr**: [supplied](supplied.md)

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

Exemple d'une zone endommagée où le texte a été écrit par une autre main

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <add hand="otherHand" place="overwritten">zuͦ trincken</add>
    </damage>
</egXML>
               
```

### Exemple 2

Exemple d'endroit endommagé où le texte est illisible

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <gap quantity="9" unit="cm" />
    </damage>
</egXML>
               
```

### Exemple 3

Exemple de passage endommagé dont le texte a été ajouté

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="water_spot">
        <supplied source="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">verthruwen</supplied>
    </damage>
</egXML>
               
```

### Exemple 4

Exemple de passage endommagé dont la lecture est incertaine

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="ink_blot">
        <unclear>die</unclear>
    </damage>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)