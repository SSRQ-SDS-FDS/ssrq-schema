---
title: Datierungsrichtlinien
---

# Datierungsrichtlinien der Sammlung Schweizerischer Rechtsquellen (SSRQ)

Die Datierungsrichtlinien ermöglichen eine einheitliche und sprachunabhängige
Erfassung und Abfrage von Datierungen und Zeiträumen.

## 1 Sortierlogik und Ausgabe

Die Sortierlogik von Datierungen bzw. Zeiträumen ist die folgende:

- Ältere Datierungen stehen vor neueren Datierungen, z. B. steht bei den beiden
  folgenden Zeiträumen «7.–10. Jh.» vor «8.–9. Jh.».
- Alles, was vor einem Datum sein könnte, wird auch vor diesem eingeordnet,
  so steht z. B. «18. Jh.» (1.1.1701–31.12.1800) vor «1800».
- Wenn zwei Datierungen mit unterschiedlichen Zeiträumen am selben Datum
  starten, dann steht die genauere Datierung vor der ungenaueren, z. B.
  «6.–7. Jh.» vor «6.–8. Jh.» und «1300–1350» vor «1300–1375».
- Wenn zwei Datierungen mit dem gleichen Zeitraum vorliegen, bei einer der
  Datierungen jedoch der zugrunde liegende Kalender unbekannt ist
  (d. h. `@calendar="unknown"`), dann steht die Datierung mit bekanntem
  Kalender zuerst, also `<date calendar="julian" when="1590-01-01/>` vor
  `<date calendar="unknown" when="1590-01-01/>`.

Die Ausgabe aller Datumsangaben erfolgt ohne führende Nullen, z. B. 1.1.1810 statt 01.01.1810

## 2 Eindeutige Datierungen

- Eindeutige Datierungen werden gemäss
  [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601) innerhalb von
  [`<date>`](date.de.md) oder [`<origDate>`](origDate.de.md) mit
  dem Attribut `@when-custom` auf folgendes Datumsformat hin normalisiert:
  `YYYY-MM-DD`, d. h. vierstellige
  Jahresangabe, zweistellige Monatsangabe, zweistellige Tagesangabe, die ggf.
  mit führenden Nullen aufgefüllt werden.
