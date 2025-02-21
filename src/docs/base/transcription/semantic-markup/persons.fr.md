# Personnes

## Balisage de personnes

Les personnes sont toujours récompensés dans un texte édité.
Si une personne se produit plusieurs fois dans une section, elle n’est taguée qu’une seule fois
avec [`<persName>`](persName.fr.md).
[`<persName>`](persName.fr.md), si possible, comprenez un nom personnel dans le nominatif.
Seul le nom est attribué sans informations supplémentaires, telles que les titres d’emploi, les
titres, etc.

## Composé des noms personnels

Dans le cas des noms personnels composites, il faut décider quelle partie est composée avec 
[`<persName>`](persName.fr.md).

Dans le workshop SDS du 24 août 2017, nous avons décidé que le prénom avec
[`<persName>`](persName.fr.md) et le lieu comme [`<placeName>`](placeName.fr.md).

Dans la [base de données personnelle](https://personae.ssrq-sds-fds.ch/)
l’abbé est affecté au couvent (= organisation) via sa fonction d’abbé et que l’organisation est
liée à l’emplacement où il est situé.

Les fonctions et les titres sont enregistrés avec une datation parmi la personne de la
[base de données personnelle](https://personae.ssrq-sds-fds.ch/).

Exemples :  
`Abt <persName>Johann</persName> von <placeName>Pfäffers</placeName>`  
`<persName>Johans</persName>, abt von <placeName>Pfävers</placeName>`

## Lieux en noms personnels

Dans le cas des noms personnels composites, qui est clair que le «von NN» est un nom de famille et
non un nom de lieu, le nom personnel entier est composé avec [`<persName>`](persname.fr.md).

Les lieux dans les noms personnels ne sont excellents que s’il n’est pas certain que ce soit un
nom de famille ou une désignation d’origine.
Au Moyen Âge, les noms de famille ne sont souvent pas encore formés et la mission n’est pas sûre.

Exemple :  
`<persName>Hans Ulrich von Ems</placeName>` vs.  
`<persName>Hans von <placeName>Gümmlingen</placeName></persName>`

## Affectation incertaine des personnes

Si un texte n’indique pas s’il est p. ex. autour de Wilhelm V. (1434, 1439) ou Wilhelm VIII.
(1462, 1483), ensuite, une note de bas de page critique de caractère [`<note>`](note.fr.md) est
définie, dans laquelle les deux personnes sont nommées.
Les deux personnes peuvent désormais être attribuées séparément et incluses dans la 
[base de données personnelle](https://personae.ssrq-sds-fds.ch/).

Si les personnes apparaissent le même nom et/ou le même nom - par exemple père et un fils/fils -
Une identité n’est supposée que dans le cas d’une forte probabilité.
Les principaux critères d’identité sont la rareté des noms ou des prénoms, des noms supplémentaires
correspondants, la proximité du temps, la congruence du travail/du bureau/de la fonction et le lieu
de résidence/lieu d’origine, bien que tous les critères ne doivent pas s’appliquer.
En cas de doute, une remarque correspondante est faite dans la
[base de données personnelle](https://personae.ssrq-sds-fds.ch/)
ou les personnes sont enregistrées individuellement.
Il s’ensuit que les personnes répertoriées individuellement avec la même famille et les mêmes noms
peuvent être identiques à la [base de données personnelle](https://personae.ssrq-sds-fds.ch/),
même si elles sont répertoriées séparément.
Des recherches plus détaillées conduiraient éventuellement à des corrections ici.

## Enregistrement de la base de données																		

Les noms de personne et de famille sont répertoriés sous l’orthographe utilisée aujourd’hui 
conformément à [HLS](https://hls-dhs-dss.ch/de/),
[HBLS](https://www.digibern.ch/katalog/historisch-biographisches-lexikon-der-schweiz)
et [«Familiennamenbuch der Schweiz»](https://hls-dhs-dss.ch/famn/?pagename=famn2).
Les noms qui ne peuvent pas être attribués sont standardisés par le modifié.
L’absence d’un nom de famille ou d’un prénom est donnée comme l’abréviation «NN»
(«Nomen nominandum»).
Les prénoms raccourcis tels que «Jörg» ou «Trina» sont généralement normalisés pour les prénoms
communs («Georg» ou «Katharina») ;
Les exceptions sont des abréviations, dont la normalisation ne peut pas être développée à partir
des aides linguistiques.

Si le nom unique et le nom de famille pris par le mari sont connus pour une femme, elle est
enregistrée sous les deux.

Les parents d’institutions spirituelles telles que les évêques, les abbés, les moines, etc. sont
répertoriés non seulement sous leurs noms familiaux, mais aussi dans l’institution correspondante.
Ces institutions apparaissent toujours sous une forme normalisée, ainsi que des noms de famille de
nobles, dans lesquels seul le prénom est mentionné, le nom de famille est connu.

Des figures saintes et bibliques, généralement transmises uniquement avec les prénoms, sont
enregistrées sous cela.

Les dynasties nobles (comptes, nobles bas) sont numérotées conformément aux unités d’édition
précédentes ou aux généalogies fiables. En cas de doute, une numérotation est distribuée.

L’année ajoutée aux personnes et aux familles indique la première mention ; une partie de la
dernière mention suit également.
Pour faciliter l’identification, surtout les données de vie selon les travaux standard et les
lexiques spécifiés chez les personnes plus connues.
Si possible, les personnes reçoivent des données standard ([GND](https://lobid.org/gnd), 
[HLS](https://hls-dhs-dss.ch/de/) etc.) et liées à [metatrid.ch](https://metagrid.ch/).

Les inscriptions à nommer, les bureaux et les fonctions ainsi que les emplacements ainsi que les
emplacements concernent les informations dans les sources éditées, ainsi que les informations
supplémentaires sur les relations.
