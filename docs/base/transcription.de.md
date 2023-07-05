---
title: Transkriptionsrichtlinien
---

# Transkriptionsregeln deutschsprachiger Texte der Sammlung Schweizerischer Rechtsquellen (SSRQ)

Grundsätzlich gilt, dass sämtliche Texte aus den Textvorlagen im geraden Schrifttypus erscheinen. Alle Texte des
Bearbeitenden werden kursiv geschrieben.

## Wichtigste Tags in der Übersicht

### Textkritische Auszeichnungen

- [[abbr]](../elements/abbr.de.md) [[expan]](../elements/expan.de.md) Abkürzungen (Abkürzungsliste fehlt noch)
- [[add]](../elements/add.de.md) [[addSpan]](../elements/addSpan.de.md) Zusätze, Nachträge, Randnotizen
- [[app]](../elements/app.de.md) Abweichende Lesungen, Textvarianten (2. Original, Kopie)
- [[corr]](../elements/corr.de.md) Normalisierungen von Verschreibern, Emendierung
- [[damage]](../elements/damage.de.md) [[damageSpan]](../elements/damageSpan.de.md) Beschädigungen des Trägermaterials
- [[del]](../elements/del.de.md) [[delSpan]](../elements/delSpan.de.md) Streichungen und Rasuren
- [[foreign]](../elements/foreign.de.md) Wörter in einer anderen Sprache als der Haupttext
- [[gap]](../elements/gap.de.md) Auslassungen seitens des Bearbeitenden
- [[handShift]](../elements/handShift.de.md) Handwechsel
- [[note]](../elements/note.de.md) sachliche Anmerkungen
- [[sic]](../elements/sic.de.md) Kennzeichnung eines Verschreibers durch den Bearbeitenden
- [[space]](../elements/space.de.md) Lücke, die der Schreiber bewusst offen gelassen hat
- [[subst]](../elements/subst.de.md) Komplexe Streichungen, Hinzufügungen
- [[supplied]](../elements/supplied.de.md) Ergänzungen des Bearbeitenden (z. B. Zeilensprung)
- [[unclear]](../elements/unclear.de.md) unsichere Lesungen

### Auszeichnungen, die der Darstellung des Editionstextes dienen

- [[ab]](../elements/ab.de.md) zeitgleiche Dorsualnotizen, Kanzleivermerke, Registraturvermerke
- [[div]](../elements/div.de.md) bzw. [[p]](../elements/p.de.md) Abschnitte im Originaltext
- [[seg]](../elements/seg.de.md) Abschnitte vom Bearbeitenden zur inhaltlichen Gliederung eines Textes
- [[figure]](../elements/figure.de.md) grafische Informationen (Notarszeichen, Federzeichnungen, L. S.)
- [[head]](../elements/head.de.md) Titel, Zwischentitel
- [[hi]](../elements/hi.de.md) höhergestellte Buchstaben
- [[lb]](../elements/lb.de.md) Zeilenumbruch
- [[orig]](../elements/orig.de.md) Originaltext im Text des Bearbeitenden
- [[pb]](../elements/pb.de.md) Seitenumbruch
- [[q]](../elements/q.de.md) direkte Rede
- [[quote]](../elements/quote.de.md) Zitat
- [[signed]](../elements/signed.de.md) Unterschrift
- [[table]](../elements/table.de.md) mit [[row]](../elements/row.de.md) und [[cell]](../elements/cell.de.md) Tabellen

### Inhaltliche Auszeichnung

- [[date]](../elements/date.de.md) Datierungen
- [[origDate]](../elements/orig.de.md) Originaldatierung
- [[measure]](../elements/measure.de.md) Masse, Gewichte, Währungen
- [[measureGrp]](../elements/measureGrp.de.md) Gruppe von Massen, Gewichten, Währungen
- [[num]](../elements/num.de.md) römische Ziffern, Zahlwörter
- [[time]](../elements/time.de.md) Zeitangaben, Fristen

### Registerdaten

- [[persName]](../elements/persName.de.md) Personen
- [[orgName]](../elements/orgName.de.md) Organisationen, Familien
- [[placeName]](../elements/placeName.de.md) Orte, Flurnamen
- [[origPlace]](../elements/origPlace.de.md) Ausstellungsort, Druckort
- [[term]](../elements/term.de.md) Lemmata, Keywords

## A Wiedergabe gedruckter Texte

### Originalgetreue Wiedergabe

Die Wiedergabe folgender Punkte erfolgt originalgetreu gemäss der Druckvorlage:

