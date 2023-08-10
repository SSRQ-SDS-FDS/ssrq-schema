---
title: delSpan
---



# `<delSpan/>` (partie de texte supprimée)

## Description

Désigne des sections plus grandes qui ont été supprimées du texte. 

## Explication

Avec [@spanTo](#spanTo)  une référence obligatoire est faite au point final de l'effacement, qui est marqué par[`<anchor/>`](anchor.md).

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

### @rend

Indique comment l'élément en question a été rendu ou présenté dans le texte source

*Valeurs possibles*

- blackened – *caviardage*
- bracketed – *la suppression se trouve entre parenthèses*
- crossout – *suppression en croisant la ligne*
- overwritten – *la suppression a été remplacée directement*
- rubbing – *suppression par grattage*
- strikethrough – *suppression par biffage*
- subpunction – *suppression par exponctuation*
- underline – *la suppression a été soulignée*

### @spanTo

Pointe vers le [@xml:id](#xml:id)  d'un point de terminaison

*Valeurs possibles*

- Référence à l'identifiant

## Exemples

### Exemple 1

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

## Sections des Guidelines de la TEI

- [11.3.1.4. Additions and Deletions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)