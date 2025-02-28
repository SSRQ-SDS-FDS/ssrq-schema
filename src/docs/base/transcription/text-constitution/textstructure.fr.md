# Structure de texte

## Divisions et paragraphes

=== "Structure du texte édité"

    La structure du modèle d’édition est prise en charge.
    
    Les paragraphes originaux sont marqués par [`<p>`](p.fr.md).
    En règle générale, ces paragraphes doivent suivre un point et non une virgule.
    
    Si un original est plus structuré, vous pouvez utiliser [`<div>`](div.fr.md)
    pour marquer des sections plus grandes.
    
    Si la structure du texte avec [`<p>`](p.fr.md) et [`<div>`](div.fr.md)
    n’est pas suffisante, l’éditeur peut diviser davantage les divisions ou
    paragraphes selon des critères de contenu en utilisant [`<seg>`](seg.fr.md).
    
    Lorsque cela semble nécessaire à une meilleure compréhension, le texte est
    divisé à l’aide d’alignées et d’une numérotation paragraphe par paragraphe
    entre crochets, centrage des titres, etc.
    
    Les documents doivent être structurés selon leur structure formelle (cf.
    [Diplomatik (dt.)](http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html), 
    [Diplomatik (frz.)](http://theleme.enc.sorbonne.fr/cours/diplomatique).

    Les formules finales des documents commençant par «actum» sont traitées
    comme des paragraphes. Après «actum» vient «coram consilio», «coram senatu»,
    «presentibus», etc. après une virgule. Un point est inséré à la fin des formules
    (cf. [ponctuation](punctuation.fr.md)).

=== "Structure des paratextes éditoriaux"

    Pour les paratextes plus longs (introduction, commentaire), les chapitres peuvent
    être numérotés avec [`<div>`](div.fr.md) et, si nécessaire, décrits plus en détail. 
    
    Le texte d’un commentaire est structuré en paragraphes au sein de
    [`<div>`](div.fr.md) avec [`<p>`](p.fr.md).

## Pages, colonnes et lignes

Dans l’édition analogique, les changements de ligne étaient représentés par `/` 
et les changements de page par `//`.

Dans l’édition numérique, les lignes sont marquées au début par
[`<lb/>`](lb.fr.md) à partir de la première ligne. Le début des
colonnes est marqué par [`<cb/>`](cb.fr.md) et le début des pages
par [`<pb/>`](pb.fr.md).

## Titre et sous-titres

Les titres et sous-titres originaux et ceux insérés par l’éditeur
sont marqués de [`<head>`](head.fr.md).

## Discours direct et citations

=== "dans le texte édité"

    Le discours direct qui était mis en évidence par `«...»` dans l’édition
    analogique est marqué par [`<q>`](q.fr.md) dans l’édition numérique.
    
    Les citations dans un texte (par exemple les documents publiés) sont
    marquées avec [`<quote>`](quote.fr.md) et à la fin de la citation se
    trouve une note critique avec [`<note>`](note.fr.md) dans laquelle il
    est fait référence au texte original cité.

    Si le texte original a été édité, une référence peut être faite à la
    pièce au lieu d’une note.

=== "dans les paratextes éditoriaux"

    Dans les paratextes éditoriaux (notes, commentaires, introduction),
    nous utilisons [`<quote>`](quote.fr.md) pour les citations de la
    littérature de recherche.

## Tableaux

Certaines sources, comme les factures ou les réglementations douanières,
contiennent des tableaux qui sont également implémentés comme tels dans l’édition. 

Pour afficher les tableaux, nous utilisons [`<table>`](table.fr.md)
en combinaison avec [`<row>`](row.fr.md) et [`<cell>`](cell.fr.md).

## Plica

Si un document contient un Plica (balisé avec [`<ab>`](ab.fr.md)), 
alors les réglementations suivantes s’appliquent :

- Le texte sous la plica est transcrit dans le cadre de la page recto.
- Le texte sur la plica est également transcrit dans le cadre de la page recto
  (bien qu’étant donné le matériel, il devrait en fait appartenir à la page verso).
- L’ordre du texte sous ou sur la plica est arbitraire dans la transcription.