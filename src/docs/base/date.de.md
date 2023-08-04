---
title: Datierungsrichtlinien
---

# Datierungsrichtlinien der Sammlung Schweizerischer Rechtsquellen (SSRQ)

Die Datierungsrichtlinien ermöglichen eine einheitliche Erfassung und Abfrage von Datierungen und Zeiträumen, die sprachunabhängig ist.
## 1 Sortierlogik
Die Sortierlogik von Datierungen bzw. Zeiträumen ist die, dass alles, was vor einem Datum sein könnte, auch vor
  dem eingeordnet wird. So steht z. B. 18. Jh. (01.01.1701–31.12.1800) nach 1700. Wenn zwei Datierungen am selben Datum
  starten, aber unterschiedliche Zeiträume beinhalten, steht die genauere Datierung vor der ungenauen. So steht z. B.
  bei den beiden Zeiträumen 6.–7. Jh. und 6.–8. Jh.  der genauere Zeitraum 6.–7. Jh. vor 6.–8. Jh.

## 2 Eindeutige Datierungen

- Eindeutige Datierungen werden gemäss ISO 8601 innerhalb von [[date]](../elements/date.de.md) oder [[origDate]](../elements/origDate.de.md) mit @when-custom normalisiert (YYYY-MM-DD). Nach ISO 8601 und
  TEI ist bei der Verwendung des when-Attributs immer der Gregorianische Kalender gemeint, was bei der SSRQ nicht immer der Fall ist, weshalb wir zur
  Präzisierung von @when-custom immer auch @datingMethod verwenden.  Beispiel:  [to do Beispiel `<date when-custom="2001-09-11" datingMethod="gregorian">11 Sept 01</date>`]
- Hierarchisch übergeordnete Leerstellen (Jahr, Monat) werden in @when-custom mit einem Bindestrich ("-") angegeben. Beispiele: [to do  - `<date when-custom="--09-11">9/11</date>`, `<date when-custom="--09">September</date>`,  `<date when-custom="---11">Eleventh of the month</date>`]
- Hierarchisch untergeordnete Leerstellen (z. B. fehlender Tag) werden nicht mit @when-custom ausgezeichnet, sondern wie eine uneindeutige Datierung als Zeitraum mit @custom-from und @custom-to ausgzeichnet. Beispiel:  [to do]
- Datierungen nach Heiligen- oder Festtagen werden mithilfe des Grotefend aufgelöst. Auf der
   [Grotefend-Webseite](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm])
  gibt es verschiedene Hilfsmittel. Auch ein Rechner steht zur Verfügung.

## 3 Uneindeutige Datierung

### 3.1 Mehrere Datierungen innerhalb einer Quelle

Enthält eine Quelle mehrere Datum-Elemente, müssen alle Datierungen einzeln ausgezeichnet werden. Wenn die Datierung eines Stücks nicht sicher ist, muss die Datierung in Form eines Zeitraums angegeben werden. Beispiel: []to do]
- `<date when="1736-11-08">1736 November 8 / 22</date>`
- `<date when="1736-11-22"/>`

### 3.2 Zeiträume
#### 3.2.1 Durchgehende Zeiträume

Zeiträume werden mit den Attributen  @from-custom und @to-custom zusammen mit
@datingMethod innerhalb von [[date]](../elements/date.de.md) oder [[origDate]](../elements/origDate.de.md)  ausgezeichnet. Beispiele: [to do - 1521 Dezember 11 – 1544 April 16: `<date from-custom="1521-12-11" to-custom="1544-04-16" datingMethod="#julian">1521
  Dezember 11 - 1544 April 16</date>`
- 1717–1718: `<date from-custom="1717" to-custom="1718" datingMethod="#gregorian">1717-1718</date>`]

#### 3.2.2 Unterbrochene Zeiträume

Liegen Quellen mit unterbrochenen Zeiträumen vor, werden diese wie mehrere Zeiträume  behandelt. Beispiele: [to do- 1610, 1620–1635: Retrodigitalisierung: `<date when="1610">1610, 1620–1635</date><date from="1620" to="1635"/>`
- 1466, 25. Mai und 25. Heumonat: Retrodigitalisierung: `<date when="1466-05-25">1466, 25. Mai und 25.
  Heumonat</date><date when="1466-07-25"/>`]

####3.2.3 Uneindeutige Datierungen, die zugeordnet werden können

Unsichere Jahresangaben, zum Beispiel «wohl 1491», wird mit [[precision]](../elements/precision.de.md)
inkl. Attribute @match und @degree ausgezeichnet. Beispiel: [to do: `<date when="1491">wohl 1491<precision match="@when" degree="0.5"/></date>`]

