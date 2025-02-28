---
title: Erschliessungsrichtlinien
---

Bei der Erschliessung der archivalischen Quellen werden die unten beschriebenen Metadaten
im Bereich [`<sourceDesc>`](sourceDesc.de.md) mit [`<msDesc>`](msDesc.de.md) erfasst.

Im Fall von Mehrfachüberlieferung wird in [`<sourceDesc>`](sourceDesc.de.md) ein
[`<listWit>`](listWit.de.md) angelegt, innerhalb dessen jeder Textträger ein [`<witness>`](witness.de.md)
mit einem eigenen [`<msDesc>`](msDesc.de.md) erhält.

Ein [`<msDesc>`](msDesc.de.md) ist in sechs grössere Bereiche untergliedert:

- Identifizierung des Textträgers: [`<msIdentifier>`](msIdentifier.de.md)
- Titel/Name des Textträger: [`<head>`](head.de.md)
- Inhalt des Textträgers: [`<msContents>`](msContents.de.md)
- Physische Beschreibung des Textträgers: [`<physDesc>`](physDesc.de.md)
- Geschichte des Textträgers: [`<history>`](history.de.md)
- Zusätzliche Angeben zum Textträger: [`<additional>`](additional.de.md)

## Bereich [`<msIdentifier>`](msIdentifier.de.md)

Der Bereich [`<msIdentifier>`](msIdentifier.de.md) enthält erstens die Metadaten zur Institution, 
z. B. einem Archiv oder einer Bibliothek, in dem sich der Textträger befindet, und zweitens die
Angaben, mit deren Hilfe der Textträger identifiziert werden kann.

Erfasst werden:

- der Ort, in dem sich die aufbewahrende Instution befindet:  [`<settlement>`](settlement.de.md)
- der vollständige Name der Institution: ([`<repository>`](repository.de.md))
- die von der aufbewahrenden Institution vergebene Signatur: ([`<idno>`](idno.de.md))
- (optional) älteren Signaturen: [`<altIdentifier>`](altIdentifier.de.md)

In einer zweisprachigen Editionseinheit, z. B. aus Fribourg, können sowohl der Ort und der Name
der aufbewahrenden Institution als auch die Signatur des Textträgers auf Deutsch und Französisch
angegeben werden, in dem jeweils das Attribut `@xml:lang` verwendet wird.

Wenn in einer Institution mehrere Textträger unter einer Signatur geführt und nummeriert werden,
erhält die Signatur nach einem Komma eine Nummer, z. B. StAZH C III 22, Nr. 397, oder
StAZH A 6.1, Nr. 3.

Wenn ein einzelner Eintrag eines paginierten Buches ediert wird, wird der Signatur die
entsprechende Seitenzahl hinzugefügt. Die genauen Seitenzahlen werden angegeben;
auf f. (= folgende) wird verzichtet, z. B. AEN MJ-17, S. 1–3.

Wenn ein Eintrag eines foliierten Buches oder ein Eintrag in einer Loseblattsammlung ediert wird,
wird der Signatur die entsprechende Blattzahl hinzugefügt. Die Vorderseite des Blattes wird mit
r (= recto) und die Rückseite mit v (= verso) bezeichnet, z. B. StAZH B I 277, fol. 105r–109v.

Enthält ein Buch mehrere Blatt- oder Seitenzählungen, weil z. B. ursprünglich separate Hefte zu
einem Band zusammengebunden wurden, wird der Blattzahl die Bezeichnung des Hefts bzw. Teils
vorangestellt, z. B. StAZH B II 4, Teil I, fol. 15v, oder StAZH F II a 290,Teil III, fol. 3 r–v.

In Rats- und Gerichtsprotokollen, Stadtbüchern, Urkunden- und Notariatsregistern, Jahzeitbüchern
etc. kann sich mehr als ein Eintrag pro Seite bzw. Blatt befinden. Der Signatur wird nach der
Angabe der Seite bzw. Folierung der Eintrag mit Nummerierung hinzugefügt. Dabei wird von oben
nach unten durchgezählt. Befindet sich am Anfang einer Seite ein Eintrag, der bereits auf der
vorhergehenden Seite beginnt, wird er als 0 gezählt, z. B. StAZH F II c 6 b, fol. 15v (2).

