---
title: Datierungsrichtlinien
---

# Datierungsrichtlinien der Sammlung Schweizerischer Rechtsquellen (SSRQ)

Die Datierungsrichtlinien ermöglichen eine einheitliche und sprachunabhängige
Erfassung und Abfrage von Datierungen und Zeiträumen.

## 1 Sortierlogik

Die Sortierlogik von Datierungen bzw. Zeiträumen ist die folgende:

- Ältere Datierungen stehen vor neueren Datierungen, z. B. steht bei den beiden
  folgenden Zeiträumen «7.–10. Jh.» vor «8.–9. Jh.».
- Alles, was vor einem Datum sein könnte, wird auch vor diesem eingeordnet,
  so steht z. B. «18. Jh.» (01.01.1701–31.12.1800) vor «1800».
- Wenn zwei Datierungen mit unterschiedlichen Zeiträumen am selben Datum
  starten, dann steht die genauere Datierung vor der ungenaueren, z. B.
  «6.–7. Jh.» vor «6.–8. Jh.» und «1300–1350» vor «1300–1375».

## 2 Eindeutige Datierungen

- Eindeutige Datierungen werden gemäss
  [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601) innerhalb von
  [`<date>`](date.de.md) oder [`<origDate>`](origDate.de.md) mit
  dem Attribut `@when-custom` normalisiert.
- Das Datumsformat lautet grundsätzlich: `YYYY-MM-DD`, d. h. vierstellige
  Jahresangabe, zweistellige Monatsangabe, zweistellige Tagesangabe, die ggf.
  mit führenden Nullen aufgefüllt werden.
