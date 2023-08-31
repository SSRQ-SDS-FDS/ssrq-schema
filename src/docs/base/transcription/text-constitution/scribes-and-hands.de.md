# Schreiber und Hände

## Hände

Für jede Hand wird ein [`<handNote/>`](handnote.de.md)-Element angelegt, 
welches die Informationen zum jeweiligen Schreiber enthält.

Auf die `xml:id` dieses Elements wird mit dem Attribut `@hand` verwiesen,
vgl. die Beispiele von [`<add>`](add.de.md).

## Zuordnung einer Hand zu einem Schreiber

Kann eine Hand einem namentlich bekannten Schreiber zugeordnet werden,
wird dieser in dem [`<handNote/>`](handnote.de.md)-Element mit dem 
entsprechenden Eintrag in der Personendatenbank verknüpft.

## Klassifikation der Hände

Eine Hand kann danach klassifiziert werden, ob sie zu den Haupthänden gehört
oder nicht:

Haupthände sind: `firstHand, secondHand ... ninthHand`,
eine andere Hand hat die Kennung: `otherHand`,
eine spätere Hand die Kennung: `laterHand`.

Dabei gilt, dass in der digitalen Edition die redaktionellen Eingriffe einer 
späteren Hand in den Anmerkungen wiedergegeben werden, während solche einer 
Haupthand oder einer anderen Hand im edierten Text erscheinen.

Alternativ kann mit `@hand` auch das Jahrhundert der Hand angegeben werden: 
`hand10c, hand11c, ... hand21c`.

Ist das Jahrhundert unsicher, wird dies folgendermassen ausgedrückt: 
`hand10cf, hand11cf, ... hand21cf`.