## 11 Strukturierung der Texte

### 11.1 Abschnitte

Die Gliederung der Textvorlage wird übernommen. Originale Abschnitte werden nur mit [`<p/>`](../../elements/p.de.md) ausgezeichnet. Sofern ein Original stärker gegliedert oder strukturiert ist, kann man [`<p/>`](../../elements/p.de.md) innerhalb von [`<div/>`](../../elements/div.de.md)verwenden.
Die inhaltliche Strukturierung eines Textes durch den Bearbeitenden in Absätze erfolgt mit [`<seg/>`](../../elements/seg.de.md). Absätze können mit @n nummeriert werden.

[to do: Beispiele für p und div. Sinnvolles Beispiel für seg und p erfassen, dasjenige, das zur Zeit vorliegt, ist falsch, da p und seg verwendet, was ja keinen Sinn macht...]

Wo es zum besseren Verständnis notwendig erscheint, wird der Text mit Hilfe von Alineas und paragraphenweiser Nummerierung in eckigen Klammern, Mitten von Titeln etc. unterteilt.
Urkunden sollten gemäss ihrem formalen Aufbau strukturiert werden (vgl. z. B.  [Diplomatik](http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html)).

In der Regel sollten Absätze nach einem Punkt und nicht nach einem Komma erfolgen.

Bei längeren Paratexten (Einleitung, Kommentar) können Kapitel durch [`<div/>`](../../elements/div.de.md) mit @n nummeriert und gegebenenfalls mit @type näher bezeichnet werden. Der Text eines Kommentars kann innerhalb von [`<div/>`](../../elements/div.de.md) mit [`<p/>`](../../elements/p.de.md)  in Absätze strukturiert werden.

### 11.2 Zeilen- und Seitenangaben

Zeilenwechsel wurden in der analogen Edition mit / und Seitenwechsel mit // wiedergegeben. In der digitalen Edition werden Zeilen am Zeilenanfang ab der ersten Zeile mit [`<lb/>`](../../elements/lb.de.md) und die Seiten zu Beginn mit [`<pb/>`](../../elements/pb.de.md)
und @n ausgezeichnet.

### 11.3 Interpunktion

Die Interpunktion folgt, so weit möglich und sinnvoll, den heute im entsprechenden Sprachgebiet üblichen Regeln.
Gibt es in der Vorlage Textstellen, deren syntaktische Konstruktion nicht nach heutigen Satzbaumustern analysiert werden
kann oder deren Sinn schwer verständlich ist, wird besser auf Interpunktion verzichtet.

Für die Interpunktion von lateinischen Texten kann grundsätzlich die moderne deutsche Kommasetzung als Richtschnur gelten. Voraussetzung für eine korrekte Interpunktion ist das Verständnis des Quellentextes in seinem ganzen Aufbau (Urkundenformular) wie im einzelnen Wortlaut. Im Zweifelsfall ist ein Komma besser wegzulassen als zu setzen. Verschachtelungen sind durch die Kommasetzung korrekt wiederzugeben.

### 11.4 Originale Titel und Zwischentitel

Originale Titel und Zwischentitel werden mit [`<head/>`](../../elements/head.de.md) ausgezeichnet, optisch mit @type abgehoben und mit @n nummeriert. Titel, die der Bearbeitende einfügt, sind mit @resp versehen.

### 11.5 Direkte Rede

Direkte Rede,  die in der analogen Edition mit « » hervorgehoben wurde, wird  mit [`<q/>`](../../elements/q.de.md) ausgezeichnet.

### 11.6 Zitate

Zitate innerhalb eines Textes (z. B. inserierte Urkunden) werden mit [`<quote/>`](../../elements/quote.de.md) ausgezeichnet
und am Schluss des Zitats mit einer sachkritischen Anmerkung [`<note/>`](../../elements/note.de.md) versehen, in der auf den
zitierten Originaltext verwiesen wird. Ist der Originaltext ediert, kann anstelle von [`<note/>`](../../elements/note.de.md)
mit der @xml:id auf das Stück verwiesen werden.

Innerhalb der Paratexte (Anmerkungen, Kommentar, Einleitung) benutzen wir [`<quote/>`](../../elements/quote.de.md) für Zitate aus der Forschungsliteratur.

### 11.7 Tabellen

Einige Quellen, wie z. B. Rechnungen oder Zollordnungen, enthalten Tabellen, die auch als solche in der Edition
umgesetzt werden. Für die Darstellung von Tabellen verwenden wir [`<table/>`](../../elements/table.de.md) mit  [`<row/>`](../../elements/row.de.md) und [`<cell/>`](../../elements/cell.md).

### 11.8 Plica

Enthält ein Dokument eine Plica, dann gelten folgende Regelungen:

- Text unter der Plica wird als Bestandteil der recto-Seite transkribiert.

- Text auf der Plica wird ebenfalls als Bestandteil der recto-Seite transkribiert (obwohl er vom Material her gesehen 
  eigentlich zur verso-Seite gehören müsste).

- Die Reihenfolge von Text unter bzw. auf der Plica ist in der Transkription beliebig.