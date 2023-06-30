---
title: Datierungsrichtlinien
---

# Grundsätze der Datierung

- Möglichst grosse Vereinheitlichung
- Nach Sprachen getrennter Abruf möglich (sprachliche Gepflogenheiten): DE, FR, IT
- Circumcisionsstil (Jahresanfang am 1. Januar), Annutiationsstil (25. März) oder Natalstil (25. Dezember) muss
  vermerkt werden.
- Die **Sortierlogik** von Datierungen bzw. Zeiträumen ist die, dass alles, was vor einem Datum sein könnte, auch vor
  dem eingeordnet wird. So steht z. B. 18. Jh. (01.01.1701–31.12.1800) nach 1700. Wenn zwei Datierungen am selben Datum
  starten, aber unterschiedliche Zeiträume beinhalten, steht die genauere Datierung vor der ungenauen. So steht z. B.
  bei den beiden Zeiträumen 6.-7. Jh. und 6.-8. Jh. 6.-7. Jh. vor 6.-8. Jh.

# Eindeutige Datierung

- Daten werden gemäss ISO 8601 im @when (– erwünscht mit @when-custom –) normalisiert (YYYY-MM-DD). Nach ISO 8601 und
  TEI ist bei der Verwendung des @when Attributs immer der Gregorianische Kalender gemeint, weshalb wir seit 2019 zur
  Präzisierung @when-custom mit @datingMethod verwenden.
- Hierarchisch übergeordnete Leerstellen (Jahr, Monat) werden in @when bzw. @when-custom mit einem Bindestrich ("-")
  angegeben. Hierarchisch untergeordnete Leerstellen (z. B. fehlender Tag) werden jedoch nicht speziell gekennzeichnet.
- Datierungen nach Heiligen- oder Festtagen werden mit Hilfe des Grotefend aufgelöst. Auf der
  Website: http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm gibt es verschiedene Hilfsmittel. Auch
  ein Rechner steht zur Verfügung.

## Beispiele

- <date when="2001">The year 2001</date>
- <date when="2001-09">September 2001</date>
- <date when="2001-09-11">11 Sept 01</date>
- <date when="--09-11">9/11</date>
- <date when="--09">September</date>
- <date when="---11">Eleventh of the month</date>

# Uneindeutige Datierung

## Mehrere Datierungen innerhalb eines Stücks (Retrodigitalisierung)

Verwendung mehrerer Datums-Elemente. (Die Verwendung mehrerer Datums-Elemente muss begründet sein und sich auf das Stück
beziehen. Datierungen von Bemerkungen, ähnlichen Stücken oder Abschriften gehören nicht in diese
Datierung [evtl. <note> verwenden]. Grundsätzlich sind jedoch diese Datierungen gleich zu behandeln.)

### Beispiele

- <date when="1736-11-08">1736 November 8 / 22</date>
- <date when="1736-11-22"/>

## Zeiträume

Zeiträume werden mit den Attributen @from und @to bzw. seit 2019 mit @from-custom und @to-custom zusammen mit
@datingMethod innerhalb von <date> ausgezeichnet.

### Beispiele

- 1521 Dezember 11 – 1544 April 16: <date from-custom="1521-12-11" to-custom="1544-04-16" datingMethod="#julian">1521
  Dezember 11 - 1544 April 16</date>
- 1717–1718: <date from-custom="1717" to-custom="1718" datingMethod="#gregorian">1717-1718</date>

## Unterbrochene Zeiträume

- (Begründung muss wie in 1. vorliegen.)
- Retrodigitalisierung: Die Zeiträume werden in mehreren Tags kodiert.

### Beispiele

- 1610, 1620–1635: Retrodigitalisierung: <date when="1610">1610, 1620–1635</date><date from="1620" to="1635"/>
- 1466, 25. Mai und 25. Heumonat: Retrodigitalisierung: <date when="1466-05-25">1466, 25. Mai und 25.
  Heumonat</date><date when="1466-07-25"/>

## Nicht eindeutige Datierungen, die jedoch zugeordnet werden können

