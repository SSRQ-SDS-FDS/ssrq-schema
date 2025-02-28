# Scribes et mains

## Mains

Pour chaque main, un élément [`<handNote/>`](handNote.fr.md) est créé,
qui contient les informations sur la main respective ou sur le scribe respectif.

Le `xml:id` de cet élément est référencé avec l’attribut `@hand`,
voir les exemples de [`<add>`](add.fr.md).

## Attribuer une main à un scribe

Si une main peut être attribuée à un écrivain connu, celle-ci est liée
à l’entrée correspondante dans la base de données des personnes dans
l’élément [`<handNote/>`](handNote.fr.md) (cf. [personnes](persons.fr.md)).

## Classification des mains

Une main peut être classée selon qu’elle est majeure ou non.

Les mains principales sont `firstHand`, `secondHand` ... `ninthHand`,
une autre main a l’identifiant `otherHand`,
une main ultérieure a l’identifiant `laterHand`.

Dans l’édition numérique, les interventions éditoriales d’une main ultérieure
sont reflétées dans les notes, tandis que celles d’une main principale ou
d’une autre main apparaissent dans le texte édité.

Alternativement, le siècle de la main peut être spécifié avec `@hand` :
`hand10c`, `hand11c`, ... `hand21c`.

Si le siècle est incertain, cela s’exprime ainsi :
`hand10cf`, `hand11cf`, ... `hand21cf`.
