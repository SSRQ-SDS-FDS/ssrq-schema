### 8.5 Klassifikation von Schreibern

Für jeden Schreiber wird ein [`<handNote/>`](../../elements/handnote.de.md)-Element angelegt, welches die Informationen
zum jeweiligen Schreiber enthält.
Auf die ID dieses Elements wird mit dem Attribut `@hand` verwiesen.
Kann eine Hand einem namentlich bekannten Schreiber zugeordnet werden, wird dieser mithilfe des Attributs `@scribe`
mit dem entsprechenden Eintrag in der Personendatenbank verknüpft.

Eine Hand kann danach klassifiziert werden, ob sie zu den Haupthänden gehört oder nicht:
Haupthände: `firstHand, secondHand ... ninthHand`, andere Hand: `otherHand`, spätere Hand: `laterHand`.
Dabei gilt, dass in der digitalen Edition die redaktionellen Eingriffe einer späteren Hand in den Anmerkungen
wiedergegeben werden, während solche einer Haupthand oder einer anderen Hand im Editionstext erscheinen.

Alternativ kann mit `@hand` auch das Jahrhundert der Hand angegeben werden: `hand10c, hand11c, ... hand21c`.
Ist das Jahrhundert unsicher, wird dies folgendermassen ausgedrückt: `hand10cf, hand11cf, ... hand21cf`.