Retrodigitalisierung: Unsichere Jahresangaben, zum Beispiel wohl 1491, wird mit [precision](../elements/precision.md)
inkl.
Attribute [[@match]] und [[@degree]] ausgezeichnet.

<date when="1491">wohl 1491<precision match="@when" degree="0.5"/></date>

Datierungen, die nicht eindeutig sind, jedoch zugeordnet werden können, werden als Intervalle kodiert: <br />

''Jeweils mit [[@from]], [[@to]] bzw. seit 2019 mit [[@from-custom]], [[@to-custom]] zusammen
mit [[@datingMethod]]'' <br />

{| border="1" cellpadding="5" cellspacing="0"
|-
|Beispiel
|Werte<br/>@from-custom & @to-custom
|Zeitspanne:<br/> Schlüssel
|-
|17. Jh.
|1601/1700
|Jh.: 100
|-
|1. Hälfte 15. Jh.
|1401/1450
|Hälfte: 50
|-
|}

<date from-custom="1401" to-custom="1450" datingMethod="#julian">1. Hälfte 15.
Jh.</date>

''Jeweils mit [[@notBefore]], [[@notAfter]] bzw. seit 2019 mit [[@notBefore-custom]], [[@notAfter-custom]]
und <[[precision]] [[@match]] [[@degree]]/>'' <br />

{| border="1" cellpadding="5" cellspacing="0"
|-
|Beispiel
|Werte<br/>@notBefore-custom & @notAfter-custom
|Zeitspanne:<br/> Schlüssel
|-
|Ende 15. Jh.
|1475/1500
|Ende: 25 Jahre
|-
|Ca. 1510
|1500/1520
|Ca.: +/-10 Jahre
|-

|Mitte 15. Jh.
|1440/1460
|Ca.: +/-10 Jahre
|-
|Mitte 1555
|1555-06/1555-07
|Ca.: +/-1 Monat
|-

|Ende März
|03-21/03-31
|Ende: 10 Tage
|-
|Anfangs Juli
|07-01/07-10
|Anfangs: 10 Tage
|-
|}

Retrodigitalisierung: <date notBefore="1500" notAfter="1520">Ca.
1510<precision match="@notBefore, @notAfter" degree="0.5"/></date>
<date notBefore="1386-07-01" notAfter="1386-07-10">1386 anfangs Juli<precision match="@notBefore, @notAfter"
degree="0.5"/></date>

Portal: <date notBefore-custom="1500" notAfter-custom="1520" datingMethod="#julian">Ca.
1510<precision match="@notBefore-custom, @notAfter-custom" degree="0.5"/></date>
<date notBefore-custom="1386-07-01" notAfter-custom="1386-07-10" datingMethod="#julian">1386 anfangs Juli<precision
match="@notBefore-custom, @notAfter-custom"
degree="0.5"/></date>

## Nicht eindeutige Datierungen, die aber nicht zugeordnet werden können

Datierungen, die nicht eindeutig sind und nicht zugeordnet werden können, sollen, falls möglich, auch als Intervalle
kodiert werden (analog 4., mit möglichst präziser Annäherung):

''Jeweils mit [[@notBefore]], [[@notAfter]] bzw. seit 2019 mit [[@notBefore-custom]], [[@notAfter-custom]]
und <[[precision]] [[@match]] [[@degree]]/>'' <br />

{| border="1" cellpadding="5" cellspacing="0"
|-
|Beispiel
|Werte<br/>@notBefore-custom & @notAfter-custom
|Zeitspanne:<br/> Schlüssel
|-
|Vor 1688
|1638/1688
|Vor: -25 Jahre (ssrq-online); -50 Jahre (hhb)
|-
|Nach 1688
|1688/1738
|Nach: +25 Jahre (ssrq-online); +50 Jahre (hhb)
|-
|Um 1500, ohne Datum
|1490/1510
|Um: +/-10 Jahre
|-
|1730 [nach November 20]
|1730-11-21/1730-12-31
|Bis Jahresende
|-
|vor 10.1738
|1738-08/1738-10
|3 Monate
|-
|wohl oder ? 1738
|1738-01-01/1738-12-31
|1 Jahr
|-
|nach 08.1738
|1738-08/1738-10
|3 Monate
|-
|}

