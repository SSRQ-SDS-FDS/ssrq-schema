# Lieux et espaces

## Balisage de lieux et espaces

Les lieux et les chambres sont toujours décernés dans le texte édité.
Si un lieu se produit dans une pièce ou dans le cas de sources étendues dans une section, elle
n’est généralement attribuée qu’une seule fois à l’exception des variantes d’écriture.

[`<placeName>`](placeName.fr.md) comprend un nom de lieu ou un nom de champ, si possible dans
le nominatif.
Seul l’emplacement est attribué sans informations supplémentaires, telles que le bureau, la tour,
l’église, etc.
Les maisons, les portes de la ville, les auberges, les moulins, etc. sans désignations plus
détaillées ne sont pas [`<placeName>`](placeName.fr.md), mais devraient être attribuées avec
[`<term>`](term.fr.md).

## Lieux avec des noms personnels

Des biens identifiés via des personnes, par ex. B. "le champ de Heini Rütiner", n’est reconnu que
comme un endroit s’il s’agit d’un bien identifiable d’une personne mentionnée ou d’une famille
mentionnée, c’est-à-dire h. un nom de champ.
Si ce n’est pas le cas, seule la personne ou la famille est attribuée.

## Lieux dans un nom organisationnel

Les lieux qui peuvent être attribués à une organisation et qui se trouvent dans un
[`<orgName>`](orgName.fr.md) n’ont pas à être attribué avec [`<placeName>`](placeName.fr.md).

Dans le cas des noms de lieux adjectifs dans les commentaires et les commentaires, l’endroit n’a
pas à être attribué avec [`<placeName>`](placeName.fr.md).
L’ID à [`<orgName>`](orgName.fr.md) ou [`<persName>`](persName.fr.md) comme instrument
d’identification. Le montage est laissé à savoir s’il rédige "le Conseil de la ville de Zurich" ou
"le Conseil de Zurich".

Exemples :  
 `des Klosters <placeName ref="loc007756">Selnau</placeName>` – lieu avec ID du monastère de Selnau
à Zurich  
`<orgName ref="org000001">gotzhus ze Pfaͤvers</orgName>`  
`der Zürcher Bürger <persName>Hensli Müller</persName> ...`  
`der <orgName>Winterthurer Rat</orgName> beschloss... `

## Lieux en noms personnels
Pour noms des lieux dans des noms personnels voir aussi [personnes](persons.fr.md).

## Enregistrement de la base de données

Les noms de lieux sont inclus dans la
[base de données des noms de lieux historiques](https://loci.ssrq-sds-fds.ch)
basés sur l’affiliation administrative et politique d’aujourd’hui : pays, canton,
municipalité/partie de municipalité.

De plus, la catégorie du nom du lieu (p. ex. alp, ruisseau, règle, etc.), qui fusionne toujours
sur la source, est enregistrée.

Si possible, un endroit est lié à d’autres données (par exemple
[ortsnamen.ch](https://ortsnamen.ch/)).
