---
title: addSpan
---



# `<addSpan/>` (partie de texte ajoutée)

## Description

Désigne des ajouts majeurs.

## Explication

 [@spanTo](#spanTo)  est utilisé pour faire référence au point final de l'addition, qui est marquée par[`<anchor/>`](anchor.md).

La place d'addition doit être dans [@place](#place)  et la main de la place ajoutée peut être tenue avec[@ hand](# hand). Si nécessaire, à l'intérieur de[@rend](#rend), il est possible de spécifier comment l'ajout a été effectué (crayon, autre encre, etc.). Si un ajout est la main du premier scribe, alors la main n'est pas spécifiquement notée.

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

### @place

Indique une position sur un témoin de texte selon une liste fixe. 

*Valeurs possibles*

- above – *au-dessus de la ligne*
- below – *au-dessous de la ligne*
- bottom – *en bas de page*
- cover – *sur la couverture*
- cover_above – *en haut de la couverture*
- cover_bottom – *en bas de la couverture*
- cover_middle – *au milieu de la couverture*
- left_margin – *dans la marge de gauche*
- next_page – *sur la page suivante*
- right_margin – *dans la marge de droite*
- verso – *au verso*

### @rend

Indique comment l'élément en question a été rendu ou présenté dans le texte source

*Valeurs possibles*

- other_ink – *avec une autre encre*
- pencil – *au crayon*

### @spanTo

Pointe vers le [@xml:id](#xml:id)  d'un point de terminaison

*Valeurs possibles*

- Référence à l'identifiant

## Exemples

### Exemple 1

Exemple d'un ajout plus important

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <addSpan spanTo="add1" hand="otherHand" place="bottom" rend="pencil" />
    <lb />Presentibus
    <lb />Antonio nepote domini officialis, fratre Germano ordinis Predicatorum; dominus
    <lb />officialis prefatus monuit dictam Jordanam pro secunda dilatione
    <lb />et assignata est ad cras pro tertia.
    <lb />Delayens
    <anchor xml:id="add1" />
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.1.4. Additions and Deletions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)