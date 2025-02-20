---
title: Richtlinien zur Metadatenerfassung
---

# 1. Richtlinien zur Metadatenerfassung

Die «Metadaten» entsprechen dem Stücktitel, der Datumszeile und der Stückbeschreibung in den gedruckten Editionseinheiten. Metadaten der Quellen- bzw. Stückbeschreibung, die zwingend oder optional im [`<teiHeader>`](teiHeader.de.md) erfasst werden müssen, sind hier beschrieben.

## Zwingende Metadaten

### Titel der Editionseinheit und Angaben zu den Bearbeitenden
Im [`<titleStmt>`](titleStmt.de.md) werden innerhalb von [`<title>`](title.de.md) der Titel der Editionseinheit, die Herausgebenden ( [`<editor>`](editor.de.md)) sowie die Verantwortung der Beteiligten an der Edition im [`<respStmt>`](respStmt.de.md) erfasst. Die meisten dieser Angaben werden durch ein Template automatisch generiert.

### Angaben zur Publikation und zur Lizenz
Das [`<publicationStmt>`](publicationStmt.de.md) enthält Elemente zur Beschreibung der Publikation und Informationen zur Lizenzierung des Stücks. Diese Angaben werden durch ein Template generiert bzw. vor der Publikation automatisch befüllt.