Datierungen, die nicht eindeutig sind, jedoch zugeordnet werden können, werden als Zeiträume  mit @from-custom und @to-custom zusammen mit @datingMethod sowie [[precision]](../elements/precision.de.md) mit @match und @degree ausgezeichnet.

<table>
<thead>
    <tr>
        <th>Beispiel</th>
        <th>Werte @from-custom und @to-custom</th>
        <th>Zeitspanne: Schlüssel</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>17. Jh.</td>
        <td>1601-01-01/1700-12-31</td>
        <td>100 Jahre</td>
    </tr>
    <tr>
        <td>1. Hälfte 15. Jh.</td>
        <td>1401-01-01/1450-12-31</td>
        <td>50 Jahre</td>
    </tr>
</tbody>
    <tr>
        <td>Ende 15. Jh.</td>
        <td>1475-01-01/1500-12-31</td>
        <td>25 Jahre</td>
    </tr>
    <tr>
        <td>Ca. 1510</td>
        <td>1500-01-01/1520-12-31</td>
        <td>Ca.: +/-10 Jahre</td>
    </tr>
    <tr>
        <td>Mitte 15. Jh.</td>
        <td>1440-01-01/1460-12-31</td>
        <td>Ca.: +/-10 Jahre</td>
    </tr>
    <tr>
        <td>Mitte 1555</td>
        <td>1555-06-01/1555-07-31</td>
        <td>Ca.: +/-1 Monat</td>
    </tr>
    <tr>
        <td>Ende März</td>
        <td>03-21/03-31</td>
        <td>Ende: 10 Tage</td>
    </tr>
    <tr>
        <td>Anfang Juli</td>
        <td>07-01/07-10</td>
        <td>Anfang: 10 Tage</td>
    </tr>
</tbody>
</table>

#### 3.2.4 Uneindeutige Datierungen, die nicht zugeordnet werden können

Datierungen, die nicht eindeutig sind und nicht zugeordnet werden können, sollen, falls möglich, mit möglichst präziser Annäherung als Zeiträume
mit @notBefore-custom und @notAfter-custom sowie [[precision]](../elements/precision.de.md) mit @match und @degree ausgezeichnet werden.

<table>
<thead>
    <tr>
        <th>Beispiel</th>
        <th>Werte @notBefore-custom und @notAfter-custom</th>
        <th>Zeitspanne: Schlüssel</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Vor 1688</td>
        <td>1638-01-01/1688-12-31</td>
        <td>Vor: -25 Jahre</td>
    </tr>
    <tr>
        <td>Nach 1688</td>
        <td>1688-01-01/1738-12-31</td>
        <td>Nach: +25 Jahre</td>
    </tr>
    <tr>
        <td>Um 1500, ohne Datum</td>
        <td>1490-01-01/1510-12-31</td>
        <td>Um: +/-10 Jahre</td>
    </tr>
    <tr>
        <td>1730 [nach November 20]</td>
        <td>1730-11-21/1730-12-31</td>
        <td>Bis Jahresende</td>
    </tr>
    <tr>
        <td>vor 10.1738</td>
        <td>1738-08/1738-10 TO DO müsste wie folgt sein ??? 1738-07-01/1738-09-30</td>
        <td>3 Monate</td>
    </tr>
    <tr>
        <td>wohl 1738 oder ? 1738</td>
        <td>1738-01-01/1738-12-31</td>
        <td>1 Jahr</td>
    </tr>
    <tr>
        <td>nach 08.1738</td>
        <td>1738-08-01/1738-10-31 TO DO  müsste es nicht wie folgt sein??? 1738-09-01/1738-11-30</td>
        <td>3 Monate</td>
    </tr>
</tbody>
</table>

#### 3.2.5 Datierungen *post quem*  bzw. *ante quem*
*Post quem*-Datierungen erhalten kein [[precision]](../elements/precision.de.md),  jedoch das errechnete End- bzw.
Beginndatum erhält ein [[precision]](../elements/precision.de.md). Wenn bei einer Amtsbezeichnungen nur bekannt ist, bis wann jemand im Amt war, rechnen wir für den Amtsbeginn mit -10 Jahren. Der Inhalt von
@notAfter-custom ist sicher, nicht aber der Inhalt in @notBefore-custom, weshalb er ein [[precision]](../elements/precision.de.md) erhält.
Beispiel: Amtszeit  bis 1499 [to do
`<date notAfter-custom="1499" notBefore-custom="1489" datingMethod="#julian">bis
1499<precision match="@notBefore-custom" degree="0.5"/></date>`]

Dasselbe gilt  auch umgekehrt für Datierungen *ante quem*.

## 4 «Fälschungen» / Datierungsänderungen

