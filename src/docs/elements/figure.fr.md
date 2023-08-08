---
title: figure
---



# `<figure/>` (figure)

## Description

Contient des éléments qui décrivent des informations graphiques.

## Explication

Contient des signes notariés (= signe notarié, sceau notarié, signum), des dessins à la plume, des gravures sur bois, des signes de référence ou, dans le cas de copies d'actes, l'endroit où se trouve le sceau dans l'acte original (L. S. = Locus sigilli) ou des illustrations commençant par [`<graphic/>`](graphic.md)  être référencé.

## Modèle de contenu

- **core**: [graphic](graphic.md) [head](head.md)

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

### @type

Affectation obligatoire à un type

*Valeurs possibles*

- copper_engraving – *gravure sur cuivre*
- drawing – *dessin à la plume*
- illustration – *figure*
- locus_sigilli – *locus sigilli*
- monogram – *monogramme*
- notarial_sign – *seing/signe notarial*
- sign – *signe de renvoi*
- stamp – *tampon*
- woodcut – *xylographie*

## Exemples

### Exemple 1

Exemple d'enseigne notariale

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <signed>
        <figure type="notarial_sign" />
        <lb />Et ego Hainricus Jacobi de Augiamaiori ...
        </signed>
</egXML>
               
```

### Exemple 2

Exemple d'arbre généalogique

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <figure type="illustration">
        <graphic type="familytree" mimeType="image/svg" url="WB_HB.svg" />
        <head>Graphik 1: Stammbaum der Grafen von Werdenberg-Heiligenberg</head>
    </figure>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [14.4. Specific Elements for Graphic Images](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/FT.html#FTGRA)