### Angaben zur Reihe und Identifikationsnummern
Das [`<seriesStmt>`](seriesStmt.de.md) enthält Elemente zur Beschreibung der Reihe sowie die Identifikationsnummern des Stücks. Die Angaben zur Reihe und die [UUID](https://de.wikipedia.org/wiki/Universally_Unique_Identifier) werden durch ein Template generiert. Die [`<idno>`](idno.de.md) des Stücks, die dem Filenamen entspricht, muss von Hand hinzugefügt werden. Sie folgt klaren Vorgaben, z. B. SSRQ-SG-III_4-95-1.

### Archiv/Bibliothek
Der vollständige Name des Archivs oder der Bibliothek ([`<repository>`](repository.de.md)), in dem ein Textträger aufbewahrt wird, wird mit dem Ort der Institution ([`<settlement>`](settlement.de.md)) im ([`<msIdentifier>`](msIdentifier.de.md)) erfasst.  Falls eine Editionseinheit nur ein Archiv umfasst, werden diese Angaben durch ein Template generiert.

### Signatur
Die Signatur ([`<idno>`](idno.de.md)) im ([`<msIdentifier>`](msIdentifier.de.md)) dient der Identifizierung eines Textträgers eines Archivs und entspricht der aktuellen Signatur des Archivs, in dem der Textträger liegt. 

#### Nummerierung
Wenn einzelne Textträger einer Signatur durchnummeriert werden, erhält die Signatur nach einem Komma eine Nummer, z. B. StAZH C III 22, Nr. 397, oder StAZH A 6.1, Nr. 3.

#### Paginierung
Wenn ein Eintrag eines paginierten Buches ediert wird, wird der Signatur die entsprechende Seitenzahl hinzugefügt. Die genauen Seitenzahlen werden angegegen; auf f. (= folgende) wird verzichtet, z. B. AEN MJ-17, S. 1–3.

#### Folierung
Wenn ein Eintrag eines foliierten Buches oder ein Eintrag in einer Loseblattsammlung ediert wird, wird der Signatur die entsprechende Blattzahl hinzugefügt. Die Vorderseite des Blattes wird mit r (= recto) und die Rückseite mit v (= verso) bezeichnet, z. B. StAZH B I 277, fol. 105r–109v.

Enthält ein Buch mehrere Blatt- oder Seitenzählungen, weil z. B. ursprünglich separate Hefte zu einem Band zusammengebunden wurden, wird der Blattzahl die Bezeichnung des Hefts bzw. Teils vorangestellt, z. B. StAZH B II 4, Teil I, fol. 15v, oder StAZH F II a 290,Teil III, fol. 3 r–v.

#### Mehrfacheinträge pro Seite bzw. Blatt
In Rats- und Gerichtsprotokollen, Stadtbüchern, Urkunden- und Notariatsregistern, Jahzeitbüchern etc. kann sich mehr als ein Eintrag pro Seite bzw. Blatt befinden. Der Signatur wird nach der Angabe der Seite bzw. Folierung der Eintrag mit Nummerierung hinzugefügt. Dabei wird von oben nach unten durchgezählt. Befindet sich am Anfang einer Seite ein Eintrag, der bereits auf der vorhergehenden Seite beginnt, wird er als 0 gezählt, z. B. StAZH F II c 6 b, fol. 15v (2).

#### Beilagen
Werden Beilagen nachträglich verzeichnet, wird die Signatur mit der Angabe Beilage in runden Klammern ergänzt, z. B. StAZH C I, Nr. 249 (Beilage).

### Titel
Eine kurze, prägnante Inhaltsangabe des edierten Stücks wird in [`<head>`](head.de.md) erfasst.  

### Sprache
Die im Quellentext verwendete Sprache wird mit [`<textLang>`](textLang.de.md) angeben. Bei mehreren Sprachen wird das Feld wiederholt in der Reihenfolge des häufigsten Vorkommens. 

### Trägermaterial
Der Beschreibstoff eines Textträgers – Papier oder Pergament – wird in [`<material>`](material.de.md) erfasst.

### Masse
Angabe der Masse ([`<dimensions>`](dimensions.de.md)):  Höhe ([`<height>`](height.de.md)) x Breite ([`<width>`](width.de.md)) in Zentimetern (cm).

Bei Urkunden N.N x N.N (Plica: N.N) in cm. Gemessen werden die Aussenmasse von Urkunden (ohne Siegel).

Die Dezimalstellen nach dem Punkt werden auf 0 oder 5 gerundet, da die Unterlagen häufig unregelmässige Ränder aufweisen.

Bei Büchern können die Blätter oder das Buch gemessen werden. Dies muss im Attribut [`@type`](#type.de) entsprechend angegeben werden.

### Überlieferungsform
In [`<bindingDesc>`](bindingDesc.de.md) wird die Art der Überlieferung (z. B. Original) sowie die Form (z. B. Heft) und der Umfang (z. B. 10 Blätter) in der genannten Reihenfolge beschrieben. 

Art der Überlieferung nach kontrolliertem Vokabular:

 - Abschrift
 - Abschrift mit Ergänzungen
 - Aufzeichnung (Als Aufzeichnung wird auch ein Stück bezeichnet, das zwar in grossen Teilen eine Abschrift einer älteren Vorlage ist, aber zugleich essentielle Änderungen enthält.
 - Aufzeichnung, Rodel (aus X Stücken zusammengenäht)
 - Aufzeichnung, Rodel (Einzelblatt)
 - Ausfertigung (für «Urkundenoriginale» Projekt SSRQ LU)
 - Auszug
 - Buch
 - Druck (= Einblattdruck)
 - Druckschrift
 - Eintrag
 - Entwurf (Obwohl ein Entwurf genau genommen vor dem Ausstellungsdatum der Ausfertigung entstanden ist, ignorieren wir das, wenn wir nichts anderes wissen und geben dasselbe Datum wie die Urkunde ein.)
 -  Fragment
 -  Fotokopie
 - Heft
 - Insert
 - Original (In seltenen Fällen kann es auch eine «spätere Ausfertigung» geben.)
 - Regest
 -  Teilabschrift
 - Teilabschrift mit Ergänzungen
 - Vidimus
 - Übersetzung
 - Zeitgenössische Abschrift

### Datierung
Das Entstehungsdatum eines Textträgers (type="document") und seines Inhalts (type="content") wird mit [`<origDate>`](origDate.de.md) in [`<origin>`](origin.de.md) erfasst. Im Rechtsquellenportal ist das Datum des Inhalts dasjenige Datum, das in der Datumszeile steht.

Bei Berichten wird hier das Datum des Ereignisses, über das berichtet wird, und nicht der Zeitpunkt, zu welchem der Bericht verfasst wurde, erfasst (Z. B.: Renward Cysat schreibt um 1600 einen Bericht über den Amstaldenhandel 1478. Unter Zeitspanne des Amstaldenhandels einordnen, nicht um 1600. Im Kommentar muss die Datierung des Berichts selbstverständlich angegeben werden.).

Ausführliche Bemerkungen zur Datierung eines undatierten Stücks werden in einem sachkritischen Kommentar ([`<back>`](back.de.md)) erfasst.
 
### Schlagworte
Die wichtigsten Schlagworte zum Inhalt eines Stücks werden in [`<keywords>`](keywords.de.md) erfasst. Diese Schlagworte beziehen sich in der Regel auf das gesamte Stück. 


## Optionale Metadaten
### Ältere Signaturen 
Zur Identifizierung eines Stücks können die älteren Signaturen in  [`<altIdentifier>`](altIdentifier.de.md) erfasst werden. Im StAZH werden z. B. die früheren Signaturen und Altsignaturen zum Nachweis der älteren Archivordnung und zur Herstellung der Konkordanz von vielzitierten Quellen als «Frühere Signaturen» erfasst. Es wird versucht, die älteren Signaturen chronologisch rückwärts zu sortieren. 

### Regest
Regest ([`<summary>`](summary.de.md)) ist  nur aus reich technischer Sicht kein Pflichtfeld, da es bereits sehr kurze Stücke gibt, die kein Regest aufweisen.

Das Regest ist eine inhaltliche Zusammenfassung des edierten Stücks unter Weglassung der Formeln. Bei lateinischen Texten wird ein ausführlicheres Regest geboten.

Offnungen, Einzugsbriefe, Urbarien etc. erhalten eine Inhaltszusammenfassung. Die verschiedenen geregelten Punkte lassen sich zu Oberthemen zusammenfassen (z. B. «Geregelt werden ...»).

Moderne, möglichst einheitliche Formulierungen, keine Verwendung von Quellentermini.

Strukturierung eines langen Regests nach inhaltlichen Gesichtspunkten mit Alineas ([`<p>`](p.de.md)).

Siegler werden durch Alinea abgesetzt.

Wenn in einer Urkunde erwähnt wird, dass mehrere Urkunden ausgefertigt und zerschnitten wurden, muss dies am Schluss des Regests zusammen mit den Sieglern beschrieben werden. Im  [`<bindingDesc>`](bindingDesc.de.md) wird zudem Chirograph festgehalten, vgl. weiter oben.

Namen werden normalisiert, unter Beibehaltung der Umlaute (z. B. Ruedi, Kuoni). Personen, die im [HLS](https://hls-dhs-dss.ch/) oder der [GND](https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd_node.html) vorkommen, werden danach normalisiert (Vorname und Nachname). Sind Personen nicht im HLS oder der GND verzeichnet, werden die Vornamen und Nachnamen nach der häufigsten Schreibweise im Stück normalisiert. Handelt es sich um einen bekannten Familiennamen wird nach dem [Familiennamenbuch](https://hls-dhs-dss.ch/famn/) normalisiert.

Wichtige Inhalte können im Kommentar ([`<back>`](back.de.md)) vertieft werden.

Einheitliche Handhabung der Titel sowie Berufs- bzw. Amtsbezeichnungen in den Metadaten und Kommentaren.

Bei Massen, Gewichten und Währungen werden arabische Ziffern verwendet. In allen andern Fällen werden die Zahlen eins bis zwölf gemäss Duden ausgeschrieben, bei Gremien wird die Zahl generell ausgeschrieben.

Die Schreiber eines Vermerks z. B. in einer Papsturkunde werden mit [`<persName>`](persName.de.md) als Personen in den Vermerken in [`<ab>`](ab.de.md) ausgezeichnet und im Regest nicht speziell erwähnt.

### Schreiber/Kanzlei, Drucker/Druckerei und Druckort eines Dokuments
#### Schreiber oder Kanzlei
Bei Handschriften kann ein Schreiber mit [`<author>`](author.de.md) und  [`<persName>`](persName.de.md) angegeben werden. Eine Kanzlei wird mit [`<orgName>`](orgName.de.md) innerhalb von [`<author>`](author.de.md) erfasst. Sind mehrere Schreiberhände in einer Handschrift erkennbar, wird eine Handbeschreibung in [`<handDesc>`](handDesc.de.md) angelegt, vgl. weiter unten.

#### Drucker oder Druckerei und Druckort
Bei Druckschriften werden die Namen der Druckerei bzw. des Druckers ([`<publisher>`](publisher.de.md)) sowie der Druckort ([`<pubPlace>`](pubPlace.de.md)) in [`<docImprint>`](docImprint.de.md) erfasst.

### Blattzählung
Eine Blattzählung kann optional in [`<foliation>`](foliation.de.md) erfasst werden.

### Erhaltungszustand
Um die Gebrauchsspuren und Beschädigungen zu dokumentieren, wird [`<condition>`](condition.de.md) mit dem Attribut [`@agent`](#agent) nach Inhalten eines kontrollierten Vokabulars befüllt. Eine detaillierte Beschreibung kann in [`<p>`](p.de.md) erfolgen.

### Beschreibung der Hände
Sind mehrere Schreiberhände in einer Handschrift erkennbar, muss eine Handbeschreibung ([`<handDesc>`](handDesc.de.md)) angelegt werden, welche die Hände innerhalb einer [`<handNote>`](handNote.de.md) datiert. Unsichere Datierungen können mit [`<precision>`](precision.de.md) angegeben werden. 

Innerhalb des edierten Textes kann mit [`@hand`](#hand) auf die hier erfassten Hände referenziert werden. Das Template hilft beim Erstellen der Handbeschreibung.

Falls eine Hand einem Schreiber zugeordnet werden kann, wird die Personenidentifikationsnummer innerhalb von [`@scribe`](#scribe) hinzugefügt.

### Beglaubigungsmittel
#### Siegel
Die Beschreibung der Siegel ([`<seal>`](seal.de.md)) erfolgt von links nach rechts im [`<sealDesc>`](sealDesc.de.md).

##### Verzeichnung der Siegler
Die Siegler bzw. die Siegelankündigung werden bzw. wird auch im Regest erfasst. In einem Stückkommentar müssen Unstimmigkeiten zwischen Siegelankündigung und Besiegelung beschrieben werden. Dies gilt auch für Abschriften. Siegelankündigungen, auch von fehlenden Siegeln und Siegelabdrücken, werden im Regest erwähnt.

 - Massgeblich ist die Siegelankündigung in der Urkunde bzw. bei «ich»-Formulierung die Ausstellernennung.

 - Im Regest erfolgt am Schluss ein Standardsatz zu den genannten Sieglern bzw. der Siegelankündigung.
    
Werden die Siegler auf der Plica oder den Pergamentstreifen namentlich genannt, werden die Namen in [`<ab>`](ab.de.md) transkribiert, ansonsten wichtige Informationen (originale Schreibweise der Siegler) verloren gehen.
 
##### Fehlende Siegel
Wenn der Siegelschlitz vorhanden ist, wird das entsprechend vermerkt und nicht einfach «fehlt» geschrieben. Nur wenn sicher ist, welches Siegel fehlt, wird der Siegler erfasst. 

#### Notarzeichen
Für Notariatssignet, Notariatszeichen oder Notariatsinstument wird der Begriff [Notarzeichen](https://termini.ssrq-sds-fds.ch/views/view-keyword.xq?id=key004763) verwendet. Diese Beglaubigungsform wird bei Notariatsinstrumenten (analog zu Siegelurkunden) im Regest erwähnt, z. B.:

- Der Notar beglaubigt das Instrument mit seinem Notarzeichen.
- Der Notar beglaubigt das Instrument mit seinem Notarzeichen unter Nennung von Zeugen.

### Ausstellungsort
Der Entstehungsort eines Texträgers ([`<origPlace>`](origPlace.de.md)) wird nur dann in [`<origin>`](origin.de.md) erfasst, wenn er im Stück steht bzw. wenn er, z. B. bei Ratsprotokollen, sicher erschlossen werden kann. 

Ausstellungsorte, Absendeorte sowie Erlassorte werden normalisiert wiedergegeben. Mehrere Ausstellungsorte werden mit «und» verbunden. 

Eine Abschrift kann zwei Entstehungsorte aufweisen: Z. B. den Ausstellungsort der abgeschriebenen Urkunde (type="content") und den Ausstellungsort des Textträgers (type="document").

### Aussteller
Ist die ausstellende Institution eines edierten Textes bekannt, kann sie mit [`<orgName>`](orgName.de.md) innerhalb von [`<origin>`](origin.de.md) erfasst werden.

### Publikationen
Publikationen, wie Quelleneditionen, Regestenwerke, Inventare, Sekundärliteratur etc., werden mit dem Kurztitel in [`<listBibl>`](listBibl.de.md) sowie vollständig in [Zotero](https://www.zotero.org/groups/5048222/ssrq/library) erfasst. Die Publikationen werden mit Labels in  [`@type`](#type) und Kurztitel chronologisch absteigend aufgelistet. 

### Verlorene Textzeugen
Wenn ein Textzeuge verloren ist, erfassen wir die Informationen zum Verlust des Textzeugen in [`<adminInfo>`](adminInfo.de.md). 


## Darstellung der Überlieferungssituation
Im Portal wird die Überlieferung nachvollziehbar mit Original (A), Abschrift (B), Abschrift der Abschrift (C) und entsprechender Zählung dargestellt. Wenn ein Original fehlt, muss die beste Abschrift als Editionsvorlage genommen werden. Bei mehreren vorhandenen Originalen sollten wenn möglich die Kriterien, die zur Wahl der Editionsvorlage beitrugen, dargelegt werden. Dasselbe gilt im Falle von Abschriften. 

Bei Mehrfachüberlieferungen wird innerhalb von [`<sourceDesc>`](sourceDesc.de.md) mit  [`<listWit>`](listWit.de.md) für jeden Textträger ein [`<witness>`](witness.de.md) angelegt und der Textzeuge in [`<msDesc>`](msDesc.de.md), wie oben beschrieben, befüllt. Das Template erstellt automatisch die UUID und die notwendigen Tags.
 
### Abschriften
####  Abschriften von Originalen
Wie weit geht man bei der Verzeichnung von weiteren Abschriften, werden z. B. viel spätere bzw. neuzeitliche Abschriften stillschweigend weggelassen? Gewisse Stücke wurden dutzendfach abgeschrieben, z. B. die Urkunden, die in die Fischereinung eingetragen und mit dieser immer wieder kopiert wurden. Das Verzeichnen solcher «Tertiärüberlieferungen» (Abschriften von Abschriften) ist ziemlich zeitaufwändig.

In der Regel sollen, wenn ein Original vorhanden ist, vor allem zeitgenössische Abschriften verzeichnet werden. Es ist unmöglich und auch nicht sinnvoll, alle Abschriften einer wichtigen Urkunde ausfindig zu machen und zu verzeichnen. Die Faustregel, Abschriften bis ca. 100 Jahr danach, kann befolgt werden. Je nach Wichtigkeit eines Stücks muss die Wirkungsgeschichte in einem Stückkommentar beschrieben werden.

#### Abweichungen der Abschriften vom Original
Wann müssen Abweichungen der Abschriften vom Original deklariert werden und wann werden sie stillschweigend ignoriert?

Im Archivinformationssystem werden solche Abschriften als «Abschrift» erfasst. Es ist zu aufwendig, diese mit «fehlerhaft» oder «mit Textvariante» zu beschreiben.

Enthält ein Original Textstellen, die unverständlich oder nicht mehr lesbar sind, ist es sinnvoll, spätere Abschriften herbeizuziehen und diese mit [`<lem>`](lem.de.md) bwz. [`<rdg>`](rdg.de.md) in der Transkription zu erfassen. Evtl. helfen sie, die Stelle zu verstehen.

Die Erneuerung einer Fischereinung von 1574 hat zwar ein paar Absätze aus der alten Einung von 1428/1519 übernommen, allerdings in anderer Reihenfolge und durchschossen mit vielen weiteren Regelungen. In solchen Fällen wird am besten das ganze Stück transkribiert.

#### Abschriften bei fehlendem Original
Wenn von einem Dokument kein Original überliefert ist, ist die aufwendige Suche nach der originalgetreusten Abschrift unumgänglich. Die verschiedenen Abschriften müssen miteinander verglichen werden. Abweichende Varianten werden mit [`<lem>`](lem.de.md) bwz. [`<rdg>`](rdg.de.md) ausgezeichnet. Die Wahl der Editionsvorlage muss in einem Stückkommentar begründet werden. 
 




