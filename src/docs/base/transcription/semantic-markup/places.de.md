# Orte und Räume

##Auszeichnung von Orten und Räumen
Orte und Räume  werden im edierten Text  immer ausgezeichnet. Kommt ein Ort innerhalb eines Stücks oder – bei umfangreichen Quellen – innerhalb eines Abschnitts wiederholt vor, wird er mit Ausnahme der Schreibvarianten in der Regel nur einmal ausgezeichnet.

 [`<placeName>`](placeName.de.md) umfasst eine Ortsbezeichnung oder einen Flurnamen, wenn möglich im Nominativ. Es wird nur der Ort ohne zusätzliche Informationen, wie Amt, Turm, Kirche etc., ausgezeichnet. Häuser, Stadttore, Gasthäuser, Mühlen usw. ohne nähere Bezeichnung werden nicht mit [`<placeName>`](placeName.de.md), sollten aber mit  [`<term>`](term.de.md)  ausgezeichnet werden.

## Orte mit Personen- oder Familiennamen
Güter, die über Personen identifiziert werden, z. B. «Heini Rütiners acker», werden nur dann als Ort ausgezeichnet, wenn es sich um ein identifizierbares Gut einer genannten Person oder einer genannten Familie, d. h. um einen Flurnamen, handelt. Wenn dies nicht der Fall ist, wird nur die Person bzw. die Familie ausgezeichnet.

##Orte in einer Organisationsbezeichnung
Orte, die einer Organisation zugeordnet werden können und sich innerhalb eines  [`<orgName>`](orgName.de.md) befinden, müssen nicht zusätzlich mit  [`<placeName>`](placeName.de.md)  ausgezeichnet werden. 

Bei adjektivisch verwendeten Ortsnamen in Kommentaren und Anmerkungen muss der Ort nicht mit [`<placeName>`](placeName.de.md)  ausgezeichnet werden. Die ID bei [`<orgName>`](orgName.de.md)  bzw.  [`<persName>`](persName.de.md) als Instrument der Identifikation reicht. Dem Bearbeitenden ist überlassen, ob sie/er «der Rat der Stadt Zürich» oder «der Zürcher Rat» schreibt.


Beispiele:    
 `des Klosters <placeName ref="loc007756">Selnau</placeName>  – Ort mit ID des Klosters Selnau in Zürich`
 
`  <orgName ref="org000001">gotzhus ze Pfaͤvers</orgName> `
  
 `der Zürcher Bürger <persName>Hensli Müller</persName> ... ` 

`der <orgName>Winterthurer Rat</orgName> beschloss... ` 

##Orte innerhalb von Personennamen
Zu Ortsnamen innerhalb von Personennamen vgl. [Personen](persons.de.md).

##Datenbankerfassung

 Die Ortsnamen werden anhand der heutigen administrativen und politischen Zugehörigkeit in die [«SSRQ Datenbank historischer Ortsnamen»](https://www.ssrq-sds-fds.ch/places-db-edit/search/search-form.xq) aufgenommen: Land, Kanton, Gemeinde/Gemeindeteil. Zudem wird  die Kategorie des Ortsnamens (z. B. Alp, Bach, Herrschaft usw.), die immer auf der Quelle fusst, erfasst. Wenn möglich wird ein Ort mit weiteren Daten (z. B. [ortsnamen.ch](https://ortsnamen.ch/de/)) verknüpft.

