# Structure de texte

## Divisions et paragraphes

=== "Structure du texte édité"

    La structure de la source est utilisée comme modèle.

    Les paragraphes originaux sont balisés avec [`<p>`](p.fr.md). 
    En règle générale, ces paragraphes doivent commencer après
    un point et non après une virgule.

    Si un original présente une structuration ou une segmentation 
    plus marquée, on peut utiliser [`<div>`](div.fr.md) pour signaler 
    de plus grandes sections.

    Si la structuration avec [`<p>`](p.fr.md) et [`<div>`](div.fr.md) 
    n’est pas suffisante, l’éditeur peut diviser davantage les sections 
    ou paragraphes selon des critères de contenu en utilisant [`<seg>`](seg.fr.md).

    Lorsque cela semble nécessaire pour une meilleure compréhension, 
    le texte est subdivisé à l’aide d’alinéas et d’une numérotation 
    des paragraphes entre crochets, du centrage des titres, etc.
    
    Les chartes doivent être structurées selon leur structure formelle 
    (cf. [Diplomatik (dt.)](http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html), 
    [Notions de diplomatique (frz.)](http://theleme.enc.sorbonne.fr/cours/diplomatique)).

    Les formules finales des actes commençant par « actum » sont traitées 
    comme des paragraphes. Après « actum » vient « coram consilio », 
    « coram senatu », « presentibus », etc., suivi d’une virgule. 
    Un point est placé à la fin de ces formules (cf. 
    [ponctuation](punctuation.fr.md)).

=== "Structure des paratextes éditoriaux"

    Pour les paratextes plus longs (introduction, commentaire), les chapitres peuvent 
    être numérotés avec [`<div>`](div.fr.md) et, si nécessaire, décrits plus en détail. 

    Le texte d’un commentaire est structuré en paragraphes avec [`<p>`](p.fr.md) 
    à l’intérieur d’un [`<div>`](div.fr.md).

## Pages, colonnes et lignes

Dans l’édition imprimée, les sauts de ligne étaient représentés par `/` 
et les sauts de page par `//`.

Dans l’édition numérique, les lignes sont marquées par [`<lb/>`](lb.fr.md) 
(à partir de la première ligne). 
Les débuts de colonnes sont marqués par [`<cb/>`](cb.fr.md) 
et les débuts de pages par [`<pb/>`](pb.fr.md).

## Titre et sous-titres

Les titres et sous-titres originaux et ceux insérés par l’éditeur 
sont balisés avec [`<head>`](head.fr.md).

## Discours direct et citations

=== "dans le texte édité"

    Le discours direct, qui était mis en évidence par « … » dans l’édition imprimée, 
    est indiqué avec [`<q>`](q.fr.md) dans l’édition numérique.
    
    Les citations faisant partie de l’original (par exemple les chartes insérées) 
    sont balisées avec [`<quote>`](quote.fr.md) et suivies d’une note critique avec
    [`<note>`](note.fr.md) dans laquelle il est fait référence au texte original cité.

    Si le texte original a été édité, on peut se référer directement 
    à la pièce plutôt que de faire une note.

=== "dans les paratextes éditoriaux"

    Dans les paratextes éditoriaux (notes, commentaires, introduction),
    nous utilisons [`<quote>`](quote.fr.md) pour les citations issues 
    de la littérature scientifique.

## Tableaux

Certaines sources, comme les comptes ou les réglementations douanières, 
contiennent des tableaux qui doivent être reproduits comme tels dans l’édition. 

Pour représenter les tableaux, nous utilisons [`<table>`](table.fr.md)
en combinaison avec [`<row>`](row.fr.md) et [`<cell>`](cell.fr.md).

## Repli

Si un document contient un repli (pli du parchemin au bas d’un acte), 
balisé avec [`<ab>`](ab.fr.md), les règles suivantes s’appliquent :

- Le texte sous le repli est transcrit comme faisant partie du recto. 
- Le texte sur le repli est également transcrit comme faisant partie 
  du recto (même si matériellement, il devrait en fait appartenir à la page verso). 
- L’ordre du texte sous et sur le repli dans la transcription est égal. 