Werden Beilagen nachträglich verzeichnet, wird die Signatur mit der Angabe Beilage in runden
Klammern ergänzt, z. B. StAZH C I, Nr. 249 (Beilage).

Wurde ein Textträger früher unter einer anderen Signatur geführt, dann kann die ältere Signatur
mit [`<altIdentifier>`](altIdentifier.de.md) angegeben werden. Das kommt z. B. im StAZH häufiger vor. Dort werden
die früheren Signaturen zum Nachweis der älteren Archivordnung und zur Herstellung einer Konkordanz
von viel zitierten Quellen als «Frühere Signaturen» erfasst.

## Bereich [`<head>`](head.de.md)

Eine kurze, prägnante Inhaltsangabe des edierten Textträgers wird in [`<head>`](head.de.md) erfasst.
Gibt es zu einem Dokument mehrere Textträger, so muss nur für den Textträger ein Titel vergeben
werden, der als Vorlage des edierten Textes dient.

## Bereich [`<msContents>`](msContents.de.md)

Im Bereich [`<msContents>`](msContents.de.md) werden Angaben zum Inhalt des Textträgers gemacht.

Erfasst werden:

- ein Regest: [`<summary>`](summary.de.md)
- die Sprache des Textes: [`<textLang>`](textLang.de.md)
- (optional) der Schreiber des Textes: [`<author>`](author.de.md)
- (bei Druckschriften) das Impressum: [`<docImprint>`](docImprint.de.md)

### Zum Regest:

Das Regest ist zwar aus rein technischer Sicht kein Pflichtfeld, da es bereits sehr kurze Stücke
gibt, die kein Regest aufweisen. Grundsätzlich sollte jedoch ein Regest erstellt werden.
Ein Regest ist eine inhaltliche Zusammenfassung des edierten Stücks unter Weglassung der Formeln.

Bei lateinischen Texten ist ein ausführlicheres Regest geboten.
Offnungen, Einzugsbriefe, Urbarien etc. erhalten eine Inhaltszusammenfassung.
Die verschiedenen geregelten Punkte lassen sich zu Oberthemen zusammenfassen
(z. B. «Geregelt werden ...»).

Das Regest wird modern mit möglichst einheitlichen Formulierungen verfasst, es werden keine
Quellentermini verwendet. Die Strukturierung eines langen Regests erfolgt nach inhaltlichen
Gesichtspunkten in Absätzen ([`<p>`](p.de.md)). Siegler werden ebenfalls durch Absätze abgesetzt.
Wenn in einer Urkunde erwähnt wird, dass mehrere Urkunden ausgefertigt und zerschnitten wurden,
muss dies am Schluss des Regests zusammen mit den Sieglern beschrieben werden. 

In [`<bindingDesc>`](bindingDesc.de.md) wird zudem Chirograph festgehalten, vgl. weiter unten.