- Gross- und Kleinschreibung
- Interpunktion: Der Schrägstrich (/, Virgel) wird transkribiert, in der Regel mit Leerschlag vor und nach dem
  Schrägstrich. Das Capitulumzeichen wird jedoch nicht transkribiert.
- Diakritische Zeichen
- Zusammen- und Getrenntschreibung
- Konsonantenverdoppelungen
- Schreibvarianten der Eigennamen
- Römische Ziffern

```
<p>
    <lb/>Datum zuͦ <origPlace>Zürich</origPlace> / uff <origDate when="1525-05-10">Mitwochen
    <lb/>am .x. tag des monats Mey
    <lb/>Anno M.D.xxv.</origDate>
</p>
```

### Normalisierungen

- I/J bzw. i/j: I und j werden nicht entsprechend der Schaftlänge unterschieden. Konsequente graphematische
  Unterscheidung zwischen vokalischem i vor Konsonanten und konsonantischem j vor Vokalen.
- Schaft-s (langes s) wird durch ein normales s wiedergegeben.
- U/V bzw. u/v: U und v werden unabhängig von der Vorlage lautgetreu wiedergegeben, nämlich der Vokal mit u und der
  Konsonant mit v.
- Ligaturen werden in Einzelbuchstaben aufgelöst.
- Versalien werden nur buchstabengetreu übernommen.
- Bogensignaturen werden weggelassen.
- Kopfzeilen, Initialen und Dekorationen werden im einleitenden Kommentar erwähnt.

### Druckfehler

Eindeutige Druckfehler werden mit [[choice]](../elements/choice.de.md), [[sic]](../elements/sic.de.md) und
[[corr]](../elements/corr.de.md) korrigiert.

### Abkürzungen

Die Handhabung entspricht derjenigen der handschriftlichen Quellen (s. unten).

### Marginalien

Die Handhabung entspricht derjenigen der handschriftlichen Quellen (s. unten).

### Kustode oder Reklamante

Die Wiederholung von einem Wort oder mehreren Wörtern nach dem Seitenwechsel wird nicht speziell ausgezeichnet. Das sich
am unteren Blattende befindliche Wort wird weggelassen bzw. auf der nächsten Seite transkribiert.

## B Wiedergabe handschriftlicher Texte

Die buchstabengetreue Wiedergabe bildet die Grundregel.

## Buchstaben und Zeichen

### Versalien

Versalien werden nur buchstabengetreu übernommen. Zum Beispiel: WJR —> wir

### Konsonantenverdoppelungen

Konsonantenverdoppelungen werden buchstabengetreu wiedergegeben. Verdoppelungszeichen (Strich über m oder n, nicht aber
über mm oder nn) werden aufgelöst.

Ausnahmen:

Im folgenden Beispiel wird der Strich über dem m am besten ignoriert und einfach mit «umb» (statt «ummb») transkribiert.

[[File:umb.gif|umb.gif]]

Nasalstrich über m in Kombination mit b/p wird ignoriert: «nempt» (statt «nemmpt»).

[[Datei:Nempt.PNG]]

### Buchstaben in Form oder Verwendung vom heutigen Gebrauch abweichend

Vokale:

- e caudata (ę) wird vom gewöhnlichen e unterschieden.
- I und j werden nicht entsprechend der Schaftlänge unterschieden. Konsequente graphematische Unterscheidung zwischen
  vokalischem i vor Konsonanten und konsonantischem j vor Vokalen. In lateinischen Texten wird y oder j als i
  wiedergegeben. Bei Fällen, in denen lediglich ein Dehnungs-h zwischen j und Vollvokal geschoben wird (wie z. B. jhe
  und jhenigen), soll das j nicht durch ein i ersetzt werden.
- Distinktionszeichen über u, welche einer Verwechslung mit n vorbeugen sollen, werden nicht wiedergegeben.
- u und v werden unabhängig von der Vorlage lautgetreu wiedergegeben, nämlich der Vokal mit u und der Konsonant mit v.
- Zwei Punkte oder ein Strich über y werden weggelassen.

Konsonanten bzw. Buchstabenverbindungen:

- Von den verschiedenen Schreibweisen des Buchstabens s (normal, lang, ß) wird nur ß als besondere Form unterschieden.
  Langes s wird als gewöhnliches s geschrieben. Dreifache s (sss, sß, ßs) werden mit ss bzw. ß transkribiert (Dreifaches
  s wird zu ss, die Kombinationen sß, ßs zu ß.). Anlautendes ß wird als s wiedergegeben. Ist am langen s noch ein
  angefügtes rundes s erkennbar, wird von einer Ligatur ausgegangen und «ss» transkribiert. Sind hingegen keine Ansätze
  zu einem runden s erkennbar oder handelt es sich lediglich um einen Bindungsbogen zum nächsten Buchstaben, wird «ß»
  transkribiert. Da sich zahlreiche Übergangsformen finden, liegt die Entscheidung im Ermessen des Bearbeitenden.
  Insbesondere wenn sich beide Formen innerhalb desselben Textes finden, sind diese in der Transkription zu
  unterscheiden.

