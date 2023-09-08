# Personen

## Auszeichnung von Personen

Personen werden in einem edierten Text immer ausgezeichnet.
Kommt eine Person in einem Abschnitt mehrmals vor, wird sie nur einmal
mit [`<persName>`](persName.de.md) getaggt.
[`<persName>`](persName.de.md) umfasst einen Personennamen wenn möglich
im Nominativ.
Es wird nur der Name ohne zusätzliche Informationen, wie Berufsbezeichnung,
Titel etc., ausgezeichnet. 

## Zusammengesetzte Personennamen

Bei zusammengesetzten Personennamen ist zu entscheiden, welcher Teil mit
[`<persName>`](persName.de.md) umfasst wird.

Im SSRQ-Workshop vom 24. August 2017 haben wir entschieden, dass bei Äbten
der Vorname mit [`<persName>`](persName.de.md) und der Ort als
[`<placeName>`](placeName.de.md) ausgezeichnet wird.

In der [Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/)
wird der Abt durch seine Funktion als Abt dem Konvent (=Organisation)
zugeordnet und die Organisation wird mit dem Ort verknüpft, an dem sie
sich befindet.

Funktionen und Titel werden zusammen mit einer Datierung bei der Person in
der [Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/) erfasst.

Beispiele:  
`Abt <persName>Johann</persName> von <placeName>Pfäffers</placeName>`
`<persName>Johans</persName>, abt von <placeName>Pfävers</placeName>`

## Orte innerhalb von Personennamen

Bei zusammengesetzten Personennamen, bei denen es klar ist, dass es sich
beim «von NN» um einen Nachnamen und nicht um eine Ortsbezeichnung handelt,
wird der ganze Personenname mit [`<persName>`](persName.de.md) umfasst.

Orte innerhalb von Personennamen werden nur ausgezeichnet, wenn nicht
sicher ist, ob es sich um einen Nachnamen oder eine Herkunftsbezeichnung
handelt. 
Im Mittelalter sind die Nachnamen oftmals noch nicht ausgebildet und die
Zuordnung ist unsicher.

Beispiel:  
`<persName>Hans Ulrich von Ems</placeName>` vs.  
`<persName>Hans von <placeName>Gümmlingen</placeName></persName>`

## Unsichere Zuordnung von Personen

Was macht man, wenn aus einem Text nicht hervorgeht, ob es sich z. B. um
Wilhelm V. (1434, 1439) oder Wilhelm VIII. (1462, 1483) handelt? –
Es wird eine sachkritische Fussnote [`<note>`](note.de.md) gesetzt,
in der beide Personen namentlich genannt werden.
Die beiden Personen können nun separat ausgezeichnet und in die
[Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/)
aufgenommen werden.

Wenn Personen gleichen Namens und/oder Vornamens vorkommen – z. B. Vater
und Sohn/Söhne –, wird eine Identität nur bei grosser Wahrscheinlichkeit
angenommen. 
Hauptkriterien für die Identität sind Seltenheit der Namen oder Vornamen,
übereinstimmende Zusatznamen, zeitliche Nähe, Kongruenz von Beruf/Amt/Funktion
und Wohn-/Herkunftsort, wobei jeweils nicht alle Kriterien zutreffen müssen.
In Zweifelsfällen erfolgt eine entsprechende Bemerkung in der
[Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/) oder die
Personen werden einzeln aufgenommen.
Daraus folgt, dass einzeln aufgeführte Personen mit gleichem Familien- und
Vornamen in der
[Personendatenbank](https://www.ssrq-sds-fds.ch/persons-db-edit/) identisch
sein können, obwohl sie separat aufgeführt sind.
Eingehendere Forschungen würden hier möglicherweise zu Berichtigungen führen.

## Datenbankerfassung																		

Die Personen- und Familiennamen sind unter der heute gebräuchlichen
Schreibweise gemäss [HLS](https://hls-dhs-dss.ch/de/),
[HBLS](https://www.digibern.ch/katalog/historisch-biographisches-lexikon-der-schweiz)
und dem
[«Familiennamenbuch der Schweiz»](https://hls-dhs-dss.ch/famn/?pagename=famn2)
aufgeführt.
Namen, die sich dort nicht zuordnen lassen, sind von den Bearbeitenden
standardisiert worden.
Das Fehlen eines Familiennamens oder eines Vornamens wird mit der Abkürzung
«NN» («Nomen nominandum») angegeben. 
Verkürzte Vornamen wie «Jörg» oder «Trina» werden in der Regel zu
gebräuchlichen Vornamen («Georg» bzw. «Katharina») normalisiert;
Ausnahmen bilden Kürzel, deren Normalisierung sich nicht aus den
sprachwissenschaftlichen Hilfsmitteln erschliessen lässt.

Wenn bei einer Ehefrau der Ledigenname und der vom Ehemann übernommene
Familienname bekannt sind, wird sie unter beiden verzeichnet.

Angehörige geistlicher Institutionen wie Bischöfe, Äbte, Mönche etc.
werden, falls bekannt, nicht nur unter ihrem Familiennamen, sondern auch
unter der entsprechenden Institution aufgeführt.
Diese Institutionen erscheinen immer in normalisierter Form, ebenso
Familiennamen von Adligen, bei denen nur der Vorname erwähnt wird,
der Familienname allerdings bekannt ist. 

Heilige und biblische Gestalten, in der Regel nur mit den Vornamen
überliefert, werden unter diesem verzeichnet. 

Adlige Dynastien (Grafen, niedrige Adlige) werden gemäss bisherigen
Editionseinheiten oder zuverlässigen Genealogien nummeriert.
In Zweifelsfällen wird auf eine Nummerierung verzichtet. 

Die bei Personen und Familien angefügte Jahreszahl gibt die erste Erwähnung an;
teilweise folgt auch die Letzterwähnung.
Um die Identifikation zu erleichtern, werden v. a. bei bekannteren Personen
die Lebensdaten gemäss genealogischen Standardwerken und Lexika angegeben.
Falls möglich werden Personen mit Normdaten ([GND](https://lobid.org/gnd),
[HLS](https://hls-dhs-dss.ch/de/) etc.) versehen und mit
[metagrid.ch](https://metagrid.ch/) verlinkt.

Die Einträge zu Berufen, Ämtern und Funktionen sowie zu Wirkungsorten beziehen 
sich auf die Angaben in den edierten Quellen, ebenso die Zusatzinformationen
zu verwandtschaftlichen Beziehungen.