''post quem'' Datierungen müssen in ihrer „certainty“ nicht hinterfragt werden, jedoch das angegebene „End-“ bzw.
„Beginndatum“:<br/>

<date notBefore-custom="1730-11-21" notAfter-custom="1730-12-31" datingMethod="#gregorian">1730
[nach November 20]<precision match="@notAfter-custom" degree="0.5"/></date>

Bei Berufs- oder Amtsbezeichnungen, bei denen man weiss, bis wann jemand im Amt war, handhaben wir wie folgt:
@notAfter-custom und bekannte Jahreszahl; @notBefore-custom mit -10 Jahre

z. B. bis 1499
<date notAfter-custom="1499" notBefore-custom="1489" datingMethod="#julian">bis
1499<precision match="@notBefore-custom" degree="0.5"/></date>

## «Fälschungen» / Datierungsänderungen

Grundsätzlich wird von der Erkenntnis des Editierenden ausgegangen (v. a. im Regest – eine entsprechende andere
Datierung wird sowieso im Fliesstext vorkommen und muss entsprechend ausgezeichnet werden).

## Neuer Stil / Alter Stil

''Herkömmliche Regeln:''

1. Es wird grundsätzlich nach dem neuen Stil datiert. Wenn ein Dokument nicht von einer Behörde stammt, die
   nachgewiesenermassen nach altem Stil datiert (z. B. Kanzleien von Zürich und Bern), wird bei einem unkommentierten
   Datum von einer Datierung nach neuem Stil ausgegangen.


2. Datierung nach dem alten Stil oder nach beiden Stilen werden in sachkritischen Anmerkungen, aber nicht im Regest
   festgehalten.


3. Wo nicht sicher ist, nach welchem Stil datiert wurde und begründete Zweifel an einer Datierung nach neuem Stil
   vorliegen, wird dies ebenfalls in einer sachkritischen Anmerkung festgehalten.

''Speziell für die Retrodigitalisierung'':

Sowohl das Gregorianische als auch das Julianische Datum werden in den Inhaltsverzeichnissen im ISO-Stil wiedergegeben.
Werden beide Daten aufgeführt, werden beide mit dem Attribut [[@calendar]] und dem Wert "Julian" oder "Gregorian"
versehen. Kommt in dem jeweiligen Inhaltsverzeichnis nur ein Datum vor, wird dieses nicht speziell gekennzeichnet,
sondern als gregorianisch angenommen.

<date from="1588-09-03" to="1588-09-20" calendar="Julian">Zwischen 3. und 20. September 1588</date>
<date when="1588-09-13" to="1588-10-30" calendar="Gregorian">Zwischen 13. und 30. September 1588</date>

Automatische Umrechnung vom Alten in den Neuen
Stil: http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm (Rechner)

''Digitale Edition:''

Julianischer Kalender (alter Stil)

Das im edierten Stück angegebene Datum bzw. der Datierungstext wird belassen. Die Normalisierung und Kennzeichnung des
Datums oder der Zeitspanne erfolgt mit den entsprechenden Attributen im ISO-Stil, d. h. im Gregorianischen Kalender bzw.
im neuen Stil. Zusätzlich wird jedoch das Attribut [[@datingMethod]] mit dem Wert "#julian" verwendet.

<date from-custom="1588-09-13" to-custom="1588-09-30" datingMethod="#julian">Zwischen 3. und 20
September 1588</date>

Bei Stücken, die doppelt, d. h. nach dem alten und neuen Stil, datiert sind, wird nach dem neuen Stil bzw. dem
Gregorianischen Kalender datiert.

Beispiel einer Doppeldatierung mit Bruchstrich: 25/15. octobris anno 90

<date when-custom="1590-10-25" datingMethod="#Gregorian">25/15. octobris anno 90</date>

### Kalenderwechsel

Die sieben katholischen Orte gingen - mit Ausnahme von Ob- und Nidwalden - am 12./22. Januar 1584 zum neuen Stil über.
Obwalden und Nidwalden nahmen den neuen Kalender einen Monat später an.

