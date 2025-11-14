---
title: Erschliessungsrichtlinien
---

Im Rahmen der Erschliessung der archivalischen Quellen für die SSRQ
werden die unten beschriebenen Metadaten im Bereich 
[`<sourceDesc>`](sourceDesc.de.md) und dort innerhalb von [`<msDesc>`](msDesc.de.md)
erfasst.

Im Fall von Mehrfachüberlieferung wird in [`<sourceDesc>`](sourceDesc.de.md) ein
[`<listWit>`](listWit.de.md) angelegt, innerhalb dessen jeder Textzeuge ein 
[`<witness>`](witness.de.md) mit einem eigenen [`<msDesc>`](msDesc.de.md) erhält.

Die Textzeugenbeschreibung ([`<msDesc>`](msDesc.de.md)) ist in sechs
grössere Bereiche untergliedert:

- [Identifizierung des Textzeugen](#1-identifizierung-des-textzeugen-in-msidentifier) 
  in [`<msIdentifier>`](msIdentifier.de.md)
- [Titel bzw. Name des Textzeugen](#2-titel-bzw-name-des-textzeugen-in-head)
  in [`<head>`](head.de.md)
- [Inhalt des Textzeugen](#3-inhalt-des-textzeugen-in-mscontents)
  in [`<msContents>`](msContents.de.md)
- [Physische Beschreibung des Textzeugen](#4-physische-beschreibung-des-textzeugen-in-physdesc)
  in [`<physDesc>`](physDesc.de.md)
- [Geschichte des Textzeugen](#5-geschichte-des-textzeugen-in-history) 
  in [`<history>`](history.de.md)
- [Zusätzliche Angaben zum Textzeugen](#6-zusätzliche-angaben-zum-textzeugen-in-additional) 
  in [`<additional>`](additional.de.md)

Darüber hinaus muss bei [Mehrfachüberlieferung](#7-mehrfachüberlieferung)
entschieden werden, welche Textzeugen überhaupt erfasst werden,
welcher Textzeuge die Textgrundlage bildet und wie mit Varianten
umgegangen wird.

## 1. Identifizierung des Textzeugen in [`<msIdentifier>`](msIdentifier.de.md)

### 1.1 Allgemeines
Der Bereich [`<msIdentifier>`](msIdentifier.de.md) enthält die Metadaten zur Institution, 
z. B. einem Archiv oder einer Bibliothek, in dem sich der Textzeuge befindet, 
und die Angaben, mit deren Hilfe der Textzeuge identifiziert werden kann.

Erfasst werden:

- der Ort, wo sich die aufbewahrende Institution befindet:  [`<settlement>`](settlement.de.md)
- der vollständige Name der aufbewahrenden Institution: [`<repository>`](repository.de.md)
- die von der aufbewahrenden Institution vergebene Signatur: [`<idno>`](idno.de.md)
- (optional) ältere oder alternative Signaturen: [`<altIdentifier>`](altIdentifier.de.md)

Beispiele:
```xml
<msIdentifier>
   <settlement xml:lang="de" ref="loc000165">Chur Bischöfliche Burg</settlement>
   <repository xml:lang="de">Bischöfliches Archiv Chur</repository>
   <idno xml:lang="de">BAC 011.0030</idno>
</msIdentifier>

<msIdentifier>
    <settlement xml:lang="fr" ref="loc007885">Lausanne</settlement>
    <repository xml:lang="fr">Archives cantonales vaudoises</repository>
    <idno source="http://www.davel.vd.ch/detail.aspx?id=244271" xml:lang="fr">ACV Ac 29, p. 1-3</idno>
</msIdentifier>

<msIdentifier>
    <settlement xml:lang="de" ref="loc000701">Schaffhausen</settlement>
    <repository xml:lang="de">Staatsarchiv Schaffhausen</repository>
    <idno xml:lang="de">StASH Urkunden 1/2780</idno>
    <altIdentifier>
      <idno>XV.A.13</idno>
    </altIdentifier>
</msIdentifier>
```

In einer zweisprachigen Editionseinheit, z. B. aus Fribourg, können sowohl der Ort und der Name
der aufbewahrenden Institution als auch die Signatur des Textzeugen auf Deutsch und Französisch
angegeben werden, indem jeweils das Attribut `@xml:lang` verwendet wird.

Beispiel:
```xml
<msIdentifier>
    <settlement xml:lang="de" ref="loc001060">Freiburg</settlement>
    <repository xml:lang="de">Staatsarchiv Freiburg</repository>
    <idno xml:lang="de">StAFR Thurnrodel 2, fol. 15r–16v</idno>
    <settlement xml:lang="fr" ref="loc001060">Fribourg</settlement>
    <repository xml:lang="fr">Archives de l’État de Fribourg</repository>
    <idno xml:lang="fr">AEF Thurnrodel 2, fol. 15r-16v</idno>
</msIdentifier>
```

### 1.2 Regeln für die Signaturen in [`<idno>`](idno.de.md)

#### 1.2.1 Aufbau der idno

Die Signatur besteht mindestens aus einem Kürzel der aufbewahrenden Institution
und der von dieser Institution vergebenen Signatur.
Zwischen dem Kürzel und der Signatur steht kein Komma.

Beispiel:
```xml
<idno xml:lang="fr">ACV Ac 29</idno>
```
und nicht:
```xml
<idno xml:lang="fr">ACV, Ac 29</idno>
```
#### 1.2.2 Unterscheidungsnummern

Wenn in einer Institution mehrere Textzeugen unter einer Signatur
geführt und nummeriert werden, erhält die Signatur nach einem Komma
eine Unterscheidungsnummer.

Beispiele:
```xml
<idno xml:lang="de">StAZH C III 22, Nr. 397</idno>
<idno xml:lang="de">StAZH A 6.1, Nr. 3</idno>
```

#### 1.2.3 Abschnitt aus einem paginierten Textzeugen

Wenn nur ein Abschnitt eines paginierten Textzeugen ediert wird,
wird der Signatur die entsprechende Stellenangabe hinzugefügt.
Dabei werden die genauen Seitenzahlen angegeben,
auf `f.` bzw. `ff.` (= folgende) wird verzichtet.
Die Paginierung wird mit `S.` (deutsch) bzw. `p.` (französisch)
angezeigt.

Beispiele:
```xml
<idno xml:lang="de">STAW AG 91/1/42.6, S. 3-7</idno>
<idno xml:lang="fr">AVN B 101.01.01.004, p. 333</idno>
```

#### 1.2.4 Abschnitt aus einem foliierten Textzeugen

Wenn nur ein Abschnitt eines foliierten Textzeugen ediert wird,
wird der Signatur die entsprechende Blattzahl hinzugefügt. 
Die Vorderseite des Blattes wird mit `r` (= recto) und die
Rückseite mit `v` (= verso) bezeichnet.
Die Foliierung wird mit `fol.` (deutsch und französisch)
angezeigt.

Beispiele:
```xml
<idno xml:lang="de">StAZH B I 273, fol. 881r–884v</idno>
<idno xml:lang="fr">AVN B 101.14.001, fol. 531r-v</idno>
```

#### 1.2.5 Abschnitt aus einem Textzeugen mit mehreren Teilen

Enthält ein Textzeuge mehrere Blatt- oder Seitenzählungen,
weil z. B. ursprünglich separate Hefte zu einem Band zusammengebunden
wurden, wird der Blattzahl die Bezeichnung des Hefts bzw. Teils
vorangestellt.

Beispiele:
```xml
<idno xml:lang="de">StAZH B II 4, Teil I, fol. 15v</idno>
<idno xml:lang="de">StAZH F II a 290, Teil III, fol. 3r–v</idno>
```

#### 1.2.6 Einträge

In Rats- und Gerichtsprotokollen, Stadtbüchern, Urkunden- und
Notariatsregistern, Jahrzeitbüchern etc. kann sich mehr als ein Eintrag
pro Seite bzw. Blatt befinden. Der Signatur wird nach der Angabe der Seite 
bzw. des Blattes die Nummer des Eintrags hinzugefügt. Dabei wird von oben
nach unten durchgezählt. Befindet sich am Anfang einer Seite ein Eintrag, 
der bereits auf der vorhergehenden Seite beginnt, wird dieser nicht mitgezählt.

Beispiele:
```xml
<idno xml:lang="de">StAZH B III 4, fol. 21v, Eintrag 1</idno>
<idno xml:lang="de">StAGR AB IV 01/007.65, S. 536, Eintrag 2</idno>
```

#### 1.2.7 Beilagen

Wird nicht der unter einer Signatur verzeichnete Textzeuge selbst ediert,
sondern eine Beilage oder ein Abschnitt einer Beilage, dann wird die Signatur
um die Angabe `Beilage` ergänzt. Gibt es mehrere Beilagen, werden diese nummeriert.
Wird nur ein Teil einer Beilage ediert, dann wird dies mit einer entsprechenden
Seitenzählung angegeben.

Beispiel:
```xml
<idno xml:lang="de">StAZH C I, Nr. 249, Beilage</idno>
<idno xml:lang="de">StAZH C I, Nr. 3165, Beilage 17</idno>
<idno xml:lang="de">StAZH C I, Nr. 3165, Beilage 2, S. 3-4</idno>
```

### 1.3 Alternative oder ältere Signaturen

Wurde ein Textzeuge früher unter einer anderen Signatur geführt
oder ist er in der Forschungsliteratur unter einem anderen Namen bekannt,
dann kann diese alternative Bezeichnung mit [`<altIdentifier>`](altIdentifier.de.md)
angegeben werden. Das kommt z. B. im StASH häufiger vor. Dort werden
die früheren Signaturen zum Nachweis der älteren Archivordnung
und zur Herstellung einer Konkordanz von viel zitierten Quellen erfasst.

Beispiele:
```xml
<idno xml:lang="de">StASH Urkunden 1/2780</idno>
<altIdentifier>
  <idno>XV.A.13</idno>
</altIdentifier>

<idno xml:lang="fr">AEN 2ACHA-1.33</idno>
<altIdentifier>
    <idno>AC 106/1</idno>
</altIdentifier>
```

## 2. Titel bzw. Name des Textzeugen in [`<head>`](head.de.md)

Eine kurze, prägnante Inhaltsangabe des edierten Textzeugen wird in 
[`<head>`](head.de.md) erfasst. Gibt es zu einem Dokument mehrere
Textzeugen, so muss nur für den Textzeugen, der als Vorlage des
edierten Textes dient, ein Titel erfasst werden.

Beispiele:
```xml
<head>Verordnung über die Dienstpflicht in Winterthur</head>
<head>Eid von Gesellen und anderen Angestellten</head>
<head>Sentence et remise au bras séculier de Pierre de la Prélaz</head>
<head>Loi des Trois-États sur les dommages causés aux bois et leur réparation</head>
```

In zweisprachigen Editionseinheiten, z. B. in Fribourg, kann sowohl
ein deutschsprachiger als auch ein französischsprachiger Titel erfasst werden.
In diesem Fall muss mit `@xml:lang` die Sprache angegeben werden.

Beispiele:
```xml
<head xml:lang="de">Françoise Dévaud-Clerc – Urteil</head>
<head xml:lang="fr">Françoise Dévaud-Clerc – Jugement</head>

<head xml:lang="de">Eid des städtischen Steinhauers, Zimmermeisters, Dachdeckers und Wagners</head>
<head xml:lang="fr">Serment des tailleur de pierre, maître charpentier, couvreur et charron de la ville</head>
```

## 3. Inhalt des Textzeugen in [`<msContents>`](msContents.de.md)

### 3.1 Allgemeines

Im Bereich [`<msContents>`](msContents.de.md) werden Angaben zum Inhalt des Textzeugen gemacht.

Erfasst werden:

- ein Regest: [`<summary>`](summary.de.md)
- die Sprache des Textes: [`<textLang>`](textLang.de.md)
- (optional bei Handschriften) der Schreiber des Textes: [`<author>`](author.de.md)
- (bei Druckschriften) das Impressum: [`<docImprint>`](docImprint.de.md)

Die Angaben zu Sprache, Schreiber und Impressum werden in [`<msItem>`](msItem.de.md) zusammengefasst.

Beispiele:

```xml
<msContents>
    <summary>
        <p>
            Die Abgeordneten von Propst und Kapitel des Grossmünsters sind vor Bürgermeister
            und Rat der Stadt Zürich erschienen und haben diese gebeten, Verordnete zu ernennen, 
            um mit diesen Artikel zur Verbesserung des Stifts auszuarbeiten.
        </p>
    </summary>
    <msItem>
        <textLang xml:lang="de"/>
        <docImprint>
            <pubPlace ref="loc000065" cert="high">Zürich</pubPlace>
            <publisher cert="high">Christoph Froschauer der Ältere</publisher>
        </docImprint>
    </msItem>
</msContents>

<msContents>
    <summary xml:lang="de">
        <p>
            Schultheiss und Rat von Winterthur erlassen eine Ordnung für das
            Sondersiechenhaus. Sie erlegen den Insassen Pflichten auf bezüglich
            Eidleistung, Austragung von Konflikten mit dem Pfleger und Gebet.
        </p>
    </summary>
    <msItem>
        <textLang xml:lang="de"/>
        <author role="scribe">
            <persName ref="per027325">Georg Bappus</persName>
        </author>
    </msItem>
</msContents>
```

In zweisprachigen Editionseinheiten, z. B. Fribourg, kann es für jede Sprache
der Editionseinheit ein eigenes Regest geben. In diesem Fall werden die Regesten
mit `@xml:lang` unterschieden.

Beispiel:
```xml
<msContents>
    <summary xml:lang="de">
        <p>
            Christine Bovigny-Corby aus Greyerz wird der Hexerei verdächtigt. 
            Sie wird mehrfach befragt und gefoltert, ohne ein Geständnis abzulegen. 
            Sie wird in ihre Wohngegend verbannt, d.h. nach Sorens oder Avry-devant-Pont.
        </p>
    </summary>
    <summary xml:lang="fr">
        <p>
            Christine Bovigny-Corby, de Gruyères, est suspectée de sorcellerie. 
            Elle est interrogée et torturée à plusieurs reprises, mais n’avoue rien.
            Elle est condamnée au bannissement dans sa région, c’est-à-dire à Sorens
            ou à Avry-devant-Pont.
        </p>
    </summary>
</msContents>
```

### 3.2 Regest

#### 3.2.1 Definition und Zweck

Grundsätzlich sollte zu jedem Dokument, auch zu kurzen, ein Regest erstellt werden.

Ein Regest ist eine inhaltliche Zusammenfassung des edierten Stücks unter Weglassung der Formeln. 
Bei lateinischen Texten ist ein ausführlicheres Regest geboten.
Gibt es viele verschiedene geregelte Punkte, lassen sich diese zu Oberthemen zusammenfassen
(z. B. «Geregelt werden …»).

#### 3.2.2 Sprache und Struktur

Das Regest wird in moderner Sprache mit möglichst einheitlichen Formulierungen verfasst, 
es werden keine Quellentermini verwendet. 

Die Strukturierung eines langen Regests erfolgt nach inhaltlichen
Gesichtspunkten in Absätzen ([`<p>`](p.de.md)).

#### 3.2.3 Siegler und Mehrfachausfertigung

Vorhandene Siegler werden am Schluss des Regests, durch Absätze abgetrennt, aufgeführt.
Siegelankündigungen, auch von fehlenden Siegeln und Siegelabdrücken, werden ebenfalls erwähnt.

Beispiele:
```xml
<summary xml:lang="de">
    <p><!--Hier das eigentliche Regest-->…</p>
    <p>Johann Ulrich Escher, Landvogt von Sax-Forstegg, siegelt.</p>
</summary>

<summary xml:lang="de">
    <p><!--Hier das eigentliche Regest-->…</p>
    <p>Der Aussteller siegelt.</p>
    <p>Für Wartau-Gretschins siegeln Wilhelm vom Fröwis, Oswald von Prad und Rudolf Kalberer.</p>
    <p>Für Sevelen, Hans Vittler und Hans Spangolf siegelt Klaus Vittler.</p>
</summary>
```

Wenn in einer Urkunde erwähnt wird, dass mehrere Exemplare der Urkunde ausgefertigt
und zerschnitten wurden, muss dies am Schluss des Regests zusammen 
mit den Sieglern beschrieben werden.

#### 3.2.4 Personennamen

Namen werden im Regest grundsätzlich normalisiert. 
Personen, die im [HLS](https://hls-dhs-dss.ch/) oder der 
[GND](https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd_node.html) vorkommen,
werden gemäss diesen Nachschlagewerken normalisiert.
Handelt es sich um einen bekannten Familiennamen, wird nach dem [Familiennamenbuch](https://hls-dhs-dss.ch/famn/) 
normalisiert.
Sind Personen nicht im HLS oder der GND verzeichnet, werden die Vornamen und Nachnamen 
nach der häufigsten Schreibweise im Stück unter Beibehaltung der Umlaute (z. B. Ruedi, Kuoni)
normalisiert.

#### 3.2.5 Sonstige Normalisierungen

Titel sowie Berufs- bzw. Amtsbezeichnungen sind im Regest und in den Kommentaren
einheitlich zu handhaben. 

Bei Massen, Gewichten und Währungen werden arabische Ziffern verwendet.
In allen andern Fällen werden die Zahlen von eins bis zwölf gemäss Duden ausgeschrieben,
bei Gremien wird die Zahl generell ausgeschrieben.

Für `Notariatssignet`, `Notariatszeichen` oder `Notariatsinstrument` wird der Begriff 
[Notarzeichen](https://termini.ssrq-sds-fds.ch/views/view-keyword.xq?id=key004763)
verwendet. Diese Beglaubigungsform wird bei Notariatsinstrumenten (analog zu Siegelurkunden)
im Regest erwähnt.

Beispiele:
```xml
<p>Der Notar beglaubigt das Instrument mit seinem Notarzeichen.</p>
<p>Der Notar beglaubigt das Instrument mit seinem Notarzeichen unter Nennung von Zeugen.</p>
```

#### 3.2.6 Was nicht ins Regest aufgenommen wird.

Handelt es sich bei der Urkunde um ein Chirograph, wird dies nicht im Regest, sondern 
in [`<bindingDesc>`](bindingDesc.de.md) festgehalten (vgl. weiter unten).

Wichtige Inhalte können im Kommentar ([`<back>`](back.de.md)) vertieft werden,
im Regest geht es nur um eine kurze Zusammenfassung.

Die Schreiber von Vermerken ([`<ab>`](ab.de.md)), z. B. in einer Papsturkunde, 
werden mit [`<persName>`](persName.de.md) im Text ausgezeichnet und im Regest nicht speziell erwähnt.

### 3.3 Die Sprache des Textes

Die im Quellentext verwendete Sprache wird mit [`<textLang>`](textLang.de.md) angeben.
Bei mehreren Sprachen wird das Element mehrfach in der Reihenfolge des häufigsten Vorkommens
angegeben.

### 3.4 Der Schreiber des Textes

Bei Handschriften kann ein Schreiber, sofern er bekannt ist, mit [`<author>`](author.de.md) und darin mit
[`<persName>`](persName.de.md) angegeben werden. Ist der Schreiber nicht bekannt, sondern nur eine Kanzlei,
dann wird diese innerhalb von [`<author>`](author.de.md) mit Freitext erfasst.

Beispiele:
```xml
<author role="scribe">
    <persName ref="per027325">Georg Bappus</persName>
</author>

<author role="scribe">
  <persName ref="per028066">Hans Jakob Beyel</persName>, Rechenschreiber von Zürich
</author>

<author role="scribe">Schreiber der Kanzlei Liechtenstein</author>
```

Sind in einer Handschrift mehrere Hände erkennbar, wird eine Handbeschreibung in
[`<handDesc>`](handDesc.de.md) angelegt, vgl. weiter unten. Diese ist nicht mehr Teil von 
[`<msContents>`](msContents.de.md), sondern Teil der physischen Beschreibung des Textzeugen.

### 3.5 Das Impressum

Bei Druckschriften werden die Namen der Druckerei bzw. des Druckers 
([`<publisher>`](publisher.de.md)) sowie
der Druckort ([`<pubPlace>`](pubPlace.de.md)) 
in [`<docImprint>`](docImprint.de.md) erfasst.

Beispiel:
```xml
<docImprint>
    <pubPlace ref="loc000065" cert="high">Zürich</pubPlace>
    <publisher cert="high">Christoph Froschauer der Ältere</publisher>
</docImprint>
```

## 4. Physische Beschreibung des Textzeugen in [`<physDesc>`](physDesc.de.md)

### 4.1 Allgemeines

Der Bereich [`<physDesc>`](physDesc.de.md) beschreibt den Textzeugen hinsichtlich 
seiner physischen Beschaffenheit. Er ist in vier Teilbereiche gegliedert.

- die [Beschreibung des Textzeugen als physisches Objekt](#42-beschreibung-des-textzeugen-als-physisches-objekt-in-objectdesc)
  in [`<objectDesc>`](objectDesc.de.md)
- die [Beschreibung der Bindung (und Überlieferung)](#43-beschreibung-der-bindung-und-überlieferung-in-bindingdesc)
  in [`<bindingDesc>`](bindingDesc.de.md)
- die [Beschreibung der Hände](#44-beschreibung-der-hände-in-handdesc)
  in [`<handDesc>`](handDesc.de.md)
- die [Beschreibung der Siegel](#45-beschreibung-der-siegel-in-sealdesc)
  in [`<sealDesc>`](sealDesc.de.md)

### 4.2 Beschreibung des Textzeugen als physisches Objekt in [`<objectDesc>`](objectDesc.de.md)

Die [`<objectDesc>`](objectDesc.de.md) enthält innerhalb von [`<supportDesc>`](supportDesc.de.md)
Angaben zum Material, zu den Massen, zur Blatt- bzw. Seitenzählung 
und zum Erhaltungszustand des Textzeugen.

Erfasst werden:

- das Material, d. h. der Beschreibstoff: [`<support>`](support.de.md) mit [`<material>`](material.de.md)
- die Höhe und Breite der Blätter (bzw. des Buches oder der Plica): [`<extent>`](extent.de.md) mit
  [`<dimensions>`](dimensions.de.md) und [`<height>`](height.de.md) bzw. [`<width>`](width.de.md)
- (optional) der Erhaltungszustand des Textträgers und seine Beschädigungen: [`<condition>`](condition.de.md)
- (optional) die Blattzählung des Originals und ggf. davon abweichende, eigene Zählungen:
  [`<foliation>`](foliation.de.md)


Beispiel:
```xml
<objectDesc>
    <supportDesc>
        <support>
            <material type="parchment"/>
        </support>
        <extent>
            <dimensions type="leaves">
                <height unit="cm" quantity="25.0"/>
                <width unit="cm" quantity="38.0"/>
            </dimensions>
            <dimensions type="plica">
                <width unit="cm" quantity="6.0"/>
            </dimensions>
        </extent>
        <condition agent="water">
            <p>Feuchtigkeitsschäden (mit Textverlust)</p>
        </condition>
        <foliation>
            <p>Paginierung des 20. Jahrhunderts</p>
        </foliation>
    </supportDesc>
</objectDesc>
```

### 4.3 Beschreibung der Bindung (und Überlieferung) in [`<bindingDesc>`](bindingDesc.de.md)

Die [`<bindingDesc>`](bindingDesc.de.md) enthält zunächst Angaben zur Bindung. 

Darüber hinaus wird hier z. Z. die Überlieferungsform als Freitext wiedergegeben. 
Es werden Art der Überlieferung (z. B. Original), Form (z. B. Heft) und Umfang
(z. B. 10 Blätter) in der genannten Reihenfolge beschrieben.

Beispiele für Art und Form wären:

 - Abschrift
 - Abschrift mit Ergänzungen
 - Aufzeichnung (als Aufzeichnung wird auch ein Stück bezeichnet, das zwar in grossen Teilen
   eine Abschrift einer älteren Vorlage ist, aber zugleich essenzielle Änderungen enthält.
 - Aufzeichnung, Rodel (aus X Stücken zusammengenäht)
 - Aufzeichnung, Rodel (Einzelblatt)
 - Ausfertigung (für «Urkundenoriginale»)
 - Auszug
 - Buch
 - Druck (= Einblattdruck)
 - Druckschrift
 - Eintrag
 - Entwurf (Obwohl ein Entwurf genau genommen vor dem Ausstellungsdatum der Ausfertigung
   entstanden ist, ignorieren wir das, wenn wir nichts anderes wissen und geben dasselbe Datum
   wie das der Urkunde ein.)
 - Fotokopie
 - Fragment
 - Heft
 - Insert
 - Original (In seltenen Fällen kann es auch eine «spätere Ausfertigung» geben.)
 - Regest 
 - Teilabschrift
 - Teilabschrift mit Ergänzungen
 - Übersetzung
 - Vidimus
 - Zeitgenössische Abschrift

### 4.4 Beschreibung der Hände in [`<handDesc>`](handDesc.de.md)

Erfasst werden:

- Schreiberhände, wenn es mehr als einen Hauptschreiber des Textes gibt
- sonstige wichtige, d. h. für die Textkritik wichtige Hände

Sind mehrere Schreiberhände in einer Handschrift erkennbar, muss eine
[`<handDesc>`](handDesc.de.md) angelegt werden, in der jede Hand mit einer [`<handNote>`](handNote.de.md)
näher beschrieben wird (vgl. dort und den Abschnitt 
[Schreiber und Hände](scribes-and-hands.de.md)
in den Transkriptionsrichtlinien).

### 4.5 Beschreibung der Siegel in [`<sealDesc>`](sealDesc.de.md)

Die Beschreibung der Siegel erfolgt von links nach rechts innerhalb von [`<sealDesc>`](sealDesc.de.md), 
jedes Siegel erhält ein eigenes ([`<seal>`](seal.de.md)).

Die Siegler bzw. die Siegelankündigungen werden auch im Regest erfasst. Im Kommentar 
müssen Unstimmigkeiten zwischen Siegelankündigung und Besiegelung beschrieben werden. 
Dies gilt auch für Abschriften.

Massgeblich ist die Siegelankündigung in der Urkunde bzw. bei «ich»-Formulierung die
Ausstellernennung.
    
Werden die Siegler auf der Plica oder den Pergamentstreifen namentlich genannt, werden die Namen
in [`<ab>`](ab.de.md) transkribiert, ansonsten würden wichtige Informationen (z. B. die originale
Schreibweise der Siegler) verloren gehen.

Wenn der Siegelschlitz vorhanden ist, wird das entsprechend vermerkt. 
Nur wenn sicher ist, welches Siegel fehlt, wird der Siegler erfasst. 

## 5. Geschichte des Textzeugen in [`<history>`](history.de.md)

Der Bereich [`<history>`](history.de.md) enthält in [`<origin>`](origin.de.md) die Angaben zur
Datierung und Lokalisierung eines Textzeugen.

Erfasst werden:

- das Entstehungsdatum des Textzeugen: [`<origDate>`](origDate.de.md) mit `type="document"`
- (optional) wenn es sich um eine Abschrift handelt, zusätzlich das Entstehungsdatum des
  mutmasslichen Originals: [`<origDate>`](origDate.de.md) mit `type="content"`
- der Entstehungsort des Textträgers [`<origPlace>`](origPlace.de.md) mit `type="document"`
- (optional) wenn es sich um eine Abschrift handelt, zusätzlich der Entstehungsort des
  mutmasslichen Originals: [`<origPlace>`](origPlace.de.md) mit `type="content"`
- (optional) die ausstellende Institution: [`<orgName>`](orgName.de.md)

Beispiele:
```xml
<origin>
    <origDate type="document" from-custom="1460-01-01" to-custom="1460-12-31" calendar="julian"/>
    <origDate type="content" when-custom="1440-12-22" calendar="julian"/>
    <origPlace type="document" ref="loc000161.05">Bâle</origPlace>
    <origPlace type="content" ref="loc000161.05">Bâle</origPlace>
</origin>

<origin>
    <origDate type="document" when-custom="1702-05-17" calendar="gregorian"/>
    <origPlace type="document" ref="loc007646">Genève</origPlace>
    <orgName role="issuer" ref="org010746">Petit Conseil</orgName>
</origin>
```

Bei Berichten über ein Ereignis, wird das Datum des Ereignisses, über das berichtet wird,
mit ```<origDate type="content"``` und der Zeitpunkt, zu welchem der Bericht verfasst wurde,
mit ```<origDate type="document"``` erfasst. Z. B.: Renward Cysat schreibt um
1600 einen Bericht über den Amstaldenhandel 1478, dann wird das wie folgt kodiert.
Zu den Datierungen selbst vgl. die [Datierungsrichtlinien](dating_guidelines.de.md).

Beispiel:
```xml
<origin>
    <origDate type="content" from-custom="1478-01-01" to-custom="1478-12-31" calendar="julian"/>
    <origDate type="document" from-custom="1590-01-01" to-custom="1610-12-31" calendar="gregorian"/>
</origin>
```

Ausführliche Bemerkungen zur Datierung eines undatierten Stücks werden in einem
Kommentar ([`<back>`](back.de.md)) erfasst.

Der Entstehungsort eines Textzeugen ([`<origPlace>`](origPlace.de.md)) wird nur dann erfasst, wenn er im
Dokument steht bzw. wenn er, z. B. bei Ratsprotokollen, sicher erschlossen werden kann. 

Ausstellungsorte, Absendeorte sowie Erlassorte werden normalisiert wiedergegeben. Bei mehreren
Ausstellungsorten erhält jeder einen eigenen ([`<origPlace>`](origPlace.de.md)).

Beispiel:
```xml
<origin>
    <origDate type="document" from-custom="1448-03-17" to-custom="1448-03-23" calendar="julian"/>
    <origPlace type="document" ref="loc008831.01">Hôpital Marie-Madeleine du Mont-Joux</origPlace>
    <origPlace type="document" ref="loc008768.01">Château de La Tour-de-Peilz</origPlace>
</origin>
```

## 6. Zusätzliche Angaben zum Textzeugen in [`<additional>`](additional.de.md)

Publikationen, wie Quelleneditionen, Regestenwerke, Inventare, Sekundärliteratur etc., 
werden mit dem Kurztitel in [`<listBibl>`](listBibl.de.md) sowie vollständig in 
[Zotero](https://www.zotero.org/groups/5048222/ssrq/library) erfasst. 
Die Publikationen werden mit Labels in `@type` und Kurztitel chronologisch
absteigend aufgelistet.

Beispiel:
```xml
<additional>
    <listBibl type="edition">
        <bibl><ref target="https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_106">SSRQ SG III/2, Nr. 46</ref></bibl>
        <bibl><ref>Graber, Urkundensammlung,</ref> Nr. 1</bibl>
    </listBibl>
    <listBibl type="summary">
        <bibl><ref target="http://permalink.snl.ch/bib/chbsg000067077">Reich-Langhans, Chronik</ref>, S. 100</bibl>
    </listBibl>
    <listBibl type="literature">
        <bibl><ref target="http://permalink.snl.ch/bib/chbsg000124577">Gabathuler 2011</ref>, S. 249</bibl>
    </listBibl>
    <listBibl type="url">
        <bibl><ref target="https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_106">https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_106</ref></bibl>
    </listBibl>
</additional>
```

Wenn ein Textträger verloren ist, erhält er keine [`<physDesc>`](physDesc.de.md). 
Stattdessen erfassen wir die Informationen zum Verlust des Textzeugen in
[`<adminInfo>`](adminInfo.de.md), für nähere Angaben, s. dort.

## 7. Mehrfachüberlieferung

### 7.1 Darstellung der Überlieferungssituation

Sind mehrere Textzeugen für ein Dokument erhalten, d. h. liegt Mehrfachüberlieferung vor,
dann erhält jeder Textzeuge, wie oben beschrieben, innerhalb von
[`<listWit>`](listWit.de.md) ein [`<witness>`](witness.de.md)-Element,
innerhalb dessen jeweils eine vollständige Textzeugenbeschreibung vorgenommen wird.

Alle Textzeugen werden mit dem Attribut `@n` klassifiziert. 
Hierzu gelten folgende Regeln:

- ein Original wird mit `n="A"` bezeichnet. Existieren mehrere Originale, werden diese
  zusätzlich nummeriert `n="A1"`, `n="A2"` usw.
- eine Abschrift wird mit `n="B"` bezeichnet. Existieren mehrere Abschriften, werden diese
  zusätzlich chronologisch nummeriert mit `n="B1"`, `n="B2"` usw.
- Abschrift von Abschriften werden analog mit `C` und entsprechender chronologisch
  Zählung dargestellt usw.

### 7.2 Wahl der Editionsgrundlage

Die Wahl der Editionsvorlage muss in einem Kommentar begründet werden. 

Der erste aufgeführte Textzeuge stellt die Grundlage für den edierten Text dar,
alle weiteren Textzeugen können für die Angabe von Varianten herangezogen werden.

Bevorzugt sollte ein Orignal zur Textgrundlage gemacht werden und nicht eine Abschrift.

Bei mehreren vorhandenen Originalen sollten, wenn möglich, die Kriterien, die zur Wahl der 
Editionsvorlage beitrugen, in einem Kommentar dargelegt werden. 

Wenn ein Original fehlt, muss die beste Abschrift als Editionsvorlage genommen werden.
In diesem Fall ist die aufwendige Suche nach der originalgetreusten Abschrift unumgänglich. 
Die verschiedenen Abschriften müssen miteinander verglichen werden.

### 7.3 Auswertung der Überlieferung

Wie weit geht man bei der Auswertung von Abschriften und Abschriften von Abschriften?
Werden z. B. viel spätere bzw. neuzeitliche Abschriften stillschweigend weggelassen? 

Gewisse Stücke wurden dutzendfach abgeschrieben, z. B. die Urkunden, die in die Fischereinung
eingetragen und mit dieser immer wieder kopiert wurden. Das Verzeichnen solcher 
«Tertiärüberlieferungen» ist äusserst zeitaufwändig.

In der Regel sollen, wenn ein Original vorhanden ist, vor allem zeitgenössische Abschriften
verzeichnet werden. Es ist unmöglich und auch nicht sinnvoll, alle Abschriften einer wichtigen
Urkunde ausfindig zu machen und zu verzeichnen. Die Faustregel, `Abschriften bis ca. 100 Jahre
nach dem Original`, kann befolgt werden.

Je nach Wichtigkeit eines Stücks muss die Wirkungsgeschichte in einem Kommentar beschrieben werden.

### 7.4 Abweichungen der Abschriften vom Original

Wann müssen Abweichungen der Abschriften vom Original deklariert werden und wann werden sie
stillschweigend ignoriert?

Im Archivinformationssystem werden Abschriften unabhängig vom Vorhandensein von Textvarianten
einfach als «Abschrift» erfasst. Es ist zu aufwendig, diese mit «fehlerhaft» oder 
«mit Textvariante» zu beschreiben.

Enthält ein Original Textstellen, die unverständlich oder nicht mehr lesbar sind, ist es sinnvoll,
spätere Abschriften herbeizuziehen und diese in Form von Apparateinträgen 
(vgl. [`<app>`](app.de.md)) in der Transkription zu erfassen. 
Eventuell helfen sie, die Stelle zu verstehen.

Beispiele:

    Die Erneuerung einer Fischereinung von 1574 hat zwar ein paar Absätze aus der alten Einung von
    1428/1519 übernommen, allerdings in anderer Reihenfolge und durchschossen mit vielen weiteren
    Regelungen. In solchen Fällen wird die Erneuerung am Besten als eigenes Stück transkribiert.

    Eine Abschrift enthält einzelne Streichungen, Hinzufügungen oder andere Abweichungen
    gegenüber dem Original. Das Original wird Grundlage für den edierten Text und 
    inhaltlich interessante Abweichungen werden in Apparateinträgen erfasst.