Beispiel ß mit Bindebogen
[[Datei:Beispiel ß mit Bindebogen.gif]]

Beispiel mit ss und ß
[[Datei:Beispiel mi ss und ß.gif]]

- cz, sz, tz werden gemäss Vorlage wiedergegeben. Lassen sich t und c nicht eindeutig unterscheiden, dann wird tz
  verwendet.
- dz, dc, wz etc. werden gemäss Vorlage wiedergegeben oder aufgelöst.

### Diakritische Zeichen

Diakritische Zeichen und übergeschriebene Buchstaben (z. B. aͤ, uͦ etc.) werden buchstabengetreu wiedergegeben.

Verwendung der Unicode-Sonderzeichen und der SSRQ-Schrift Lexia Fontes. (Tastaturbelegung für das einfache Tippen
der kombinierten Zeichen liegt für PC und Mac vor).

## Zahlen und Ziffern

Einzelnummern und römische Zahlen werden gemäss Vorlage ziffern- resp. buchstabengetreu wiedergegeben. Römische Zahlen
werden kleingeschrieben. Römische Zahlen und Zahlwörter werden mit [[num]](../elements/num.de.md) und @value
ausgezeichnet.

`<num value="41">xlj</num>`

Monatsnamen mit römischen Ziffern sollten ausgeschrieben werden. Zur Bezeichnung von Währungen werden Sonderzeichen
verwendet.

Eine Originaldatierung mit römischen Ziffern wird mit [[origDate]](../elements/origDate.de.md) und @when ausgezeichnet.

```
<lb/> qual cosa si è essequito sino nell'
<lb/> anno <origDate when="1558">mdlviii</origDate> all'hora più oltra è apparso a 
<lb/> n[ost]ri sig[no]ri et superiori
```

## Gross- und Kleinschreibung

Grundsätzlich gilt Kleinschreibung bei handschriftlichen Texten bis zum Ende des 18. Jahrhunderts. Grossgeschrieben
werden Satzanfänge und Eigennamen (Personen-, Familien-, Organisations-, Ort- und Flurnamen). Zu beachten sind folgende
Besonderheiten:

### Gattungsnamen

Gattungsnamen werden kleingeschrieben. Der Bearbeitende entscheidet, ob es sich um einen Eigennamen oder um einen
Appellativ handelt. In Zweifelsfällen wird die Kleinschreibung vorgezogen.

BEISPIELE: oben am bühel, eidgenossen (wenn es sich wirklich um die schweizerischen Eidgenossen handelt, wird
Eidgenossen grossgeschrieben), walser

### Respektsbezeichnungen und Anreden

Respektsbezeichnungen und Anreden werden kleingeschrieben.

BEISPIELE: üwer gnaden, gott

### Heiligennamen, Festbezeichnungen

Bei Daten und Terminen werden Wochentage und Monatsbezeichnungen sowie Beifügungen zu Heiligennamen und
Festbezeichnungen (im Gegensatz zu den früheren TR 2010) immer klein-, Heiligennamen üblicherweise grossgeschrieben.

BEISPIELE: sonntag, idus aprilis, unser frowen tag ze dem ärnde, erzengel Michael, st. Johann baptiste, ostern,
liechtmess, invocavit, uff donrstag nach sant Jacobs des meren zwölffbotten tag, uff donstag vor unser lieben frowen

### Latein

Bei adjektivischem Gebrauch im Lateinischen werden Eigennamen grossgeschrieben.

BEISPIEL: episcopus Constantiensis

### Mehrteilige Eigennamen

Bei zusammengesetzten zwei- oder mehrteiligen Eigennamen werden die Bestandteile grossgeschrieben.

BEISPIELE: zum Grossen Münster, an der Underen Straass, ein acker ze dem Bösen Möslin, St. Pelayenstift

Die Entscheidung, was ein Flurname ist und wo ein reiner Appellativ vorliegt, ist teilweise schwierig (z. B. egg oder
Egg?). Viele Orts- und Flurnamen sind mit Hilfe einer alten Karte 1:25'000 oder mit Flurnamensbücher (ortsnamen.ch)
heute noch zu identifizieren, so dass man dort mit der Grossschreibung sicher richtig liegt.

