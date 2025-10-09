# Lieux et espaces

## Balisage des lieux et des espaces

Les lieux et les espaces sont toujours mis en évidence dans le texte édité. 
Si un lieu apparaît à plusieurs reprises dans une source ou, dans le cas 
de sources plus longues, dans une même section, il n’est généralement 
indiqué qu’une seule fois, à l’exception des variantes graphiques.

[`<placeName>`](placeName.fr.md) comprend la désignation d’un lieu ou d’un toponyme, 
si possible au nominatif. Seul le lieu est balisé, sans informations 
supplémentaires par exemple l’office, la tour, l’église, etc. 
Les maisons, les portes de la ville, les auberges, les moulins, etc. 
sans désignations plus détaillées ne sont pas balisées avec [`<placeName>`](placeName.fr.md), 
mais devraient être marquées avec [`<term>`](term.fr.md).

## Lieux comportant des noms de personnes ou de famille

Les biens nommés selon des noms de personnes, p. ex. « le champ de Heini Rütiner », 
ne sont enregistrés comme des lieux que s’il est possible d’identifier ces biens 
comme appartenant à la personne ou la famille mentionnée ; c’est-à-dire des toponymes. 
Si ce n’est pas le cas, seule la personne ou la famille est indiquée.

## Lieux dans un nom d’organisation

Les lieux qui peuvent être attribués à une organisation et qui ont déjà été balisés dans 
[`<orgName>`](orgName.fr.md) n’ont pas besoin d’être balisés avec [`<placeName>`](placeName.fr.md).

Dans le cas de noms de lieux utilisés en tant qu’adjectifs dans les commentaires et les notes, 
l’endroit n’a pas besoin d’être balisé avec [`<placeName>`](placeName.fr.md).
L’ID [`<orgName>`](orgName.fr.md) ou [`<persName>`](persName.fr.md) en tant qu’instrument d’identification suffit. 
L’éditeur décide s’il veut écrire « le Conseil de la ville de Zurich » 
ou « le Conseil de Zurich ».

Exemples :  
 `des Klosters <placeName ref="loc007756">Selnau</placeName>` – lieu avec ID du monastère de Selnau
à Zurich  
`<orgName ref="org000001">gotzhus ze Pfaͤvers</orgName>`  
`der Zürcher Bürger <persName>Hensli Müller</persName> ...`  
`der <orgName>Winterthurer Rat</orgName> beschloss... `

## Lieux dans des noms de personnes
Pour les lieux présents dans des noms de personnes ou de famille, voir [personnes](persons.fr.md).

## Enregistrement de la base de données

Les noms de lieux sont intégrés à la [base de données des noms de lieux historiques](https://loci.ssrq-sds-fds.ch)
sur la base de leur affiliation administrative et politique actuelle : 
pays, canton, commune/partie de commune.

De plus, la catégorie du nom de lieu est indiquée, p. ex. alpage, ruisseau, seigneurie, etc., 
toujours d’après la source.

Dans la mesure du possible, un nom de lieu est relié à d’autres bases de données (par exemple 
[ortsnamen.ch](https://ortsnamen.ch/)).