- Nach ISO 8601 und TEI ist bei der Verwendung des `@when`-Attributs immer der
  gregorianische
  [Kalender](https://hls-dhs-dss.ch/de/articles/012812/2018-01-15/)
  gemeint, was bei der SSRQ allerdings nicht immer der Fall ist.
  Deshalb verwenden wir statt `@when` das allgemeinere Attribut
  `@when-custom` in Kombination mit `@calendar`, um den Kalender
  zu spezifizieren. Wenn der verwendete Kalender unbekannt ist, wird
  `calendar="unknown"` benutzt.
  Beispiele:

    ```
    <date when-custom="2001-09-11" calendar="gregorian">11 Sept 2001</date>
    ```

    ```
    <date when-custom="1001-09-11" calendar="julian">11 Sept 1001</date>
    ```

    ```
    <date when-custom="1601-09-11" calendar="unknown">11 Sept 1601</date>
    ```

- Hierarchisch übergeordnete Leerstellen (z. B. fehlendes Jahr, fehlender
  Monat) werden in `@when-custom` mit einem Bindestrich ("-") angegeben.
  Beispiele:

    ```xml
    <date when-custom="--09-11">11.9.</date>
    ```

    ```xml
    <date when-custom="---11">Elfter Tag eines Monats</date>
    ```

- Hierarchisch untergeordnete Leerstellen (z. B. fehlender Tag) werden hingegen
  nicht mit `@when-custom` ausgezeichnet, sondern wie eine uneindeutige
  Datierung als Zeitraum mit `@from-custom` und `@to-custom` ausgezeichnet.
  Beispiel:
  `<date from-custom="1001-09-01" to-custom="1001-09-30" calendar="julian">September 1001</date>`
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

```
<date when-custom="1736-11-08" calendar="gregorian">8./22. November 1736</date>
<date when-custom="1736-11-22" calendar="gregorian"/>
```

### 3.2 Zeiträume

#### 3.2.1 Durchgehende Zeiträume

Zeiträume werden mit den Attributen `@from-custom` und `@to-custom` zusammen mit
`@calendar` innerhalb von [`<date>`](date.de.md) oder
[`<origDate>`](origDate.de.md) ausgezeichnet.
Beispiele:

```
<date from-custom="1521-12-11" to-custom="1544-04-16"
      calendar="julian">11. Dezember 1521 - 16. April 1544</date>
```

```
<date from-custom="1717-01-01" to-custom="1718-12-31"
      calendar="gregorian">1717-1718</date>
```

#### 3.2.2 Unterbrochene Zeiträume

Liegen unterbrochene Zeiträumen vor, werden diese wie mehrere Zeiträume
behandelt.
Beispiele:

```
<date from-custom="1610-01-01" to-custom="1610-12-31"
      calendar="gregorian">1610, 1620–1635</date>
```

```
<date from-custom="1620-01-01" to-custom="1635-12-31"
      calendar="gregorian"/>
```

```
<date when-custom="1466-05-25" calendar="julian">25. Mai und 25.
    Heumonat 1466</date><date when-custom="1466-07-25" calendar="julian"/>
```

#### 3.2.3 Uneindeutige Datierungen, die zugeordnet werden können

Unsichere Jahresangaben, zum Beispiel «wohl 1491», werden mit
[`<precision>`](precision.de.md) ausgezeichnet.
Beispiel:

```
<date from-custom="1491-01-01" to-custom="1491-12-31" calendar="julian">wohl 1491
    <precision match="@from-custom @to-custom" precision="medium"/>
</date>
```

Datierungen, die nicht eindeutig sind, jedoch zugeordnet werden können,
werden als Zeiträume mit `@from-custom` und `@to-custom` zusammen mit
`@calendar` sowie [`<precision>`](precision.de.md) ausgezeichnet.

| Beispiel          | Werte `@from-custom` und `@to-custom` | Zeitspanne  |
|-------------------|---------------------------------------|-------------|
| 15. Jh.           | 1401-01-01/1500-12-31                 | 100 Jahre   |
| 1. Hälfte 15. Jh. | 1401-01-01/1450-12-31                 | 50 Jahre    |
| 2. Hälfte 15. Jh. | 1451-01-01/1500-12-31                 | 50 Jahre    |
| Anfang 15. Jh.    | 1401-01-01/1425-12-31                 | 25 Jahre    |
| Ende 15. Jh.      | 1475-01-01/1500-12-31                 | 25 Jahre    |
| Ca. 1510          | 1500-01-01/1520-12-31                 | +/-10 Jahre |
| Mitte 15. Jh.     | 1440-01-01/1460-12-31                 | +/-10 Jahre |
| Mitte 1555        | 1555-06-01/1555-07-31                 | +/-1 Monat  |
| Anfang März       | --03-01/--03-10                       | 10 Tage     |
| Mitte Februar     | --04-09/--04-19                       | +- 5 Tage   |
| Mitte März        | --03-10/--03-20                       | +- 5 Tage   |
| Ende März         | --03-22/--03-31                       | 10 Tage     |

#### 3.2.4 Uneindeutige Datierungen, die nicht zugeordnet werden können

Datierungen, die nicht eindeutig sind und nicht zugeordnet werden können,
sollen mit möglichst präziser Annäherung als Zeiträume mit `@notBefore-custom`
und `@notAfter-custom` sowie [`<precision>`](precision.de.md) ausgezeichnet
werden.

| Beispiel               | Werte `@notBefore-custom` und `@notAfter-custom` | Zeitspanne:      |
|------------------------|--------------------------------------------------|------------------|
| vor 1700               | 1675-01-01/1699-12-31                            | -25 Jahre        |
| nach 1700              | 1701-01-01/1725-12-31                            | +25 Jahre        |
| um 1700                | 1690-01-01/1710-12-31                            | +/-10 Jahre      |
| wohl 1700 oder 1700?   | 1700-01-01/1700-12-31                            | 1 Jahr           |
| vor 20. November 1700  | 1700-01-01/1700-11-19                            | von Jahresanfang |
| nach 20. November 1700 | 1700-11-21/1700-12-31                            | bis Jahresende   |
| vor Oktober 1700       | 1700-07-01/1700-09-30                            | -3 Monate        |
| nach Oktober 1700      | 1700-11-01/1701-01-31                            | +3 Monate        |

#### 3.2.5 Datierungen _post quem_ bzw. _ante quem_

_Post quem_-Datierungen erhalten kein [`<precision>`](precision.de.md),
jedoch das errechnete End- bzw. Beginndatum.

Wenn bei Amtsbezeichnungen nur bekannt ist, bis wann jemand im Amt war,
rechnen wir für den Amtsbeginn mit -10 Jahren.
Der Inhalt von `@notAfter-custom` ist sicher, nicht aber der Inhalt in
`@notBefore-custom`, weshalb er ein [`<precision>`](precision.de.md) erhält.
Beispiel:

```
<date notBefore-custom="1489-01-01" notAfter-custom="1499-12-31"
      calendar="julian">[Amtszeit] bis 1499
    <precision match="@notBefore-custom" precision="medium"/>
</date>
```

Dasselbe gilt auch umgekehrt für Datierungen _ante quem_.

## 4 «Fälschungen» / Datierungsänderungen

Wenn eine Fälschung ediert wird, ist das Datum der Fälschung relevant
und nicht die Datierung im Quellentext.
Ein erklärender Kommentar ist notwendig.

Weicht eine Datierung im Regest von einer Datierung im Quellentext ab,
ist ein Kommentar obligatorisch.

## 5 Neuer Stil / alter Stil

Für die Zeit nach der
[Kalenderreform](http://www.hls-dhs-dss.ch/textes/d/D12812.php),
d. h. die Zeit, in der sowohl der julianische Kalender (alter Stil)
als auch der gregorianische Kalender (neuer Stil)
verwendet wurden, gelten folgende Regelungen:

1. In den Quellen vorkommende Daten werden so belassen, wie sie in der Quelle
   stehen. Sie werden nicht auf den neuen Stil umgeschrieben. In den Attributen
   (`@when-custom`, `@from-custom`, `@to-custom` etc.) wird das Datum nach dem
   in der Quelle verwendeten Kalender zugrunde gelegt.
   Beispiel:
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="julian">Zwischen 3. und 20. September 1588</date>
    ```
2. Gibt eine Quelle ein Datum in beiden Stilen an (doppelte Datierung), wird
   in den Attributen das Datum nach dem neuen Stil verwendet.
   Beispiel:
    ```
    <date when-custom="1590-10-25"
          calendar="gregorian">25/15. octobris anno 90</date>
    ```
3. Wenn ein Dokument nicht von einer Behörde stammt, die nachgewiesenermassen
   nach altem Stil datiert (z. B. die Kanzleien von Zürich und Bern), wird bei
   einem unkommentierten Datum von einer Datierung nach neuem Stil ausgegangen.
4. Wo nicht sicher ist, nach welchem Stil datiert wurde und begründete Zweifel
   an einer Datierung nach neuem Stil vorliegen, wird dies innerhalb von
   `@calendar` mit dem Wert `unknown` festgehalten.
   Eine Anmerkung mit [`<note>`](note.de.md) ist in diesen Fällen sinnvoll.
   Beispiel:
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="unknown">Zwischen 3. und 20. September 1588</date>
    <note>Es finden sich keine Informationen zum Kalenderwechsel.</note>
    ```
5. In den editorischen Paratexten (z. B. Einleitungen, Kommentare etc.) sollten
   die Bearbeitenden den neuen Stil verwenden, sofern sie nicht explizit auf
   die Verwendung des alten Stils hinweisen möchten.
   Beispiel:
   ```
    am <date when-custom="1588-09-03" calendar="julian">3. September 1588</date>
    <note>Der Verkauf des Landguts XY an die Familie Soundso wurde nicht,
    wie in der Quelle steht, am <date when-custom="1588-09-03" calendar="julian">
    3. September 1588</date>, sondern bereits <date from-custom="1587-01-01"
    to-custom="1587-12-31 calendar="gregorian">1587</date> abgeschlossen.
    Dies geht aus XYZ hervor, vgl. <bibl><ref>Hinz 1962, S. 63.</ref></bibl>
    </note>
   ```

Die sieben katholischen Orte gingen – mit Ausnahme von Ob- und Nidwalden –
am 12./22. Januar 1584 zum neuen Stil über. Obwalden und Nidwalden nahmen den
neuen Kalender einen Monat später an.
In Luzern war der Tag der Umstellung am 12. Januar 1584 alten Stils = 22.
Januar 1584 neuen Stils (StALU RP 39, fol. 7r).

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

In Genf fand der Kalenderwechsel am 13. Dezember 1700 statt ([SDS GE 4, Nr. 2947](https://www.ssrq-sds-fds.ch/online/GE_4/index.html#p_672)).

## 6 Jahresanfangsstile

Die vom üblichen Jahresanfangsstil, dem
_Circumcisionsstil_ (Jahresanfang am 1. Januar), abweichenden Stile:
_Annuntiationsstil_ (Jahresanfang am 25. März) und
_Natalstil_ (Jahresanfang am 25. Dezember)
müssen in [`<date>`](date.de.md) und
[`<origDate>`](origDate.de.md) mithilfe von `@calendar` vermerkt werden.

Der Annuntiationsstil gilt in der Diözese Lausanne und in Freiburg vom
Anfang bis in die 2. Hälfte des 15. Jahrhunderts, sonst in der Diözese
Lausanne bis in die 1. Hälfte des 16. Jahrhunderts.

In [SDS FR I/2/6](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5)
wird der Annuntiationsstil mit «n. st.» (= «nouveau style»)
angezeigt, das Datum wird aber gemäss modernem Kalender aufgelöst.
Beispiel:

```
 Ordonnance au sujet des voies de fait. 1364 (n. st.) février 4. –
 In der Quelle steht folgende Datierung:
 «... <date calendar="julian_annunciation" when-custom="1363-02-04">lo quar jor
 dou moys de febrier, in l’ant de Nostre Segnour corant per
 mil CCC et sexante et troys</date> ...»
```

Weil nun der 4. Februar in der Zeit zwischen dem 1. Januar (oder allenfalls 25.
Dezember) und dem 25. März (= Annuntiation Mariä) liegt, ediert die
Bearbeitende zu Recht den «4. Februar 1363» als den «4. Februar 1364».