### Zusammengesetzte Familiennamen

Bei zusammengesetzten Familiennamen, die im Text in zwei oder mehreren Bestandteilen erscheinen, ist Kleinschreibung des
Namensattributs (nameLink) empfehlenswert.

`<persName>Hans am Herd</persName>`

### Vorlage

Bei handschriftlichen Texten des 19. Jahrhunderts sollte man zu Gross- und Kleinschreibung entsprechend der Vorlage
übergehen.

## Zusammen- und Getrenntschreibung

Grundsätzlich folgen Zusammen- und Getrenntschreibung der Vorlage. Bei getrennt geschriebenen Komposita kann man dem
Handschriftenbefund folgen, wenn wirklich klar und eindeutig getrennt geschrieben wird. In Zweifelsfällen kommt die
heutige Schreibweise zur Anwendung. Auch bei losen Wortverbindungen, die für heutige echte Komposita stehen, kann man
der Zusammenschreibung in der Handschrift folgen (z. B. «hohengerichten».) Ebenso mag man bei stehenden Wendungen wie
«von alterhar» oder «vor handen sein» (für vorhanden sein) bei der von der heutigen Rechtschreibung abweichenden
Schreibweise bleiben, sofern solche Schreibweisen nicht in den Handschriften selbst die Ausnahmen bilden.

Bindestriche (Auslassungsstriche) werden berücksichtigt und in der heute gebräuchlichen Form dargestellt.

Bei Flur- und Ortsnamen sollte die Zusammen- und Getrenntschreibung immer der Vorlage folgen.

Bei Worttrennungen durch Zeilenwechsel [[lb]](../elements/lb.de.md) @break="no" in der Vorlage entfällt in der
Textwiedergabe der Trennstrich.

```
geschri<lb break="no"/>ben

Ra<lb break="no"/>gatz
```

## Hervorhebungen

Hervorhebungen (Versalien, verlängerte Buchstaben, Unterstreichungen, Farben etc.) und lateinische Schrift in deutschen
Texten werden nicht dargestellt.