Namen werden normalisiert, unter Beibehaltung der Umlaute (z. B. Ruedi, Kuoni). Personen,
die im [HLS](https://hls-dhs-dss.ch/) oder der
[GND](https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd_node.html) vorkommen,
werden danach normalisiert (Vorname und Nachname). Sind Personen nicht im HLS oder der GND
verzeichnet, werden die Vornamen und Nachnamen nach der häufigsten Schreibweise im Stück
normalisiert. Handelt es sich um einen bekannten Familiennamen, wird nach dem
[Familiennamenbuch](https://hls-dhs-dss.ch/famn/) normalisiert.

Wichtige Inhalte können im Kommentar ([`<back>`](back.de.md)) vertieft werden.

Titel sowie Berufs- bzw. Amtsbezeichnungen sind in den Metadaten und Kommentaren einheitlich
zu handhaben. Bei Massen, Gewichten und Währungen werden arabische Ziffern verwendet.
In allen andern Fällen werden die Zahlen eins bis zwölf gemäss Duden ausgeschrieben,
bei Gremien wird die Zahl generell ausgeschrieben.

Die Schreiber von Vermerken, z. B. in einer Papsturkunde, werden mit [`<persName>`](persName.de.md)
in den Vermerken in [`<ab>`](ab.de.md) ausgezeichnet und im Regest nicht speziell erwähnt.

Für Notariatssignet, Notariatszeichen oder Notariatsinstument wird der Begriff [Notarzeichen](https://termini.ssrq-sds-fds.ch/views/view-keyword.xq?id=key004763)
verwendet. Diese Beglaubigungsform wird bei Notariatsinstrumenten (analog zu Siegelurkunden)
im Regest erwähnt, z. B.:

- Der Notar beglaubigt das Instrument mit seinem Notarzeichen.
- Der Notar beglaubigt das Instrument mit seinem Notarzeichen unter Nennung von Zeugen.

### Zu den übrigen Angaben:

Die im Quellentext verwendete Sprache wird mit [`<textLang>`](textLang.de.md) angeben.
Bei mehreren Sprachen wird das Feld wiederholt in der Reihenfolge des häufigsten Vorkommens.

Bei Handschriften kann ein Schreiber, sofern er bekannt ist, mit [`<author>`](author.de.md) und darin
[`<persName>`](persName.de.md) angegeben werden. Ist der Schreiber nicht bekannt, sondern nur eine Kanzlei,
dann wird diese mit [`<orgName>`](orgName.de.md) innerhalb von [`<author>`](author.de.md) erfasst.
Sind mehrere Hände in einer Handschrift erkennbar, wird eine Handbeschreibung in
[`<handDesc>`](handDesc.de.md) angelegt, vgl. weiter unten.

Bei Druckschriften werden die Namen der Druckerei bzw. des Druckers ([`<publisher>`](publisher.de.md)) sowie
der Druckort ([`<pubPlace>`](pubPlace.de.md)) in [`<docImprint>`](docImprint.de.md) erfasst.

Sowohl die Sprache des Textes, als auch der Schreiber bzw. das Impressum werden in
[`<msItem>`](msItem.de.md) zusammengefasst.

## Bereich [`<physDesc>`](physDesc.de.md)

Der Bereich [`<physDesc>`](physDesc.de.md) beschreibt den Textträger hinsichtlich seiner physischen
Beschaffenheit. Er ist in vier Teilbereiche gegliedert.

- die Beschreibung des Textträgers als physisches Objekt: [`<objectDesc>`](objectDesc.de.md)
- die Beschreibung der Bindung (und Überlieferung): [`<bindingDesc>`](bindingDesc.de.md)
- die Beschreibung der Hände: [`<handDesc>`](handDesc.de.md)
- die Beschreibung der Siegel: [`<sealDesc>`](sealDesc.de.md)

### [`<objectDesc>`](objectDesc.de.md)

Die [`<objectDesc>`](objectDesc.de.md) enthält innerhalb von [`<supportDesc>`](supportDesc.de.md)
Angaben zum Material, zu den Massen, zur Blatt bzw. Seitenzählung und zum Erhaltungszustand
des Textzeugen.

Erfasst werden:

- das Material (der Beschreibstoff): [`<support>`](support.de.md) mit [`<material>`](material.de.md)
- die Höhe und Breite der Blätter (bzw. des Buches oder der Plica): [`<extent>`](extent.de.md) mit
  [`<dimensions>`](dimensions.de.md) und [`<height>`](height.de.md) bzw. [`<width>`](width.de.md)
- (optional) die Blattzählung des Originals und ggf. davon abweichende, eigene Zählungen:
  [`<foliation>`](foliation.de.md)
- der Erhaltungszustand des Textträgers und seine Beschädigungen: [`<condition>`](condition.de.md)

### [`<bindingDesc>`](bindingDesc.de.md)

Die [`<bindingDesc>`](bindingDesc.de.md) erhält zunächst Angaben zur Bindung. Darüber hinaus wird
z. Z. hier die Überlieferungsform als Freitext wiedergegeben. Es werden Art der Überlieferung
(z. B. Original), Form (z. B. Heft) und Umfang (z. B. 10 Blätter) in der genannten Reihenfolge
beschrieben. 

Beispiele für Art und Form wären:

 - Abschrift
 - Abschrift mit Ergänzungen
 - Aufzeichnung (Als Aufzeichnung wird auch ein Stück bezeichnet, das zwar in grossen Teilen
   eine Abschrift einer älteren Vorlage ist, aber zugleich essentielle Änderungen enthält.
 - Aufzeichnung, Rodel (aus X Stücken zusammengenäht)
 - Aufzeichnung, Rodel (Einzelblatt)
 - Ausfertigung (für «Urkundenoriginale» Projekt SSRQ LU)
 - Auszug
 - Buch
 - Druck (= Einblattdruck)
 - Druckschrift
 - Eintrag
 - Entwurf (Obwohl ein Entwurf genau genommen vor dem Ausstellungsdatum der Ausfertigung
   entstanden ist, ignorieren wir das, wenn wir nichts anderes wissen und geben dasselbe Datum
   wie die Urkunde ein.)
 - Fragment
 - Fotokopie
 - Heft
 - Insert
 - Original (In seltenen Fällen kann es auch eine «spätere Ausfertigung» geben.)
 - Regest 
 - Teilabschrift
 - Teilabschrift mit Ergänzungen
 - Vidimus
 - Übersetzung
 - Zeitgenössische Abschrift

### [`<handDesc>`](handDesc.de.md)

Erfasst werden:

- Schreiberhände, wenn es mehr als einen Hauptschreiber des Textes gibt
- sonstige wichtige, d. h. für die Textkritik wichtige Hände

Sind mehrere Schreiberhände in einer Handschrift erkennbar, muss eine Handbeschreibung
([`<handDesc>`](handDesc.de.md)) angelegt werden, in der jede Hand mit einer [`<handNote>`](handNote.de.md)
näher beschrieben wird (s. dort).

### [`<sealDesc>`](sealDesc.de.md)

Die Beschreibung der Siegel erfolgt von links nach rechts in [`<sealDesc>`](sealDesc.de.md), jedes Siegel
erhält ein eigenes ([`<seal>`](seal.de.md)).

Die Siegler bzw. die Siegelankündigung werden bzw. wird auch im Regest erfasst. In einem
Stückkommentar müssen Unstimmigkeiten zwischen Siegelankündigung und Besiegelung beschrieben
werden. Dies gilt auch für Abschriften. Siegelankündigungen, auch von fehlenden Siegeln und
Siegelabdrücken, werden im Regest erwähnt.

Massgeblich ist die Siegelankündigung in der Urkunde bzw. bei «ich»-Formulierung die
Ausstellernennung. Im Regest erfolgt am Schluss ein Standardsatz zu den genannten Sieglern bzw.
der Siegelankündigung.
    
Werden die Siegler auf der Plica oder den Pergamentstreifen namentlich genannt, werden die Namen
in [`<ab>`](ab.de.md) transkribiert, ansonsten würden wichtige Informationen (originale
Schreibweise der Siegler) verloren gehen.

Wenn der Siegelschlitz vorhanden ist, wird das entsprechend vermerkt und nicht einfach «fehlt»
geschrieben. Nur wenn sicher ist, welches Siegel fehlt, wird der Siegler erfasst. 

## Bereich [`<history>`](history.de.md)

Der Bereich [`<history>`](history.de.md) enthält in [`<origin>`](origin.de.md) die Angaben zur
Datierung und Lokalisierung eines Textträgers.

Erfasst werden:

- das Entstehungsdatum des Textträgers: [`<origDate>`](origDate.de.md)
- (optional) wenn es sich um eine Abschrift handelt, zusätzlich das Entstehungsdatum des
  Inhalts des Textträgers: [`<origDate>`](origDate.de.md)
- der Entstehungsort des Textträgers [`<origPlace>`](origPlace.de.md)
- (optional) wenn es sich um eine Abschrift handelt, zusätzlich den Entstehungsort des
  Inhalts des Textträgers: [`<origPlace>`](origPlace.de.md)
- wenn bekannt, die ausstellende Institution: [`<orgName>`](orgName.de.md)

Bei Berichten wird hier das Datum des Ereignisses, über das berichtet wird, und nicht der
Zeitpunkt, zu welchem der Bericht verfasst wurde, erfasst (Z. B.: Renward Cysat schreibt um
1600 einen Bericht über den Amstaldenhandel 1478. Unter Zeitspanne des Amstaldenhandels einordnen,
nicht um 1600. Im Kommentar muss die Datierung des Berichts selbstverständlich angegeben werden.).

Ausführliche Bemerkungen zur Datierung eines undatierten Stücks werden in einem sachkritischen
Kommentar ([`<back>`](back.de.md)) erfasst.

Der Entstehungsort eines Textträgers ([`<origPlace>`](origPlace.de.md)) wird nur dann in erfasst, wenn er im
Stück steht bzw. wenn er, z. B. bei Ratsprotokollen, sicher erschlossen werden kann. 

Ausstellungsorte, Absendeorte sowie Erlassorte werden normalisiert wiedergegeben. Bei mehreren
Ausstellungsorten erhält jeder einen eigenen ([`<origPlace>`](origPlace.de.md))


## Bereich [`<additional>`](additional.de.md)

Publikationen, wie Quelleneditionen, Regestenwerke, Inventare, Sekundärliteratur etc., werden
mit dem Kurztitel in [`<listBibl>`](listBibl.de.md) sowie vollständig in [Zotero](https://www.zotero.org/groups/5048222/ssrq/library) erfasst. Die
Publikationen werden mit Labels in `@type` und Kurztitel chronologisch absteigend aufgelistet.

Wenn ein Textträger verloren ist, erhält er keine [`<physDesc>`](physDesc.de.md). 
Stattdessen erfassen wir die Informationen zum Verlust des Textzeugen in
[`<adminInfo>`](adminInfo.de.md). 


-----------
Todo:

## Darstellung der Überlieferungssituation
Im Portal wird die Überlieferung nachvollziehbar mit Original (A), Abschrift (B), Abschrift der
Abschrift (C) und entsprechender Zählung dargestellt. Wenn ein Original fehlt, muss die beste
Abschrift als Editionsvorlage genommen werden. Bei mehreren vorhandenen Originalen sollten,
wenn möglich, die Kriterien, die zur Wahl der Editionsvorlage beitrugen, dargelegt werden.
Dasselbe gilt im Falle von Abschriften.
 
### Abschriften
####  Abschriften von Originalen
Wie weit geht man bei der Verzeichnung von weiteren Abschriften, werden z. B. viel spätere bzw.
neuzeitliche Abschriften stillschweigend weggelassen? Gewisse Stücke wurden dutzendfach
abgeschrieben, z. B. die Urkunden, die in die Fischereinung eingetragen und mit dieser immer
wieder kopiert wurden. Das Verzeichnen solcher «Tertiärüberlieferungen» (Abschriften von
Abschriften) ist ziemlich zeitaufwändig.

In der Regel sollen, wenn ein Original vorhanden ist, vor allem zeitgenössische Abschriften
verzeichnet werden. Es ist unmöglich und auch nicht sinnvoll, alle Abschriften einer wichtigen
Urkunde ausfindig zu machen und zu verzeichnen. Die Faustregel, Abschriften bis ca. 100 Jahr
danach, kann befolgt werden. Je nach Wichtigkeit eines Stücks muss die Wirkungsgeschichte in
einem Stückkommentar beschrieben werden.

#### Abweichungen der Abschriften vom Original
Wann müssen Abweichungen der Abschriften vom Original deklariert werden und wann werden sie
stillschweigend ignoriert?

Im Archivinformationssystem werden solche Abschriften als «Abschrift» erfasst. Es ist zu aufwendig,
diese mit «fehlerhaft» oder «mit Textvariante» zu beschreiben.

Enthält ein Original Textstellen, die unverständlich oder nicht mehr lesbar sind, ist es sinnvoll,
spätere Abschriften herbeizuziehen und diese mit [`<lem>`](lem.de.md) bwz. [`<rdg>`](rdg.de.md)
in der Transkription zu erfassen. Evtl. helfen sie, die Stelle zu verstehen.

Die Erneuerung einer Fischereinung von 1574 hat zwar ein paar Absätze aus der alten Einung von
1428/1519 übernommen, allerdings in anderer Reihenfolge und durchschossen mit vielen weiteren
Regelungen. In solchen Fällen wird am besten das ganze Stück transkribiert.

#### Abschriften bei fehlendem Original
Wenn von einem Dokument kein Original überliefert ist, ist die aufwendige Suche nach der
originalgetreusten Abschrift unumgänglich. Die verschiedenen Abschriften müssen miteinander
verglichen werden. Abweichende Varianten werden mit [`<lem>`](lem.de.md) bwz. [`<rdg>`](rdg.de.md)
ausgezeichnet. Die Wahl der Editionsvorlage muss in einem Stückkommentar begründet werden. 
