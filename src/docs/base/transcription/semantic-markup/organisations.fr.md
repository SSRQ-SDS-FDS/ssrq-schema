# Organisations et familles

## Balisage d'organisations et de familles

[`<orgName>`](orgName.fr.md) comprend une organisation (communauté, couvent, conseil, guilde, etc.)
ou un nom de famille, si possible dans le nominatif.

Les organisations, bien que le concept moderne ne signifie pas que les organismes ou les
institutions ainsi que les familles sont toujours récompensés dans les textes édités.
Si une organisation ou un nom de famille se produit plusieurs fois dans une section, il n'est
tagué qu'une seule fois.

Schöffen, Siebner, Stuhlsässen, Pfleger etc. ne sont pas attribués avec [`<orgName>`](orgName.fr.md).

## Différenciation entre l'organisation et le lieu

Ce doit être avec des termes tels que «Eidgenossenschaft» se distingue que ce soit une organisation
ou un nom géographique.
Pour la «Eidgenossenschaft» [`<placeName>`](placeName.fr.md) est utilisé, mais pour les
«Eidgenossen» [`<orgName>`](orgName.fr.md).
La «Eidgenossenschaft» est capitalisé dans l'édition tandis que le «Eidgenossen» comme organisation
ne sont pas capitalisé.

Lors de la dénomination de l'empire, il faut décider s'il s'agit de l'espace ou du territoire ou
de l'institution.

Si une personne apparaît dans une procédure judiciaire en tant que représentant autorisé, la
paroisse en tant qu'organisation de Kirchenossenschaft peut être étiquetée et la personne peut
être affectée à l'organisation dans la
[base de données personnelle](https://personae.ssrq-sds-fds.ch/).


Dès qu'un «lieu» se produit dans un conflit en tant que partie intérimaire, le parti doit être
reconnu comme une organisation et non comme un lieu.

Exemple :  
```
...spann und irrung wegen, so sich dann gehalten hand entzwischen baider
kilchspel <orgName>Bux</orgName> und <orgName>Sevellen</orgName>, ...
```

Aux lieux au sein des organisations voir aussi [lieux et espaces](places.fr.md).

## Enregistrement de la base de données

Chaque organisation nouvellement enregistrée reçoit un type d'organisation.

Chaque personne appartient à une famille (organisation).
Les épouses sont généralement acceptées sous le nom de son mari et, si elles sont connues,
également sous celle de son père.

Les évêques et les abbés sont répertoriés non seulement sous leur nom de famille, mais aussi sous
la convention de diocèse ou de monastère correspondant.

Groupes de personnes, comme  Winterthur ou Zurich, sont tagués dans les unités d'édition SDS ZH de
simplicité comme [`<placeName>`](placeName.fr.md).
Dans ce cas, les autres unités d'édition sont attribuées [`<orgName>`](orgName.fr.md) et selon la
valeur du groupe de résidents, coopérative, etc.