Hochgestellte Buchstaben werden mit [[hi]](../elements/hi.de.md) [@rend="sup" wiedergegeben.

`deß 1729<hi rend="sup">ten</hi> jahrs`

## Abkürzungen

### Häufige Abkürzungen

- Typische, im selben Schriftstück oder in mehreren Schriftstücken wiederkehrende Abkürzungen werden stehen
  gelassen, mit [[abbr]](../elements/abbr.de.md) getaggt, mit dem Abkürzungsverzeichnis verlinkt oder, wenn fehlend, ins
  Abkürzungsverzeichnis aufgenommen. Es werden keine Kürzungspunkte verwendet, da die Abkürzungen durch die Auszeichnung
  bereits als solche gekennzeichnet sind.

`<abbr>etc</abbr>`

- Kürzel, wie zum Beispiel lobl., m. g. h., tit. oder s. v., werden konsequent als Kürzel belassen und
  mit [[abbr]](../elements/abbr.de.md) ausgezeichnet. Die Auflösung erfolgt im Abkürzungsverzeichns.

`<abbr>tit</abbr>`

### Abbkürzungen auflösen

Abkürzungen in der Textvorlage werden aufgelöst, wenn es möglich und sinnvoll ist. Orthographische Gepflogenheiten des
Schreibers werden ohne besondere Kennzeichnung berücksichtigt. Einige Abkürzungen (wie z. B. Ao = anno, dz= das) sowie
Endungen werden stillschweigend aufgelöst.

Auflösungen wurden früher in Zweifelsfällen in [   ] gesetzt, in der digitalen Edition werden sie
mit [[choice]](../elements/choice.de.md), [[abbr]](../elements/abbr.de.md) und [[expan]](../elements/expan.de.md)
getaggt.

obg[e]n[ann]t[er]:

```
<choice>
    <abbr>obgnt</abbr>
    <expan>obgenannter</expan> 
</choice>

<choice>
   <abbr>7bris</abbr>
   <expan>septembris</expan> 
</choice>
```

### Abkürzungen von Mass- und Münzbezeichnungen

Abkürzungen von Mass- und Münzbezeichnungen werden ausser in Fliesstexten (Kommentaren, Bemerkungen) nicht aufgelöst und
erscheinen im Abkürzungsverzeichnis. Es werden die entsprechenden Sonderzeichen verwendet. Zur Liste der Mass- und
Münzbezeichnungen vgl. (Tastaturbelegung -> CURRENCY SYMBOLS). Zur Auszeichnung der Währungen, Masse und Gewichte
vgl. [[measure]](../elements/measure.de.md).

## Behandlung von Lücken, Schäden und Mängeln in der Textvorlage

### Lücken vom Schreiber

Vom Schreiber zwecks späterer Ergänzung bewusst gelassene Lücken (Auslassungen) wurden in analogen Bänden durch drei
Auslassungspunkte ohne Klammer gekennzeichnet und in einer textkritischen Anmerkung unter Angabe der Grösse der
Textlücke erläutert. In der digitalen Edition werden sie mit [[space]](../elements/space.de.md) getaggt unter Angabe der
Lückengrösse mit @unit und @quantity:

`<space unit="line" quantity="2"/>`

Referenzpunkte bzw. Reverenzpunkte vor Namen oder Amtsbezeichnungen wurden in der analogen Edition durch 2 Punkte ohne
Klammer wiedergegeben. In der digitalen Edition werden sie ebenfalls mit 2 Punkten ohne Klammer wiedergegeben.

### Klammern in der Editionsvorlage

Vom Schreiber in (   ) gesetzte Textteile werden identisch wiedergegeben.

### Weggelassene Textteile

Vom Schreiber irrtümlich weggelassene Textteile (z. B. beim Abschreiben übersprungene Zeile) wurden in der analogen
Edition durch einen Ersatztext aus einer anderen originalen oder kopialen Quelle oder durch den Bearbeitenden selbst im
Sinne einer sinngemässen Textwiedergabe in [   ]a ergänzt. Eine Anmerkung war notwendig.

In der digitalen Edition wird die Lücke mit [[supplied]](../elements/supplied.de.md) getaggt. Mit @reason wird der
Grund der Lücke und mit @resp das Kürzel des Bearbeitenden angegeben. Falls notwendig, kann eine
[[note]](../elements/note.de.md) gesetzt werden. Bei Ergänzungen anhand einer anderen Vorlage (2. Original, Kopie etc.)
wird mit @source auf diesen Textzeugen referenziert. Vgl. dazu auch [[app]](../elements/app.de.md).

`<supplied reason="omitted" unit="line" quantity="1" resp="PS"/>hier folgt die Ergänzung</supplied>`

Ein Textverlust infolge Mäusefrass, verblasster Tinte, Brand, Pilzbefall, Rissen, Löchern, Kassation usw. wird
mit [[damage]](../elements/damage.de.md) und [[gap]](../elements/gap.de.md) gekennzeichnet und falls möglich innerhalb
von <damage> mit [[supplied]](../elements/supplied.de.md) – oder bei Unsicherheit mit
[[unclear]](../elements/unclear.de.md) und @cert – ergänzt. Der Schaden wird innerhalb von
[[damage]](../elements/damage.de.md) mit @agent näher bezeichnet.

`<damage agent="mice"><gap unit="cm" quantity="3"/></damage>`

### Irrtümliche Wiederholungen

Irrtümliche Wiederholungen von Silben, Wörtern und Satzteilen sollen mit [[choice]](../elements/choice.de.md),
[[sic]](../elements/sic.de.md) angemerkt und mit [[corr]](../elements/corr.de.md) normalisiert werden.

```
<choice>
    <sic>das das</sic>
    <corr>das</corr>
</choice>
```

### Unsichere Lesung: [[unclear]]

Bei Wörtern mit unsicherer Lesung wurden bei der analogen Edition in einer textkritischen Anmerkung denkbare
Lesevarianten angeführt. Sie konnten zusätzlich mit [?] gekennzeichnet werden.
In der digitalen Edition werden unsichere Lesungen mit [[unclear]](../elements/unclear.de.md) getaggt. Die
Wahrscheinlichkeit der Lesung kann mit @cert angegeben werden. Falls dies nicht genügt, kann auch eine Anmerkung mit
[[note]](../elements/note.de.md) gemacht werden.

`ve<unclear cert="high">stik</unclear>lich`

### Schreib-, Sprach- und Stilfehler

Schreib-, Sprach- und Stilfehler werden im Text nicht korrigiert. In der analogen Edition wurden sie in einer
textkritischen Anmerkung erläutert oder mit einem [!] gekennzeichnet.
In der digitalen Edition werden solche Fehler mit [[choice]](../elements/choice.de.md) zusammen mit
[[sic]](../elements/sic.de.md) getaggt und mithilfe von [[corr]](../elements/corr.de.md) korrigiert.

```
<choice>
     <sic>kan</sic>
     <corr>kam</corr>
</choice>
```

### Bewusste Auslassungen von Text durch den Bearbeitenden

Bewusste Auslassungen von Text durch den Bearbeitenden (Teilabdruck) werden in der analogen Edition mit [...] und in der
digitalen mit [[gap]](../elements/gap.de.md) @reason="irrelevant" wiedergegeben. Dies sollte, wenn möglich, vermieden
werden.

Werden spätere Nachträge nicht beim Original, sondern als eigenständiges Stück ediert, können die Teile, die bereits in
einem früheren Original ediert wurden, mit [[gap]](../elements/gap.de.md) weggelassen werden. Auf das bereits edierte
Stück wird mit @source verwiesen. Eine Anmerkung in [[note]](../elements/note) oder eine Bemerkung in
[[back]](../elements/back.de.md) ist nötig.

## Behandlung redaktioneller Eingriffe des Schreibers

Grundsätzlich hat ein transkribierter Text, auch wenn er auf einer von verschiedenen Händen mehrfach überarbeiteten
Vorlage basiert, gut lesbar und verständlich zu sein. Der Bearbeitende muss sich für eine Textvariante entscheiden und
die übrigen Varianten mit tags auszeichnen. Zu beachten ist:

### Streichungen

- Auf einfache Korrekturen, die beim Schreibvorgang entstanden sind, wird nur in Ausnahmefällen hingewiesen.
- Streichungen wurden in der analogen Transkription mit a–...–a gekennzeichnet und in einer textkritischen Anmerkung
  aufgeführt.
- In der digitalen Edition werden Streichungen mit [[del]](../elements/del.de.md) getagt.

`und <del>umb</del>`

- Bei mehrfach gestrichenen Texten müssen [[delSpan]](../elements/delSpan.de.md)
  und [[anchor]](../elements/anchor.de.md)
  eingesetzt werden.

```
<p>
    <delSpan spanTo="#Streichung1"/>
    <lb/>Lieber guͥnediger her, dz klagent wir uͥch und uͥnwern reiten und truͥwen uͥch und uͥnwern reiten, ir widerent uͥns
    <lb/> und helfent, dz wir beliben, da <add place="above">bi</add> wir bilich beliben soͤlin, der dz tuͦt, so wellin wir tuͦn gern alles, dz wir tuͦn soͤlin 
    <lb/> und unser herschaft dienen vestenklich <del>als je da hat.</del>
    <anchor xml:id="Streichung1"/>
</p>
```

- Durch Streichungen unlesbar gewordene Textstellen wurden in der analogen Edition mit [...]a gekennzeichnet und mit
  einer Anmerkung versehen. In der digitalen Edition werden sie mit [[del]](../elements/del.de.md) und einem leeren
  [[gap]](../elements/gap.de.md) getaggt.

`<del><gap unit="cm" quantity="4"/></del>`

- Bei Textstellen, die mehrere Streichungen und/oder Hinzufügungen bzw. Kombinationen davon aufweisen, muss
  [[subst]](../elements/subst.de.md) verwendet werden.

### Zusätze oder Nachträge

Zusätze oder Nachträge von erster oder späterer Hand müssen in den Text aufgenommen werden und wurden in der analogen
Edition in einer textkritischen Anmerkung erklärt. In der digitalen Edition wird der Tag [[add]](../elements/add.de.md)
dafür verwendet.

- Ein Zusatz oder Nachtrag wurde in der analogen Edition in den Text aufgenommen und durch eine vorangestellte Bemerkung
  in kursiver Schrift charakterisiert. BEISPIEL: Nachtrag einer Hand des 18. Jahrhunderts

`<add hand=hand18c></add>`

- Zusätze und Nachträge werden in den fortlaufenden Text aufgenommen. In der analogen Edition wurden sie vom
  Bearbeitenden mit Anmerkungsklammern von gleich bleibenden Kleinbuchstaben für jede unterscheidbare Hand
  charakterisiert. BEISPIEL:     a–a Am Rand von anderer Hand hinzugefügt.

`<add place="margin" hand="other hand"></add>`

### Rasuren

Mit Rasuren wurde in der analogen Edition gleich verfahren wie mit Streichungen und eine textkritische Anmerkung war
erforderlich. In der digitalen Edition wird eine Rasur mit dem tag [[del]](../elements/del.de.md) und dem Attribut
@rend="rubbing" gekennzeichnet.

`<del rend="rubbing"><unclear>unsichere Lesung wegen Rasur</unclear></del>`

Wenn bei Rasuren oder auch bei heftigen Streichungen gar nichts mehr lesbar ist, wird ein leeres
[[gap]](../elements/gap.de.md) innerhalb von [[del]](../elements/del.de.md) verwendet.

`<del rend="rubbing"><gap unit="cm" quantity="1"/></del>`

### Marginalien

Bei Marginalien entschied sich in der analogen Edition der Bearbeitende, ob es sich um eine kommentierende Randbemerkung
handelt, welche in die Anmerkungen verbannt wurde, oder um einen Zusatz, der unter Umständen in den Text gesetzt werden
konnte. In der digitalen Edition werden Marginalien mit [[add]](../elements/add.de.md) getaggt.

`<add place="margin">+</add>`

### Anmerkungen

#### Textkritische Anmerkungen

Für textkritische Anmerkungen wurden in der analogen Edition Kleinbuchstaben in alphabetischer Reihenfolge und für
sachkritische Anmerkungen arabische Ziffern verwendet. Worterklärungen, z. B. für lateinische Wendungen etc.,
erfolgen in der Glossardatenbank.

#### Sachkritische Anmerkungen

In der digitalen Edition wird der tag [[note]](../elements/note.de.md) für sachkritische Anmerkungen jeglicher Art
verwendet.

Bei speziellen Wortformen, bei denen ein allgemeiner Glossareintrag [[term]](../elements/term.de.md) nicht genügt, um
sie zu verstehen, ist eine sachkritische Fussnote notwendig, in der die Übersetzung angeboten wird.

```
  <lb/>Die egenannten lüte gemeinlich, so an die herscheften ze Wolhusen gehoͤrent, und 
  <lb/> alle ir erben und nachkomen sond oͧch bi den vorgeschriben iren eiden minen herren von Oͤsterrich und jetzund minem oͤchem von Torberg oder sinen erben, ob er enwer 
  <note>enwer: hier im Sinne von nicht sein, nicht mehr leben.</note> ...
```

## Textvarianten

### Doppel- oder Mehrfachausfertigungen

Bei Doppel- oder Mehrfachausfertigungen entscheidet sich der Bearbeitende für einen einzigen Text. Varianten und
deren Besonderheiten können mit Hilfe von [[app]](../elements/app.de.md) angemerkt werden. Inhaltliche Abweichungen
der anderen Originale von der Editionsvorlage müssen zwingend angemerkt werden.

Bei mehreren vorhandenen Originalen sollten wenn möglich die Kriterien, die zur Wahl der Editionsvorlage beitrugen, in
einem Kommentar dargelegt werden. Dasselbe gilt im Falle von Abschriften.

### Abschriften

Falls nur Abschriften vorhanden sind, soll die geeignetste, d. h. die der Originalvorlage am nächsten kommende,
ediert werden. Kriterien sind: Alter, Vollständigkeit, Sorgfalt, Beglaubigung, Vidimus oder Transsumpt etc. Varianten
können angemerkt werden. Inhaltliche Abweichungen der anderen Abschriften von der Editionsvorlage müssen zwingend
angemerkt werden.

Wenn ein Original fehlt, muss die beste Abschrift als Editionsvorlage genommen werden. Das muss nicht unbedingt die
älteste sein. Der Entscheid, welche Abschrift dem Original am nächsten kommen dürfte, ist vom Bearbeitenden zu fällen
und sollte in einem Kommentar beschrieben werden.

## Strukturierung der Texte

### Abschnitte

Wo es zum besseren Verständnis notwendig erscheint, wurde der Text in der analogen Edition mit Hilfe von
Gedankenstrichen, Alineas, paragraphenweiser Nummerierung in eckigen Klammern, Mitten von Titeln etc. unterteilt. In der
digitalen Edition erfolgt die Gliederung eines Textes nach der Vorlage mit den tags [[div]](../elements/div.de.md) und
[[p]](../elements/p.de.md) – allenfalls mit einer Nummerierung innerhalb von [[seg]](../elements/seg) mit @n.

Urkunden sollten gemäss ihrem formalen Aufbau strukturiert werden (vgl. Diplomatik z. B.
[[http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html]](http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html]),
[[http://wwws.phil.uni-passau.de/histhw/TutMA/hiwi2.html]](http://wwws.phil.uni-passau.de/histhw/TutMA/hiwi2.html),
[[http://theleme.enc.sorbonne.fr/cours/diplomatique]](http://theleme.enc.sorbonne.fr/cours/diplomatique)).
Die inhaltliche Strukturierung eines Textes durch den Bearbeitenden in Absätze erfolgt mit
[[seg]](../elements/seg.de.md).

In der Regel sollten Absätze nach einem Punkt und nicht nach einem Komma erfolgen.

Kommentare bitte mit [[div]](../elements/div.de.md) (falls eine Nummerierung notwendig ist) oder
[[p]](../elements/p.de.md) strukturieren, dadurch wird die Lesbarkeit erhöht.

### Zeilenwechsel und Seitenwechsel

Zeilenwechsel wurden in der analogen Edition mit / und Seitenwechsel mit // wiedergegeben. In der digitalen Edition
werden die Zeilenwechsel mit [[lb]](../elements/lb.de.md) und die Seitenwechsel mit [[pb]](../elements/pb.de.md)
ausgezeichnet.

### Interpunktion

Die Interpunktion folgt, so weit möglich und sinnvoll, den heute im entsprechenden Sprachgebiet üblichen Regeln.
Gibt es in der Vorlage Textstellen, deren syntaktische Konstruktion nicht nach heutigen Satzbaumustern analysiert werden
kann oder deren Sinn schwer verständlich ist, wird besser auf Interpunktion verzichtet.

### Originale Titel und Zwischentitel

Originale Titel und Zwischentitel können mit [[head]](../elements/head.de.md) ausgezeichnet und optisch abgehoben
werden.

### Direkte Rede

Direkte Rede, die in der analogen Edition mit « » hervorgehoben wurde, wird in der digitalen Edition mit
[[q]](../elements/q.de.md) ausgezeichnet.

### Zitate

Zitate innerhalb eines Textes (z. B. inserierte Urkunden) werden mit [[quote]](../elements/quote.de.md) ausgezeichnet
und am Schluss des Zitats mit einer sachkritischen Anmerkung [[note]](../elements/note.de.md) versehen, in der auf den
zitierten Originaltext verwiesen wird. Ist der Originaltext ediert, kann anstelle von [[note]](../elements/note.de.md)
mit der @xml:id auf das Stück verwiesen werden.

### Tabellen

Einige Quellen, wie z. B. Rechnungen oder Zollordnungen, enthalten Tabellen, die auch als solche in der Edition
umgesetzt werden sollen. Für die Darstellung von Tabellen verwenden wir [[table]](../elements/table.de.md) mit
[[row]](../elements/row.de.md) und [[cell]](../elements/cell).

# Transkriptionsregeln lateinischer Texte der Sammlung Schweizerischer Rechtsquellen (SSRQ)

- Die Transkription folgt wie bei deutschen Texten dem Grundsatz der buchstabengetreuen Wiedergabe der Handschrift mit
  Grossschreibung der Eigennamen (aber nicht von Nomina sacra wie deus, dominus, virgo) sowie am Satzanfang.
  Entsprechend erfolgen keine Anpassungen an klassisches Latein.
- Abkürzungen werden stillschweigend aufgelöst, sofern nicht Zweifel an der korrekten Auflösung bestehen. Die
  Auflösung erfolgt gemäss (mittellateinischem) Wörterbuch, ausser bei abweichender Praxis des Schreibers.
- Konsonantisches u wird als v, vokalisches v als u transkribiert.
- i / j werden nicht unterschieden, d.h. es wird kein j transkribiert (Ausnahme: Eigennamen, z. B. Johannes).
- e caudata (ę) wird gemäss bisheriger Praxis der SSRQ umgesetzt.
- Schluss-s wird als einfaches s transkribiert und nicht als Scharf-s, da es sich lediglich um eine Ligatur handelt.
- c / t wird gemäss Vorlage transkribiert, falls nicht unterscheidbar nach der Praxis des Schreibers an anderen Stellen,
  sonst nach Wörterbuch.
- Der Gebrauch von n anstelle von m (z.B. cunque) wird übernommen, wenn der Buchstabe ausgeschrieben ist.
- Fehler werden – namentlich in Urkunden – in der Regel nicht emendiert, sondern mit [[sic]] ausgezeichnet oder im
  Apparat diskutiert.
- Römische Ziffern werden in Kleinbuchstaben gesetzt.
- Begriffe, die einzeln dekliniert werden können, werden getrennt geschrieben (z. B. Jahreszahlen, die in Papsturkunden
  in der Regel zusammen geschrieben sind). Wendungen mit Genitiv-Attribut werden in Einzelfällen als Kompositum
  zusammengeschrieben (christifideles).
- Für die Interpunktion kann grundsätzlich die moderne deutsche Kommasetzung als Richtschnur gelten. Voraussetzung für
  eine korrekte Interpunktion ist das Verständnis des Quellentextes in seinem ganzen Aufbau (Urkundenformular) wie im
  Einzelnen Wortlaut. Im Zweifelsfall ist ein Komma besser wegzulassen als zu setzen. Verschachtelungen sind durch die
  Kommasetzung korrekt wiederzugeben.