In der gemeineidgenössischen Vogtei Thurgau führte die Anwendung des neuen Stils 1584 zu Spannungen zwischen Zürich und
den fünf inneren Orten. Am 6.3.1585 verfügte die Badener Tagsatzung die Feier der kirchlichen Feste nach dem neuen
Kalender; die Evangelischen durften jedoch Weihnachten, Stephanstag, Neujahr, Ostern, Christi Himmelfahrt und Pfingsten
nach dem alten Stil begehen.

Im Appenzellerland führte die Einführung des Gregorianischen Kalenders zum Widerstand der Äusseren Rhoden. Innerrhoden
nahm den neuen Stil 1584 an, Ausserrhoden erst während der Helvetik, an Weihnachten 1798.

Im Wallis erfolgte der Übergang am 1./11. März 1656. Im Untertanengebiet des Unterwallis hatte der neue Stil schon 1622
Einzug gehalten.

Die evangelischen Stände Zürich, Bern, Basel und Schaffhausen, zudem Katholisch-Glarus, Neuenburg und Genf gingen am
1./12. Januar 1701 zum neuen Kalender über. Die Stadt St. Gallen folgte 1724. Evangelisch-Glarus nahm den neuen Stil in
der Helvetik am 4.7.1798 an.

In Graubünden wurde der Gregorianische Stil in katholischen Gemeinden 1623/1624 eingeführt. In den paritätischen
Gemeinden folgten die Katholiken ab der Mitte des 17. Jahrhunderts dem neuen Kalender, die Reformierten erst ab der
zweiten Hälfte des 18. Jahrhunderts. In den evangelischen Gemeinden erfolgte der Übergang zwischen 1783 (Oberengadin und
Bergell) und 1812 (Schiers und Grüsch).

Literatur:
HLS (Kalender), URL: http://www.hls-dhs-dss.ch/textes/d/D12812.php

Luzern: Tag der Umstellung: 12. Januar 1584 alten Stils = 22. Januar 1584 neuen Stils<ref>StALU RP 39, fol. 7r.</ref>

'''Verweise'''
<references />

##8. Jahresanfangsstile

Die unterschiedlichen
Jahresanfangsstile [Circumcisionsstil (Jahresanfang am 1. Januar), Annutiationsstil (25. März) oder
Natalstil (25. Dezember)] müssen in <date> mit Hilfe von [[@calendar]] vermerkt werden.

'''Annuntiationsstil'''

Der Annuntiationsstil gilt in der
Diözese Lausanne und in Freiburg von den Anfängen bis in die

2. Hälfte des 15. Jahrhunderts, sonst in der Diözese
   Lausanne bis in die 1. Hälfte 16. Jahrhundert.

In SDS FR I/2/6 wird der Annuntiationsstil mit n. st. (= nouveau style) angezeigt, das Datum wird aber gemäss modernem
Kalender aufgelöst.

Beispiel:

5. Ordonnance au sujet des voies de fait. http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5
   1364 (n. st.) février 4.
   In der Quelle steht folgende Datierung: ... le quatre jour
   du mois de février en l’ans Notre Seigneur courant 1363 ...

Weil nun der 4. Februar in der Zeit zwischen dem 1. Januar (oder allenfalls

25. Dezember) und dem 25. März (= Annuntiation Mariä) liegt,
    verwandelt die Editorin zu Recht den 4. Februar 1363 in den
4. Februar 1364.

# Termine und Fristen

Termine (Weidetermine, Jagdzeitbeschränkungen etc.) werden auch als Datierungen mit <[[date]]> und [[@when]]
ausgezeichnet. Zur Kennzeichnung, dass es sich um einen Termin handelt, wird [[@type]] mit dem Inhalt "deadline"
eingefügt.

Zum Beispiel bei einem Termin:
wellind und doch nit
länger dann bis <date type="deadline" when="--04-16">zuͦ mittem aprellen</date>

Schonfrist von Fischen vom 3. Januar bis 4. März

<date from="--01-03" to="--03-04"></date>

Bewegliche Feiertage: z.B. Fastenzeit: von Aschermittwoch bis Karfreitag mit Taxonomie lösen