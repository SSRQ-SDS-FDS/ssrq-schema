# Personnes

## Balisage des noms de personnes

Dans un texte édité, les noms de personnes sont toujours balisés. 
Si une personne apparait plusieurs fois dans un même paragraphe, 
elle n’est taguée qu’une seule fois avec [`<persName>`](persName.fr.md). 
[`<persName>`](persName.fr.md) comprend, si possible un nom de personne 
au nominatif. Seul le nom est balisé, sans informations
supplémentaires telles que profession, titre, etc.

## Noms composés

Dans le cas des noms de personnes composés, il faut décider quelle partie sera inclus dans
[`<persName>`](persName.fr.md).

Lors de l’atelier SDS du 24 août 2017, nous avons décidé que pour les abbés,
le prénom serait balisé avec [`<persName>`](persName.fr.md) et le lieu avec [`<placeName>`](placeName.fr.md).

Dans la [base de données des personnes](https://personae.ssrq-sds-fds.ch/) 
l’abbé est rattaché à sa fonction d’abbé du couvent (= organisation), 
et cette organisation est liée au lieu où il se trouve.

Les fonctions et les titres sont saisis dans la 
[base de données des personnes](https://personae.ssrq-sds-fds.ch/), 
accompagnés d’une datation.

Exemples :  
`Abt <persName>Johann</persName> von <placeName>Pfäffers</placeName>`  
`<persName>Johans</persName>, abt von <placeName>Pfävers</placeName>`

## Lieux dans les noms de personnes

Dans le cas des noms composés où il est clair que « von NN » est 
un nom de famille et non une désignation d’origine, l’ensemble 
du nom est inscrit dans [`<persName>`](persName.fr.md).

Les lieux dans ces noms composés ne sont balisés que s’il n’est pas 
certain qu’il s’agisse d’un nom de famille ou d’une désignation d’origine. 
Au Moyen Âge, les noms de famille ne sont souvent pas encore formés 
et l’attribution peut être incertaine.

Exemple :  
`<persName>Hans Ulrich von Ems</placeName>` vs.  
`<persName>Hans von <placeName>Gümmlingen</placeName></persName>`

## Affectation incertaine des personnes

Si, dans un texte, il n’est pas clair si une personne est, 
p. ex. Guillaume V (1434, 1439) ou Guillaume VIII (1462, 1483), 
une note critique de contenu [`<note>`](note.fr.md) est ajoutée, 
dans laquelle les deux personnes sont mentionnées. 
Ces deux personnes peuvent alors être balisées séparément et intégrées 
à la [base de données des personnes](https://personae.ssrq-sds-fds.ch/).

Si des personnes portent le même prénom et/ou le même nom – p. ex. père et son fils –, 
leur identité n’est supposée qu’en cas de forte probabilité. 
Les critères principaux sont : rareté du nom ou du prénom, 
noms supplémentaires correspondants, proximité temporelle, 
concordance de la profession/charge/fonction et du lieu de résidence/origine, 
bien que tous les critères ne doivent pas s’appliquer à chaque fois. 
En cas de doute, une remarque est faite dans la 
[base de données](https://personae.ssrq-sds-fds.ch/), 
ou alors les personnes sont enregistrées individuellement. 
Il est donc possible que deux entrées séparées de personnes portant 
les mêmes noms et prénoms dans la [base de données](https://personae.ssrq-sds-fds.ch/) 
désignent en réalité la même personne. 
Des recherches plus poussées pourraient conduire à des corrections.

## Saisie dans la base de données																	

Les noms de personnes et de familles sont répertoriés selon leur orthographe actuelle, 
conformément au Dictionnaire historique de la suisse ([DHS](https://hls-dhs-dss.ch/de/)), 
à [HBLS](https://www.digibern.ch/katalog/historisch-biographisches-lexikon-der-schweiz) 
et au « [Familiennamenbuch der Schweiz](https://hls-dhs-dss.ch/famn/?pagename=famn2) ». 
Les noms non répertoriés dans ces ouvrages sont normalisés par l’éditeur. 
L’absence d’un nom de famille ou d’un prénom est signalée comme l’abréviation 
« NN » (« Nomen nominandum »). Les prénoms abrégés, tels que « Jörg » ou « Trina », 
sont en principe normalisés vers les formes usuelles (« Georg » ou « Katharina »), 
à l’exception des abréviations dont la forme développée ne peut pas être déduite 
à partir des outils linguistiques.

Pour une femme mariée, si le nom de jeune fille et le nom de mariage sont connus, 
elle est enregistrée sous les deux.

Les religieux (évêques, abbés, moines, etc.) sont répertoriés non seulement sous 
leur nom de famille, mais aussi sous l’institution correspondante. 
Ces institutions apparaissent toujours sous une forme normalisée, ainsi que les 
noms de famille de nobles pour lesquels seul le prénom est mentionné, mais dont 
le nom de famille est connu.

Les saints et les personnages bibliques, généralement connus uniquement par leur prénom, 
sont enregistrés sous celui-ci.

Les dynasties nobles (comtes, petite noblesse) sont numérotées selon les éditions 
précédentes ou des généalogies fiables. 
En cas de doute, aucune numérotation n’est donnée.

L’année indiquée pour les personnes et les familles correspond 
à leur première mention ; parfois, l’année de leur dernière mention 
est mentionnée ensuite. Pour faciliter l’identification, en particulier 
des personnes connues, les dates de vie sont ajoutées conformément 
aux ouvrages et lexiques généalogiques de référence. Si possible, 
les personnes reçoivent des identifiants normalisés ([GND](https://lobid.org/gnd), 
[DHS](https://hls-dhs-dss.ch/de/), etc.) et sont reliées à [metagrid.ch](https://metagrid.ch/).

Les informations sur les professions, charges et fonctions, ainsi que les lieux d’activité, 
se réfèrent aux données présentes dans les sources éditées, tout comme les informations 
supplémentaires sur les liens de parenté.