- Nach ISO 8601 und TEI ist bei der Verwendung des `@when`-Attributs immer der
  gregorianische [Kalender](https://hls-dhs-dss.ch/de/articles/012812/2018-01-15/)
  gemeint, was bei der SSRQ allerdings nicht immer der Fall ist.
  Deshalb verwenden wir statt `@when` das allgemeinere Attribut
  `@when-custom` in Kombination mit `@datingMethod`, um den Kalender
  zu spezifizieren.
  Beispiele:

    ```xml
    <date when-custom="2001-09-11" datingMethod="gregorian">11 Sept 2001</date>
    ```

    ```xml
    <date when-custom="1001-09-11" datingMethod="julian">11 Sept 1001</date>
    ```

- Hierarchisch übergeordnete Leerstellen (z. B. fehlendes Jahr, fehlender
  Monat) werden in `@when-custom` mit einem Bindestrich ("-") angegeben.
  Beispiele:

    ```xml
    <date when-custom="--09-11">11.09.</date>
    ```

    ```xml
    <date when-custom="--09">September</date>
    ```

    ```xml
    <date when-custom="---11">Elfter Tag eines Monats</date>
    ```

- Hierarchisch untergeordnete Leerstellen (z. B. fehlender Tag) werden hingegen
  nicht mit `@when-custom` ausgezeichnet, sondern wie eine uneindeutige
  Datierung als Zeitraum mit `@from-custom` und `@to-custom` ausgezeichnet.
  Beispiel:
  `<date from-custom="1001-09-01" to-custom="1001-09-30" datingMethod="julian">September 1001</date>`
- Datierungen nach Heiligen- oder Festtagen werden mithilfe der HTML-Version des
  [Grotefend](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm)
  aufgelöst. Dort gibt auch es verschiedene Hilfsmittel, wie z. B. einen
  Kalenderrechner.

## 3 Uneindeutige Datierung

### 3.1 Mehrere Datierungen innerhalb einer Quelle

Enthält eine Quelle mehrere Daten, müssen alle einzeln ausgezeichnet werden.
Wenn die Datierung eines Stücks nicht sicher ist, muss die Datierung in Form
eines Zeitraums angegeben werden.
Beispiel:

```xml
<date when-custom="1736-11-08" datingMethod="gregorian">8./22. November 1736</date>
 <date when-custom="1736-11-22" datingMethod="gregorian"/>
```

### 3.2 Zeiträume

#### 3.2.1 Durchgehende Zeiträume

Zeiträume werden mit den Attributen `@from-custom` und `@to-custom` zusammen mit
`@datingMethod` innerhalb von [`<date>`](date.de.md) oder
[`<origDate>`](origDate.de.md) ausgezeichnet.
Beispiele:
```xml
    <date from-custom="1521-12-11" to-custom="1544-04-16"
    datingMethod="julian">11. Dezember 1521 - 16. April 1544</date>
```

```xml
<date from-custom="1717-01-01" to-custom="1718-12-31"
  datingMethod="gregorian">1717-1718</date>
```

#### 3.2.2 Unterbrochene Zeiträume

Liegen unterbrochene Zeiträumen vor, werden diese wie mehrere Zeiträume
behandelt.
Beispiele:

```xml
<date from-custom="1610-01-01" to-custom="1610-12-31"
  datingMethod="gregorian">1610, 1620–1635</date>
```

```xml
<date from-custom="1620-01-01" to-custom="1635-12-31
  datingMethod="gregorian"/>
```

```xml
<date when-custom="1466-05-25" datingMethod="julian">25. Mai und 25.
  Heumonat 1466</date><date when="1466-07-25"/>
```

#### 3.2.3 Uneindeutige Datierungen, die zugeordnet werden können

Unsichere Jahresangaben, zum Beispiel «wohl 1491», werden mit
[`<precision>`](precision.de.md) ausgezeichnet.
Beispiel:

```xml
<date from-custom="1491-01-01" to-custom="1491-12-31">wohl 1491
    <precision match="@from-custom @to-custom" precision="medium"/>
</date>
```

Datierungen, die nicht eindeutig sind, jedoch zugeordnet werden können,
werden als Zeiträume mit `@from-custom` und `@to-custom` zusammen mit
`@datingMethod` sowie [`<precision>`](precision.de.md) ausgezeichnet.

| Beispiel          | Werte `@from-custom` und `@to-custom` | Zeitspanne: Schlüssel |
| ----------------- | ------------------------------------- | --------------------- |
| 15. Jh.           | 1401-01-01/1500-12-31                 | 100 Jahre             |
| 1. Hälfte 15. Jh. | 1401-01-01/1450-12-31                 | 50 Jahre              |
| Anfang 15. Jh.    | 1401-01-01/1425-12-31                 | 25 Jahre              |
| Ende 15. Jh.      | 1475-01-01/1500-12-31                 | 25 Jahre              |
| Ca. 1510          | 1500-01-01/1520-12-31                 | +/-10 Jahre           |
| Mitte 15. Jh.     | 1440-01-01/1460-12-31                 | +/-10 Jahre           |
| Mitte 1555        | 1555-06-01/1555-07-31                 | +/-1 Monat            |
| Ende März         | --03-22/--03-31                       | 10 Tage               |
| Anfang Juli       | --07-01/--07-10                       | 10 Tage               |

#### 3.2.4 Uneindeutige Datierungen, die nicht zugeordnet werden können

Datierungen, die nicht eindeutig sind und nicht zugeordnet werden können,
sollen mit möglichst präziser Annäherung als Zeiträume mit `@notBefore-custom`
und `@notAfter-custom` sowie [`<precision>`](precision.de.md) ausgezeichnet
werden.

| Beispiel               | Werte `@notBefore-custom` und `@notAfter-custom` | Zeitspanne: Schlüssel |
| ---------------------- | ------------------------------------------------ | --------------------- |
| vor 1700               | 1675-01-01/1699-12-31                            | -25 Jahre             |
| nach 1700              | 1701-01-01/1725-12-31                            | +25 Jahre             |
| um 1700                | 1690-01-01/1710-12-31                            | +/-10 Jahre           |
| wohl 1700 oder 1700?   | 1700-01-01/1700-12-31                            | 1 Jahr                |
| vor 20. November 1700  | 1700-01-01/1700-11-19                            | von Jahresanfang      |
| nach 20. November 1700 | 1700-11-21/1700-12-31                            | bis Jahresende        |
| vor Oktober 1700       | 1700-07-01/1700-09-30                            | -3 Monate             |
| nach Oktober 1700      | 1700-11-01/1701-01-31                            | +3 Monate             |

#### 3.2.5 Datierungen _post quem_ bzw. _ante quem_

_Post quem_-Datierungen erhalten kein [`<precision>`](precision.de.md),
jedoch das errechnete End- bzw. Beginndatum.

Wenn bei Amtsbezeichnungen nur bekannt ist, bis wann jemand im Amt war,
rechnen wir für den Amtsbeginn mit -10 Jahren.
Der Inhalt von `@notAfter-custom` ist sicher, nicht aber der Inhalt in
`@notBefore-custom`, weshalb er ein [`<precision>`](precision.de.md) erhält.
Beispiel:

```xml
<date notBefore-custom="1489-01-01" notAfter-custom="1499-12-31
datingMethod="julian">[Amtszeit] bis 1499<precision match="@notBefore-custom"
precision="medium/></date>
```

Dasselbe gilt auch umgekehrt für Datierungen _ante quem_.

## 4 «Fälschungen» / Datierungsänderungen

Wenn eine Fälschung ediert wird, ist das Datum der Fälschung relevant
und nicht die Datierung im Quellentext.
Ein erklärender Kommentar ist notwendig.

Weicht eine Datierung im Regest von einer Datierung im Quellentext ab,
ist ein Kommentar obligatorisch.

## 5 Neuer Stil / Alter Stil

1. Es wird grundsätzlich nach dem neuen Stil, d. h. dem gregorianischer
   Kalender, datiert.
   Wenn ein Dokument nicht von einer Behörde stammt, die nachgewiesenermassen
   nach altem Stil, d. h. dem julianischer Kalender, datiert (z. B. die
   Kanzleien von Zürich und Bern), wird bei einem unkommentierten Datum von
   einer Datierung nach neuem Stil ausgegangen.
2. Bei Stücken, die doppelt, d. h. nach dem alten und neuen Stil, datiert sind,
   wird nach dem neuen Stil datiert.
3. Wo nicht sicher ist, nach welchem Stil datiert wurde und begründete Zweifel
   an einer Datierung nach neuem Stil vorliegen, wird dies innerhalb von`@datingMethod` mit dem Wert `unkown`  festgehalten.  Eine
   Anmerkung mit [`<note>`](note.de.md) ist in der Regel sinnvoll.


Datiert eine Quelle nach dem julianischen [Kalender](http://www.hls-dhs-dss.ch/textes/d/D12812.php), also dem alten Stil, wird
das im edierten Stück angegebene Datum belassen. Die Normalisierung und Kennzeichnung des Datums oder der Zeitspanne erfolgt mit
den entsprechenden Attributen, d. h. im gregorianischen Kalender bzw. im neuen
Stil. Zusätzlich wird jedoch das Attribut `@datingMethod` mit dem Wert
`gregorian` verwendet (vgl. Beispiel 2 unten).

Die Umrechnung vom alten in den neuen Stil kann mit dem Rechner des
[Grotefend](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm)
vorgenommen werden.

Beispiele:  
```xml
<date from-custom="1588-09-03" to-custom="1588-09-20"
  datingMethod="julian">Zwischen 3. und 20. September 1588</date
```
```xml
<date from-custom="1588-09-13" to-custom="1588-09-30
  datingMethod="gregorian">Zwischen 3. und 20. September 1588</date>
```

```xml
<date from-custom="1588-09-03" to-custom="1588-09-20"
  datingMethod="unknown">Zwischen 3. und 20. September 1588</date>
  <note>Es finden sich keine Informationen zum Kalenderwechsel.</note>
```

## 6 Kalenderwechsel

Die sieben katholischen Orte gingen – mit Ausnahme von Ob- und Nidwalden –
am 12./22. Januar 1584 zum neuen Stil über. Obwalden und Nidwalden nahmen den
neuen Kalender einen Monat später an. 
In Luzern  war der Tag der Umstellung am 12. Januar 1584 alten Stils = 22. Januar 1584 neuen Stils (StALU RP 39, fol. 7r).

In der gemeineidgenössischen Vogtei Thurgau führte die Anwendung des neuen
Stils 1584 zu Spannungen zwischen Zürich und den fünf inneren Orten.
Am 6.3.1585 verfügte die Badener Tagsatzung die Feier der kirchlichen Feste
nach dem neuen Kalender; die Evangelischen durften jedoch Weihnachten,
Stephanstag, Neujahr, Ostern, Christi Himmelfahrt und Pfingsten nach dem
alten Stil begehen.

Im Appenzellerland führte die Einführung des gregorianischen Kalenders zum
Widerstand der Äusseren Rhoden. Innerrhoden nahm den neuen Stil 1584 an,
Ausserrhoden erst während der Helvetik, an Weihnachten 1798.

Im Wallis erfolgte der Übergang am 1./11. März 1656. Im Untertanengebiet
des Unterwallis hatte der neue Stil schon 1622 Einzug gehalten.

Die evangelischen Stände Zürich, Bern, Basel und Schaffhausen, zudem
Katholisch-Glarus, Neuenburg und Genf gingen am 1./12. Januar 1701
zum neuen Kalender über. Die Stadt St. Gallen folgte 1724. Evangelisch-Glarus
nahm den neuen Stil in der Helvetik am 4.7.1798 an.

In Graubünden wurde der gregorianische Stil in katholischen Gemeinden
1623/1624 eingeführt. In den paritätischen Gemeinden folgten die Katholiken
ab der Mitte des 17. Jahrhunderts dem neuen Kalender, die Reformierten erst
ab der zweiten Hälfte des 18. Jahrhunderts. In den evangelischen Gemeinden
erfolgte der Übergang zwischen 1783 (Oberengadin und Bergell) und 1812
(Schiers und Grüsch).


## 7 Jahresanfangsstile

Die unterschiedlichen Jahresanfangsstile:
_Circumcisionsstil_ (Jahresanfang am 1. Januar),
_Annuntiationsstil_ (Jahresanfang am 25. März) und
_Natalstil_ (Jahresanfang am 25. Dezember)
müssen in [`<date>`](date.de.md) mithilfe von `@datingMethod` vermerkt werden.

Der Annuntiationsstil gilt in der Diözese Lausanne und in Freiburg vom
Anfang bis in die 2. Hälfte des 15. Jahrhunderts, sonst in der Diözese
Lausanne bis in die 1. Hälfte des 16. Jahrhunderts.

In [SDS FR I/2/6](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5)  wird der Annuntiationsstil mit «n. st.» (= «nouveau style»)
angezeigt, das Datum wird aber gemäss modernem Kalender aufgelöst. Beispiel:
` Ordonnance au sujet des voies de fait.
  1364 (n. st.) février 4. –
 In der Quelle steht folgende Datierung:
 «... lo quar jor dou moys de febrier, in l’ant de Nostre Segnour corant per
 mil CCC et sexante et troys (1363) ...» ` Weil nun der 4. Februar in der Zeit zwischen dem 1. Januar (oder allenfalls 25.
Dezember) und dem 25. März (= Annuntiation Mariä) liegt, ediert die
Bearbeitende zu Recht den «4. Februar 1363» als den «4. Februar 1364».
