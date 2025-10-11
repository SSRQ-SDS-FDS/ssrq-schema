# Scribes et mains

## Mains

Pour chaque main, un élément [`<handNote/>`](handNote.fr.md) est créé,
qui contient les informations sur la main et le scribe respectif.

Le `xml:id` de cet élément est référencé avec l’attribut `@hand` ;
voir les exemples de [`<add>`](add.fr.md).

## Attribuer une main à un scribe

Si une main peut être attribuée à un scribe connu par son nom, 
cette dernière doit être relié, dans l’élément [`<handNote/>`](handNote.fr.md), 
à l’entrée correspondante dans la base de données des personnes 
(cf. [personnes](persons.fr.md)).

## Classification des mains

Une main peut être classée selon qu’elle appartient ou non aux mains principales.

Les mains principales sont : `firstHand`, `secondHand` … `ninthHand`. 
Une autre main reçoit l’identifiant `otherHand`, et une main postérieure 
l’identifiant `laterHand`.

Dans l’édition numérique, les interventions éditoriales d’une main postérieure 
sont reproduites dans les notes, tandis que celles d’une main principale ou 
d’une autre main apparaissent dans le texte édité.

On peut aussi indiquer avec `@hand`, le siècle auquel appartient la main : 
`hand10c`, `hand11c`, … `hand21c`.

Si le siècle est incertain, cela s’exprime ainsi :
`hand10cf`, `hand11cf`, … `hand21cf`.
