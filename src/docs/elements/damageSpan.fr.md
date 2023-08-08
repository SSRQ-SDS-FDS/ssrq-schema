---
title: damageSpan
---



# `<damageSpan/>` (partie de texte endommagée)

## Description

Désigne des sections plus grandes qui sont endommagées.

## Explication

 [@spanTo](#spanTo)  est utilisé pour forcer la référence au point final de la corruption, qui est marqué par[`<anchor/>`](anchor.md). Le type de dommage est décrit plus en détail avec[@agent](#agent)  analogue à[`<damage/>`](damage.md).

## Modèle de contenu

Ne contient aucun élément ou texte.

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

### @spanTo

Pointe vers le [@xml:id](#xml:id)  d'un point de terminaison

*Valeurs possibles*

- Référence à l'identifiant

## Exemples

### Exemple 1

Exemple d'un dommage plus important

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damageSpan agent="faded_ink" spanTo="damage1" />
    <lb />geschwüsterige, einandern erben und im fahl die
    <lb />mutter im leben wär, soll die mutter den dritten
    <lb />theil und die geschwüsterte die zwenn theil erben.
    <anchor xml:id="damage1" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)