Wenn ein Bearbeitender eine Fälschung ediert, ist das Datum der Fälschung relevant und nicht die Datierung im Quellentext. Ein erklärender Kommentar ist notwendig. Weicht eine Datierung im Regest von einer Datierung im Quellentext ab, ist zwingend ein Kommentar angebracht.

## 5 Neuer Stil  / Alter Stil

**Regeln**

1. Es wird grundsätzlich nach dem neuen Stil (Gregorianischer Kalender) datiert. Wenn ein Dokument nicht von einer Behörde stammt, die
   nachgewiesenermassen nach altem Stil (Julianischer Kalender) datiert (z. B. Kanzleien von Zürich und Bern), wird bei einem unkommentierten
   Datum von einer Datierung nach neuem Stil ausgegangen.
2. Bei Stücken, die doppelt, d. h. nach dem alten und neuen Stil, datiert sind, wird nach dem neuen Stil datiert.
3. Wo nicht sicher ist, nach welchem Stil datiert wurde und begründete Zweifel an einer Datierung nach neuem Stil
   vorliegen, wird dies in einer sachkritischen Anmerkung festgehalten.

Beispiele: [To do]

### 5.1 Kalenderwechsel

`<date from="1588-09-03" to="1588-09-20" calendar="Julian">Zwischen 3. und 20. September 1588</date>`<br/>
`<date when="1588-09-13" to="1588-10-30" calendar="Gregorian">Zwischen 13. und 30. September 1588</date>`

Automatische Umrechnung vom Alten in den Neuen Stil:
[[http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm]](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm])
(Rechner)

**Digitale Edition:**

Julianischer Kalender (alter Stil)

Das im edierten Stück angegebene Datum bzw. der Datierungstext wird belassen. Die Normalisierung und Kennzeichnung des
Datums oder der Zeitspanne erfolgt mit den entsprechenden Attributen im ISO-Stil, d. h. im Gregorianischen Kalender bzw.
im neuen Stil. Zusätzlich wird jedoch das Attribut `@datingMethod` mit dem Wert `julian` verwendet.

```xml
<date from-custom="1588-09-13" to-custom="1588-09-30" datingMethod="julian">Zwischen 3. und 20
September 1588</date>
```

Bei Stücken, die doppelt, d. h. nach dem alten und neuen Stil, datiert sind, wird nach dem neuen Stil bzw. dem
Gregorianischen Kalender datiert.


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
[HLS (Kalender)](http://www.hls-dhs-dss.ch/textes/d/D12812.php)

## 6 Jahresanfangsstile

Die unterschiedlichen
Jahresanfangsstile (*Circumcisionsstil* (Jahresanfang am 1. Januar), *Annuntiationsstil* (25. März) oder
*Natalstil* (25. Dezember)) müssen in [[date]](../elements/date.de.md) mit Hilfe von @calendar vermerkt werden.

Der Annuntiationsstil gilt in der Diözese Lausanne und in Freiburg von den Anfängen bis in die 2. Hälfte des 15.
Jahrhunderts, sonst in der Diözese Lausanne bis in die 1. Hälfte des 16. Jahrhunderts.

In SDS FR I/2/6 wird der Annuntiationsstil mit n. st. (= nouveau style) angezeigt, das Datum wird aber gemäss modernem
Kalender aufgelöst.
> Beispiel: 5. Ordonnance au sujet des voies de fait.
> [[http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5]](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5)
> 1364 (n. st.) février 4.
> In der Quelle steht folgende Datierung: ... le quatre jour
> du mois de février en l’ans Notre Seigneur courant 1363 ...

Weil nun der 4. Februar in der Zeit zwischen dem 1. Januar (oder allenfalls 25. Dezember) und dem 25. März
(= Annuntiation Mariä) liegt, verwandelt die Editorin zu Recht den 4. Februar 1363 in den 4. Februar 1364.

------------
FOLGENDER ABSCHNITT GEHÖRT ZU DATE
# Termine und Fristen

Termine (Weidetermine, Jagdzeitbeschränkungen etc.) werden auch als Datierungen mit [[date]](../elements/date.de.md)
und @when ausgezeichnet. Zur Kennzeichnung, dass es sich um einen Termin handelt, wird @type mit dem Inhalt "deadline"
eingefügt.

Zum Beispiel bei einem Termin:
> wellind und doch nit länger dann bis `<date type="deadline" when-custom="--04-16">zuͦ mittem aprellen</date>`

Schonfrist von Fischen vom 3. Januar bis 4. März

`<date from-custom="--01-03" to-custom="--03-04"/>`

Bewegliche Feiertage: z.B. Fastenzeit: von Aschermittwoch bis Karfreitag mit Taxonomie lösen
