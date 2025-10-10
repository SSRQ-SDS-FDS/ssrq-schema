# Organisations et familles

## Balisage d’organisations et de familles

[`<orgName>`](orgName.fr.md) englobe les organisations (communautés, couvents, 
conseils, guildes, etc.) et les noms de famille, si possible au nominatif.

Les organisations, les corporations ou les institutions ainsi que les familles
sont toujours balisées dans les textes édités. Lorsqu’une organisation ou un
nom de famille apparaît plusieurs fois dans un même paragraphe, il n’est tagué
qu’une seule fois.

Les échevins (Schöffen), « Siebner », juges (Stuhlsässen), administrateurs (Pfleger), etc. 
ne sont pas balisés avec [`<orgName>`](orgName.fr.md).

## Distinction entre organisation et lieu

Pour des notions telles que « Eidgenossenschaft », il faut distinguer s’il s’agit
d’une organisation ou d’un nom géographique. Pour « Eidgenossenschaft », on utilise 
[`<placeName>`](placeName.fr.md) , mais pour les « Eidgenossen », [`<orgName>`](orgName.fr.md).
« Eidgenossenschaft » prend une majuscule dans l’édition tandis que les « Eidgenossen », 
en tant qu’organisation sont écrits avec une minuscule.

Pour ce qui est de la dénomination « Empire/Reich » il faut décider s’il 
s’agit de l’espace/du territoire ou de l’institution.

Si une personne apparaît dans une procédure judiciaire en tant
que représentant d’une paroisse, celle-ci doit être balisée
comme une organisation (communauté paroissiale) et la personne
doit être intégrée à la [base de données des personnes](https://personae.ssrq-sds-fds.ch/) 
comme envoyée de l’organisation.

Lorsqu’un « lieu » apparait dans un conflit comme un protagoniste du conflit, 
il doit être balisé comme une organisation et non comme un lieu.

Exemple :  
```
… spann und irrung wegen, so sich dann gehalten hand entzwischen baider
kilchspel <orgName>Bux</orgName> und <orgName>Sevellen</orgName>, …
```

Pour des lieux à l’intérieur d’organisations, voir [lieux et espaces](places.fr.md).

## Enregistrement dans la base de données

Chaque organisation nouvellement enregistrée reçoit un type d’organisation.

Chaque personne appartient à une famille (organisation). 
Les épouses sont généralement enregistrées sous le nom de leur mari et, 
si connu, également sous celui de leur père.

Les évêques et les abbés sont répertoriés non seulement sous leur
nom de famille, mais aussi sous le diocèse ou le couvent correspondant.

Les groupes de personnes, p. ex. les Winterthourois ou les Zurichois, 
sont tagués dans les unités d’édition SDS ZH comme [`<placeName>`](placeName.fr.md), 
par souci de simplicité. Dans les autres éditions, ces noms sont attribués 
avec [`<orgName>`](orgName.fr.md) et organisés selon l’importance du groupe
d’habitants, de la communauté, etc.
