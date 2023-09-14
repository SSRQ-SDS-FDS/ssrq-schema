# Textstruktur

## Abschnitte und Absätze

=== "Struktur des edierten Textes"

    Die Gliederung der Editionsvorlage wird übernommen.
    
    Originale Absätze werden mit [`<p>`](p.de.md) ausgezeichnet.
    In der Regel sollten diese Absätze nach einem Punkt und nicht
    nach einem Komma erfolgen.
    
    Sofern ein Original stärker gegliedert oder strukturiert ist, kann man
    [`<div>`](div.de.md) zur Auszeichnung größerer Abschnitte verwenden.
    
    Reicht die Gliederung des Textes mit [`<p>`](p.de.md) und 
    [`<div>`](div.de.md) nicht aus, kann der Bearbeitende die Abschnitte 
    oder Absätze mit [`<seg>`](seg.de.md) weiter nach inhaltlichen Kriterien 
    unterteilen.
    
    Wo es zum besseren Verständnis notwendig erscheint, wird der Text mithilfe
    von Alineas und absatzweiser Nummerierung in eckigen Klammern, 
    Mitten von Titeln etc. unterteilt.
    
    Urkunden sollten gemäss ihrem formalen Aufbau strukturiert werden (vgl.
    [Diplomatik
    (dt.)](http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html), 
    [Diplomatik (frz.)](http://theleme.enc.sorbonne.fr/cours/diplomatique).

    Mit «actum» eingeleitete Schlussformeln von Urkunden, werden wie Absätze
    behandelt. Nach «actum» folgt nach einem Komma «coram consilio», 
    «coram senatu», «presentibus» etc. Am Ende der Formeln wird ein Punkt
    eingesetzt (vgl. [Interpunktion](punctuation.de.md)).

=== "Struktur der editorischen Paratexte"

    Bei längeren Paratexten (Einleitung, Kommentar) können die Kapitel mit
    [`<div>`](div.de.md) nummeriert und ggf. näher bezeichnet werden. 
    
    Der Text eines Kommentars kann innerhalb von [`<div>`](div.de.md) mit 
    [`<p>`](p.de.md) in Absätze strukturiert werden.

## Seiten, Spalten und Zeilen

Zeilenwechsel wurden in der analogen Edition mit `/` und Seitenwechsel mit `//` 
wiedergegeben. 

In der digitalen Edition werden Zeilen am Zeilenanfang ab der ersten Zeile 
mit [`<lb/>`](lb.de.md) ausgezeichnet. Spaltenanfänge werden mit 
[`<cb/>`](cb.de.md) und Seitenanfänge mit [`<pb/>`](pb.de.md) ausgezeichnet.

## Titel und Zwischentitel

Originale Titel und Zwischentitel und solche, die der Bearbeitende einfügt, 
werden mit [`<head>`](head.de.md) ausgezeichnet.

## Direkte Rede und Zitate

=== "im edierten Text"

    Direkte Rede, die in der analogen Edition mit `«...»` hervorgehoben wurde,
    wird in der digitalen Edition mit [`<q>`](q.de.md) ausgezeichnet.
    
    Zitate innerhalb eines Textes (z. B. inserierte Urkunden) werden mit
    [`<quote>`](quote.de.md) ausgezeichnet und am Schluss des Zitats mit
    einer sachkritischen Anmerkung mit [`<note>`](note.de.md) versehen,
    in der auf den zitierten Originaltext verwiesen wird.
    Ist der Originaltext ediert, kann statt einer Anmerkung auf das Stück
    verwiesen werden.

=== "in den editorischen Paratexten"

    Innerhalb der editorischen Paratexte (Anmerkungen, Kommentar, Einleitung)
    benutzen wir [`<quote>`](quote.de.md) für Zitate aus der 
    Forschungsliteratur.

## Tabellen

Einige Quellen, wie z. B. Rechnungen oder Zollordnungen, enthalten Tabellen,
die auch als solche in der Edition umgesetzt werden. 

Für die Darstellung von Tabellen verwenden wir [`<table>`](table.de.md)
in Kombination mit [`<row>`](row.de.md) und [`<cell>`](cell.de.md).

## Plica

Enthält ein Dokument eine Plica (getaggt mit [`<ab>`](ab.de.md)),
dann gelten folgende Regelungen:

- Text unter der Plica wird als Bestandteil der recto-Seite transkribiert.
- Text auf der Plica wird ebenfalls als Bestandteil der recto-Seite
  transkribiert (obwohl er vom Material her gesehen eigentlich zur verso-Seite
  gehören müsste).
- Die Reihenfolge von Text unter bzw. auf der Plica ist in der Transkription
  beliebig.