# Organisationen und Familien

## Auszeichnung von Organisationen und Familien

[`<orgName>`](orgName.de.md) umfasst eine Organisation (Bürgergemeinde,
Konvent, Rat, Zunft etc.) oder einen Familiennamen, wenn möglich im Nominativ.

Organisationen, wobei nicht der moderne Begriff gemeint ist, Körperschaften
oder Institutionen sowie Familien werden in den edierten Texten immer
ausgezeichnet.
Kommt eine Organisation oder ein Familienname in einem Abschnitt mehrmals vor,
wird er nur einmal getaggt. 

Schöffen, Siebner, Stuhlsässen, Pfleger usw. werden nicht mit
[`<orgName>`](orgName.de.md) ausgezeichnet.

## Unterscheidung zwischen Organisation und Ort

Es muss bei Begriffen wie z. B. «Eidgenossenschaft» unterschieden werden,
ob es sich um eine Organisation oder um eine geographische Bezeichnung handelt.
Für die «Eidgenossenschaft» wird [`<placeName>`](placeName.de.md) verwendet,
für die «Eidgenossen» hingegen [`<orgName>`](orgName.de.md).
Die «Eidgenossenschaft» wird in der Edition grossgeschrieben, während die
«Eidgenossen» als Organisation kleingeschrieben werden.

Bei der Nennung des Reichs muss entschieden werden, ob es sich um den Raum
bzw. das Territorium oder um die Institution handelt.

Wenn eine Person als Bevollmächtigte eines Kirchspiels in einem
Rechtsverfahren auftritt, dann ist das Kirchspiel als Organisation
Kirchgenossenschaft zu taggen und die Person ist in der
[Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/) als
Gesandter der Organisation zuzuordnen.

Sobald ein «Ort» in einem Konflikt als handelnde Partei auftritt,
sollte die Partei als Organisation und nicht als Ort ausgezeichnet werden.

Beispiel:  
```
...spann und irrung wegen, so sich dann gehalten hand entzwischen baider
kilchspel <orgName>Bux</orgName> und <orgName>Sevellen</orgName>, ...
```

Zu Orten innerhalb von Organisationen vgl. [Orte und Räume](places.de.md).

## Datenbankerfassung

Jede Organisation, die neu aufgenommen wird, erhält zwingend einen
Organisationstyp.

Jede Person gehört einer Familie (Organisation) an.
Ehefrauen werden in der Regel unter dem Namen ihres Mannes und,
wenn bekannt, auch unter demjenigen ihres Vaters aufgenommen.

Bischöfe und Äbte werden nicht nur unter ihrem Familiennamen,
sondern auch unter dem entsprechenden Bistum bzw. Klosterkonvent aufgeführt.

Gruppen von Personen, wie z. B. Winterthurer oder Zürcher, werden in den
Editionseinheiten SSRQ ZH der Einfachheit halber als 
[`<placeName>`](placeName.de.md) getaggt.
In den anderen Editionseinheiten wird in diesem Fall mit
[`<orgName>`](orgName.de.md) ausgezeichnet und je nach Wertigkeit
der Gruppe der Bewohnerschaft, Genossenschaft etc. zugeordnet.
