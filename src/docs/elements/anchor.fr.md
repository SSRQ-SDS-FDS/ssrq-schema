---
title: anchor
---



# `<anchor/>` (point d'ancrage)

## Description

Point final d'un ajout important ([`<addSpan/>`](addSpan.md) ), d'une suppression ([`<delSpan/>`](delSpan.md) ) ou d'une corruption ([`<damageSpan/>`](damageSpan.md) ).

## Explication

La valeur de l'attribut [@xml:id](#xml:id)  est la première partie du nom des éléments correspondants ([`<addSpan/>`](addSpan.md),[`<delSpan/>`](delSpan.md)  ou[`<damageSpan/>`](damageSpan.md) ) et a pour composer un numéro consécutif: ex. add1, add2, etc. ou del1, del2, etc. ou damage1, damage2, etc.

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @xml:id

Fournit un identifiant unique pour l'élément qui porte l'attribut

*Valeurs possibles*

- Identificateur – Restriction: expression régulière `(del|damage|add)[1-9]+`

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

### Exemple 2

Exemple de suppression plus importante

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <delSpan spanTo="del1" hand="otherHand" rend="crossout" />
    <lb />Wir der Burgermeyster
    <lb />Radt und der groß Radt. Embietend
    <lb />allen und yeden unsern Burgeren
    <lb />unsern günstlichen gruͦß / geneygten
    <lb />willen / unnd alles guͦts zuͦvor / unnd thuͦnd üch sampt unnd sunders
    <lb />zuͦ vernemmen.
    <anchor xml:id="del1" />
</egXML>
               
```

### Exemple 3

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

- [8.4.2. Synchronization and Overlap](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TS.html#TSSAPA)
- [16.5. Correspondence and Alignment](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SACS)