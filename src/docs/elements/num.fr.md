---
title: num
---



# `<num/>` (numéral)

## Description

Contient un nombre dans le texte source transcrit.

## Explication

La valeur du nombre est stockée sous une forme lisible par machine dans l'attribut [@value](#value).

Dans le cas d'informations sur les dimensions, les poids, les devises, etc., dans lesquelles [`<measure/>`](measure.md)  est utilisé pour marquer le nombre avec[@quantity](#quantity),[`<num/>`](num.md)  n'est pas utilisé. De même,[`<num/>`](num.md)  n'est pas utilisé pour les années qui sont décrites plus en détail avec[`<origDate/>`](origDate.md)  et[@when](#when). Dans une spécification de temps avec[@dur](#dur),[`<num/>`](num.md)  n'est pas utilisé.

## Modèle de contenu

- **core**: [hi](hi.md) [lb](lb.md) [pb](pb.md)
- Contenu de texte au choix

## Attributs

### @value

Valeur numérique en chiffres arabes

*Valeurs possibles*

- Nombre à virgule flottante
- Nombre

## Exemples

Aucun exemple pour la langue sélectionnée.

## Sections des Guidelines de la TEI

- [3.6.3. Numbers and Measures](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONANU)