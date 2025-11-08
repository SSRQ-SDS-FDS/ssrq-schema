---
title: Directives de catalogage
---

Dans le cadre de l’exploitation des sources archivistiques pour les SDS,
les métadonnées décrites ci-dessous sont enregistrées dans la section
[`<sourceDesc>`](sourceDesc.fr.md) et, à l’intérieur, dans [`<msDesc>`](msDesc.fr.md).

En cas de tradition multiple, un
[`<listWit>`](listWit.fr.md) est créé dans [`<sourceDesc>`](sourceDesc.fr.md),
chaque témoin textuel y recevant un
[`<witness>`](witness.fr.md) avec sa propre [`<msDesc>`](msDesc.fr.md).


La description des témoins textuels ([`<msDesc>`](msDesc.fr.md)) est subdivisée
en six grandes sections :

- [Identification du témoin textuel](#1-identifizierung-des-textzeugen-in-msidentifier)
  dans [`<msIdentifier>`](msIdentifier.fr.md)
- [Titre ou nom du témoin textuel](#2-titel-bzw-name-des-textzeugen-in-head)
  dans [`<head>`](head.fr.md)
- [Contenu du témoin textuel](#3-inhalt-des-textzeugen-in-mscontents)
  dans [`<msContents>`](msContents.fr.md)
- [Description physique du témoin textuel](#4-physische-beschreibung-des-textzeugen-in-physdesc)
  dans [`<physDesc>`](physDesc.fr.md)
- [Histoire du témoin textuel](#5-geschichte-des-textzeugen-in-history)
  dans [`<history>`](history.fr.md)
- [Informations supplémentaires sur le témoin textuel](#6-zusätzliche-angaben-zum-textzeugen-in-additional)
  dans [`<additional>`](additional.fr.md)

De plus, en cas de [tradition multiple](#7-mehrfachüberlieferung), il faut décider 
quels témoins textuels doivent être enregistrés, quel témoin constitue la base
textuelle et comment traiter les variantes.


## 1. Identification du témoin textuel dans [`<msIdentifier>`](msIdentifier.fr.md)

### 1.1 Règles générales
La section [`<msIdentifier>`](msIdentifier.fr.md) contient les métadonnées concernant l’institution,  
par exemple un archive ou une bibliothèque, où se trouve le témoin textuel,  
ainsi que les informations permettant d’identifier ce témoin.

Sont enregistrés :

- le lieu où se trouve l’institution de conservation : [`<settlement>`](settlement.fr.md)
- le nom complet de l’institution : [`<repository>`](repository.fr.md)
- la cote attribuée par l’institution de conservation : [`<idno>`](idno.fr.md)
- (optionnel) anciennes ou autres cotes : [`<altIdentifier>`](altIdentifier.fr.md)


Exemples :
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

Dans une unité d’édition bilingue, p. ex. provenant de Fribourg, 
le lieu et le nom de l’institution de conservation ainsi que la cote du témoin textuel 
peuvent être indiqués en allemand et en français, en utilisant à chaque fois l’attribut `@xml:lang`.

Exemple :
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

### 1.2 Règles pour les cotes dans [`<idno>`](idno.fr.md)

#### 1.2.1 Structure de l’idno

La cote se compose au minimum d’un sigle de l’institution de conservation
et de la cote attribuée par cette institution.
Aucune virgule ne sépare le sigle de la cote.

Exemple :
```xml
<idno xml:lang="fr">ACV Ac 29</idno>
```

et pas :
```xml
<idno xml:lang="fr">ACV, Ac 29</idno>
```

#### 1.2.2 Numéros de distinction

Lorsque plusieurs témoins textuels sont enregistrés et numérotés sous 
une même cote dans une institution, la cote reçoit, après une virgule, un numéro de distinction.

Exemples :
```xml
<idno xml:lang="de">StAZH C III 22, Nr. 397</idno>
<idno xml:lang="de">StAZH A 6.1, Nr. 3</idno>
```

#### 1.2.3 Section d’un témoin textuel paginé

Lorsque seule une section d’un témoin textuel paginé est éditée,
la cote reçoit l’indication de localisation correspondante.
Les numéros de page exacts sont indiqués,
sans utiliser `f.` ou `ff.` (pages suivantes).
La pagination est indiquée par `S.` (allemand) ou `p.` (français).

Exemples :
```xml
<idno xml:lang="de">STAW AG 91/1/42.6, S. 3-7</idno>
<idno xml:lang="fr">AVN B 101.01.01.004, p. 333</idno>
```

#### 1.2.4 Section d’un témoin textuel folié

Lorsque seule une section d’un témoin textuel folié est éditée,
la cote reçoit le numéro de la feuille correspondant.
Le recto de la feuille est indiqué par `r` et le verso par `v`.
La foliation est indiquée par `fol.` (allemand et français).

Exemples :
```xml
<idno xml:lang="de">StAZH B I 273, fol. 881r–884v</idno>
<idno xml:lang="fr">AVN B 101.14.001, fol. 531r-v</idno>
```

#### 1.2.5 Section d’un témoin textuel à plusieurs parties

Si un témoin textuel comprend plusieurs numérotations de feuilles ou de pages,
parce que, par exemple, des cahiers initialement séparés ont été reliés en un volume,
le numéro de la feuille est précédé de l’indication du cahier ou de la partie correspondante.

Exemples :
```xml
<idno xml:lang="de">StAZH B II 4, Teil I, fol. 15v</idno>
<idno xml:lang="de">StAZH F II a 290, Teil III, fol. 3r–v</idno>
```

#### 1.2.6 Entrées

Dans les procès-verbaux des conseils et tribunaux, les livres de ville, les registres 
d’actes et de notariat, les livres de messes anniversaires, etc., il peut y avoir plusieurs
entrées par page ou par feuille.  
Après l’indication de la page ou de la feuille, le numéro de l’entrée est ajouté à la cote.  
Le comptage se fait de haut en bas.  
Si une entrée commence au début d’une page, mais a déjà commencé sur la page précédente, 
elle n’est pas comptée.

Exemples :
```xml
<idno xml:lang="de">StAZH B III 4, fol. 21v, Eintrag 1</idno>
<idno xml:lang="de">StAGR AB IV 01/007.65, S. 536, Eintrag 2</idno>
```

#### 1.2.7 Suppléments

Si ce n’est pas le témoin textuel enregistré sous une cote qui est édité,  
mais un supplément ou une section d’un supplément, la cote est complétée par la mention `Supplément`.  
S’il y a plusieurs suppléments, ceux-ci sont numérotés.  
Si seule une partie d’un supplément est éditée, cela est indiqué par la pagination correspondante.

Exemple :
```xml
<idno xml:lang="de">StAZH C I, Nr. 249, Beilage</idno>
<idno xml:lang="de">StAZH C I, Nr. 3165, Beilage 17</idno>
<idno xml:lang="de">StAZH C I, Nr. 3165, Beilage 2, S. 3-4</idno>
```

### 1.3 Cotes alternatives ou anciennes

Si un témoin textuel a été enregistré auparavant sous une autre cote  
ou est connu dans la littérature scientifique sous un autre nom,  
cette désignation alternative peut être indiquée avec [`<altIdentifier>`](altIdentifier.fr.md).  
C’est par exemple fréquent dans le StASH.  
Les cotes antérieures y sont enregistrées pour documenter l’ancienne organisation des archives  
et pour établir une concordance entre des sources fréquemment citées.

Exemples :
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

## 2. Titre ou nom du témoin textuel dans [`<head>`](head.fr.md)

Un résumé court et précis du contenu du témoin textuel édité est enregistré dans 
[`<head>`](head.fr.md).  
Si un document possède plusieurs témoins textuels, un titre ne doit être enregistré 
que pour le témoin servant de base au texte édité.

Exemples :
```xml
<head>Verordnung über die Dienstpflicht in Winterthur</head>
<head>Eid von Gesellen und anderen Angestellten</head>
<head>Sentence et remise au bras séculier de Pierre de la Prélaz</head>
<head>Loi des Trois-États sur les dommages causés aux bois et leur réparation</head>
```

Dans les unités d’édition bilingues, par exemple à Fribourg,  
un titre en allemand ainsi qu’un titre en français peuvent être enregistrés.  
Dans ce cas, l’attribut `@xml:lang` doit être utilisé pour indiquer la langue.

Exemples :
```xml
<head xml:lang="de">Françoise Dévaud-Clerc – Urteil</head>
<head xml:lang="fr">Françoise Dévaud-Clerc – Jugement</head>

<head xml:lang="de">Eid des städtischen Steinhauers, Zimmermeisters, Dachdeckers und Wagners</head>
<head xml:lang="fr">Serment des tailleur de pierre, maître charpentier, couvreur et charron de la ville</head>
```

## 3. Contenu du témoin textuel dans [`<msContents>`](msContents.fr.md)

### 3.1 Règles générales

La section [`<msContents>`](msContents.fr.md) contient des informations 
sur le contenu du témoin textuel.

Sont enregistrés :

- un résumé : [`<summary>`](summary.fr.md)
- la langue du texte : [`<textLang>`](textLang.fr.md)
- (optionnel pour les manuscrits) le scribe du texte : [`<author>`](author.fr.md)
- (pour les imprimés) l’indication d’édition : [`<docImprint>`](docImprint.fr.md)

Les informations sur la langue, le scribe et l’indication d’édition 
sont regroupées dans [`<msItem>`](msItem.fr.md).

Exemples :
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

Dans les unités d’édition bilingues, par exemple à Fribourg,  
il peut exister un résumé analytique distinct pour chaque langue de l’unité d’édition.  
Dans ce cas, les résumés sont différenciés à l’aide de l’attribut `@xml:lang`.

Exemple :
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

### 3.2 Résumé

#### 3.2.1 Définition et but

En principe, un résumé doit être établi pour chaque document, même pour les courts.

Un résumé est une synthèse du contenu du texte édité, en omettant les formules.  
Pour les textes en latin, un résumé plus détaillé est recommandé.  
Si de nombreux points sont réglementés, ceux-ci peuvent être regroupés sous des thèmes principaux  
(par exemple « Sont réglés … »).

#### 3.2.2 Langue et structure

Le résumé est rédigé dans une langue moderne avec des formulations aussi uniformes que possible,  
sans utiliser de termes provenant des sources.  

La structuration d’un long résumé se fait selon les aspects de contenu, 
en paragraphes ([`<p>`](p.fr.md)).

#### 3.2.3 Sceaux et copies multiples

Les sceaux existants sont mentionnés à la fin du résumé, séparés par des paragraphes.  
Les annonces de sceaux, y compris celles de sceaux ou empreintes manquants, sont également signalées.

Exemples :
```xml
<summary xml:lang="de">
    <p><!--Ici se trouve le résumé réel-->…</p>
    <p>Johann Ulrich Escher, Landvogt von Sax-Forstegg, siegelt.</p>
</summary>

<summary xml:lang="de">
    <p><!--Ici se trouve le résumé réel-->…</p>
    <p>Der Aussteller siegelt.</p>
    <p>Für Wartau-Gretschins siegeln Wilhelm vom Fröwis, Oswald von Prad und Rudolf Kalberer.</p>
    <p>Für Sevelen, Hans Vittler und Hans Spangolf siegelt Klaus Vittler.</p>
</summary>
```

Si un acte mentionne que plusieurs exemplaires de l’acte ont été rédigés et découpés,  
cela doit être indiqué à la fin du résumé, conjointement avec les sceaux.

#### 3.2.4 Noms de personnes

Les noms sont en principe normalisés dans le résumé.  
Les personnes figurant dans le [DHS](https://hls-dhs-dss.ch/) 
ou le [GND](https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd_node.html)  
sont normalisées conformément à ces ouvrages de référence.  
S’il s’agit d’un nom de famille connu, il est normalisé selon le 
[Répertoire des noms de famille suisses](https://hls-dhs-dss.ch/famn/).  
Si les personnes ne sont pas répertoriées dans le HLS ou le GND, les prénoms et noms de famille  
sont normalisés selon l’orthographe la plus fréquente dans le document, en conservant 
les caractères spéciaux (p. ex. Ruedi, Kuoni).

#### 3.2.5 Autres normalisations

Les titres ainsi que les désignations professionnelles ou officielles doivent être traités 
de manière cohérente dans le résumé et dans les commentaires.

Pour les mesures, poids et monnaies, on utilise les chiffres arabes.  
Dans tous les autres cas, les nombres de un à douze sont écrits en toutes lettres selon le Duden,  
et pour les instances, le nombre est systématiquement écrit en toutes lettres.

Pour `Notariatssignet`, `Notariatszeichen` ou `Notariatsinstrument`, on utilise le terme 
[Signe](https://termini.ssrq-sds-fds.ch/views/view-keyword.xq?id=key004763).  
Cette forme d’authentification est mentionnée dans le résumé pour les instruments notariaux 
(de manière analogue aux actes scellés).

Exemples :
```xml
<p>Le notaire authentifie l’instrument avec son signe.</p>
<p>Le notaire authentifie l’instrument avec son signe en présence de témoins.</p>
```

#### 3.2.6 Ce qui n’est pas inclus dans le résumé

Si l’acte est un chirographe, cela n’est pas indiqué dans le résumé, mais dans 
[`<bindingDesc>`](bindingDesc.fr.md) (voir ci-dessous).

Les contenus importants peuvent être approfondis dans le commentaire ([`<back>`](back.fr.md)),  
le résumé se limitant à une synthèse concise.

Les scribes des mentions ([`<ab>`](ab.fr.md)), par exemple dans un acte pontifical,  
sont signalés dans le texte avec [`<persName>`](persName.fr.md) et ne sont pas mentionnés 
spécifiquement dans le résumé.

### 3.3 La langue du texte

La langue utilisée dans le texte source est indiquée avec [`<textLang>`](textLang.fr.md).  
En cas de plusieurs langues, l’élément est répété dans l’ordre de fréquence d’apparition.

### 3.4 Le scribe du texte

Pour les manuscrits, un scribe peut, s’il est connu, être indiqué avec [`<author>`](author.fr.md) 
et, à l’intérieur, avec [`<persName>`](persName.fr.md). Si le scribe n’est pas connu, 
mais seulement l’atelier, celui-ci est enregistré en texte libre à l’intérieur de 
[`<author>`](author.fr.md).

Exemples :
```xml
<author role="scribe">
    <persName ref="per027325">Georg Bappus</persName>
</author>

<author role="scribe">
  <persName ref="per028066">Hans Jakob Beyel</persName>, Rechenschreiber von Zürich
</author>

<author role="scribe">Schreiber der Kanzlei Liechtenstein</author>
```

Si plusieurs mains sont reconnaissables dans un manuscrit, une description des mains est créée 
dans [`<handDesc>`](handDesc.fr.md) (voir ci-dessous). Celle-ci ne fait plus partie de 
[`<msContents>`](msContents.fr.md), mais de la description physique du témoin textuel.

### 3.5 L’indication d’édition

Pour les imprimés, les noms de l’imprimerie ou de l’imprimeur ([`<publisher>`](publisher.fr.md))  
ainsi que le lieu d’impression ([`<pubPlace>`](pubPlace.fr.md))  
sont enregistrés dans [`<docImprint>`](docImprint.fr.md).

Exemple :
```xml
<docImprint>
    <pubPlace ref="loc000065" cert="high">Zürich</pubPlace>
    <publisher cert="high">Christoph Froschauer der Ältere</publisher>
</docImprint>
```

## 4. Description physique du témoin textuel dans [`<physDesc>`](physDesc.fr.md)

### 4.1 Règles générales

La section [`<physDesc>`](physDesc.fr.md) décrit le témoin textuel en termes 
de caractéristiques physiques.  
Elle est subdivisée en quatre sous-sections :

- description du témoin textuel en tant qu’objet physique dans [`<objectDesc>`](objectDesc.fr.md)
- description de la reliure (et de la transmission) dans [`<bindingDesc>`](bindingDesc.fr.md)
- description des mains dans [`<handDesc>`](handDesc.fr.md)
- description des sceaux dans [`<sealDesc>`](sealDesc.fr.md)

### 4.2 Description du témoin textuel en tant qu’objet physique dans [`<objectDesc>`](objectDesc.fr.md)

La section [`<objectDesc>`](objectDesc.fr.md) contient, à l’intérieur de 
[`<supportDesc>`](supportDesc.fr.md), des informations sur le matériau, les dimensions, 
la pagination et l’état de conservation du témoin textuel.

Sont enregistrés :

- le matériau, c’est-à-dire le support : [`<support>`](support.fr.md) avec [`<material>`](material.fr.md)
- la hauteur et la largeur des feuilles (ou du livre ou de la plica) : [`<extent>`](extent.fr.md) avec
  [`<dimensions>`](dimensions.fr.md) et [`<height>`](height.fr.md) ou [`<width>`](width.fr.md)
- (optionnel) l’état de conservation du support et ses détériorations : [`<condition>`](condition.fr.md)
- (optionnel) le décompte des feuilles de l’original et, le cas échéant, 
  des décomptes propres différents : [`<foliation>`](foliation.fr.md)

Exemple :
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

### 4.3 Description de la reliure (et de la transmission) dans [`<bindingDesc>`](bindingDesc.fr.md)

La section [`<bindingDesc>`](bindingDesc.fr.md) contient d’abord des informations sur la reliure.

De plus, la forme de transmission est actuellement indiquée en texte libre.  
Le type de transmission (p. ex., original), la forme (p. ex., cahier) et l’étendue 
(p. ex., 10 feuilles) sont décrits dans l’ordre mentionné.

Exemples de type et de forme :

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

### 4.4 Description des mains dans [`<handDesc>`](handDesc.fr.md)

Sont enregistrées :

- les mains des scribes, lorsqu’il y a plus d’un scribe principal du texte
- les autres mains importantes, c’est-à-dire celles pertinentes pour la critique textuelle

Si plusieurs mains de scribes sont reconnaissables dans un manuscrit, 
une [`<handDesc>`](handDesc.fr.md) doit être créée,  
dans laquelle chaque main est décrite plus en détail à l’aide d’une [`<handNote>`](handNote.fr.md)  
(voir cette section et la section [Scribes et mains](scribes-and-hands.fr.md))  
dans les directives de transcription.

### 4.5 Description des sceaux dans [`<sealDesc>`](sealDesc.fr.md)

La description des sceaux se fait de gauche à droite dans [`<sealDesc>`](sealDesc.fr.md),  
chaque sceau recevant son propre élément ([`<seal>`](seal.fr.md)).

Les signataires ou les annonces de sceaux sont également enregistrés dans le résumé.  
Dans le commentaire, les divergences entre l’annonce du sceau et la scellure doivent être décrites.  
Cela vaut également pour les copies.

Le point de référence est l’annonce du sceau dans l’acte ou, pour une formulation 
à la première personne, la mention de l’émetteur.

Si les signataires sont nommément indiqués sur la plica ou les bandes de parchemin,  
les noms sont transcrits dans [`<ab>`](ab.fr.md), sinon des informations importantes  
(par exemple, l’orthographe originale des signataires) seraient perdues.

Si la fente du sceau est présente, cela est mentionné en conséquence.  
Le signataire n’est enregistré que si l’on est certain du sceau manquant.

## 5. Histoire du témoin textuel dans [`<history>`](history.fr.md)

La section [`<history>`](history.fr.md) contient, dans [`<origin>`](origin.fr.md),  
les informations sur la datation et la localisation d’un témoin textuel.

Sont enregistrés :

- la date de création du témoin textuel : [`<origDate>`](origDate.fr.md) avec `type="document"`
- (optionnel) s’il s’agit d’une copie, en plus, la date de création de l’original présumé : 
  [`<origDate>`](origDate.fr.md) avec `type="content"`
- le lieu de création du support : [`<origPlace>`](origPlace.fr.md) avec `type="document"`
- (optionnel) s’il s’agit d’une copie, en plus, le lieu de création de l’original présumé : 
  [`<origPlace>`](origPlace.fr.md) avec `type="content"`
- (optionnel) l’institution émettrice : [`<orgName>`](orgName.fr.md)


Exemples :
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

Pour les rapports sur un événement, la date de l’événement rapporté est enregistrée avec  
```<origDate type="content"``` et le moment où le rapport a été rédigé avec  
```<origDate type="document"```.  
Par exemple : Renward Cysat rédige vers 1600 un rapport sur le commerce d’Amstalden de 1478,  
cela est codé comme suit.  
Pour les règles de datation elles-mêmes, voir les [directives de datation](dating_guidelines.fr.md).

Exemple :
```xml
<origin>
    <origDate type="content" from-custom="1478-01-01" to-custom="1478-12-31" calendar="julian"/>
    <origDate type="document" from-custom="1590-01-01" to-custom="1610-12-31" calendar="gregorian"/>
</origin>
```

Les remarques détaillées sur la datation d’un document non daté sont enregistrées 
dans un commentaire ([`<back>`](back.fr.md)).

Le lieu de création d’un témoin textuel ([`<origPlace>`](origPlace.fr.md)) 
n’est enregistré que s’il figure dans le document  
ou s’il peut être établi de manière certaine, par exemple pour les procès-verbaux du conseil.

Les lieux d’émission, d’expédition ainsi que les lieux de promulgation sont normalisés.  
En cas de plusieurs lieux d’émission, chacun reçoit son propre élément 
([`<origPlace>`](origPlace.fr.md)).

Exemple :
```xml
<origin>
    <origDate type="document" from-custom="1448-03-17" to-custom="1448-03-23" calendar="julian"/>
    <origPlace type="document" ref="loc008831.01">Hôpital Marie-Madeleine du Mont-Joux</origPlace>
    <origPlace type="document" ref="loc008768.01">Château de La Tour-de-Peilz</origPlace>
</origin>
```

## 6. Informations supplémentaires sur le témoin textuel dans [`<additional>`](additional.fr.md)

Les publications, telles que les éditions de sources, les ouvrages de résumés, les inventaires, 
la littérature secondaire, etc.,  
sont enregistrées avec le titre abrégé dans [`<listBibl>`](listBibl.fr.md) et intégralement dans  
[Zotero](https://www.zotero.org/groups/5048222/ssrq/library).  
Les publications sont listées avec des étiquettes dans `@type` et le titre abrégé, 
par ordre chronologique décroissant.

Exemple :
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

Si un support textuel est perdu, il ne reçoit pas de [`<physDesc>`](physDesc.fr.md).  
À la place, les informations relatives à la perte du témoin textuel sont enregistrées dans  
[`<adminInfo>`](adminInfo.fr.md) ; pour plus de détails, voir cette section.

## 7. Transmission multiple

### 7.1 Présentation de la situation de transmission

Si plusieurs témoins textuels sont conservés pour un document, c’est-à-dire 
en cas de transmission multiple, chaque témoin reçoit, comme décrit ci-dessus, au sein de 
[`<listWit>`](listWit.fr.md) un élément [`<witness>`](witness.fr.md),  
dans lequel une description complète du témoin textuel est effectuée.

Tous les témoins textuels sont classés à l’aide de l’attribut `@n`.  
Les règles suivantes s’appliquent :

- un original est désigné par `n="A"`. S’il existe plusieurs originaux, ceux-ci 
  sont en plus numérotés `n="A1"`, `n="A2"`, etc.
- une copie est désignée par `n="B"`. S’il existe plusieurs copies, 
  elles sont en plus numérotées chronologiquement `n="B1"`, `n="B2"`, etc.
- les copies de copies sont indiquées de manière analogue avec `C` 
  et un décompte chronologique correspondant, etc.

### 7.2 Choix du texte de base pour l’édition

Le choix du texte de base pour l’édition doit être justifié dans un commentaire.

Le premier témoin textuel mentionné constitue la base du texte édité,  
tous les autres témoins peuvent être utilisés pour l’indication de variantes.

Il est préférable de prendre un original comme texte de base plutôt qu’une copie.

S’il existe plusieurs originaux, les critères ayant conduit au choix du texte de base  
doivent, si possible, être exposés dans un commentaire.

Si un original fait défaut, la meilleure copie doit être prise comme texte de base pour l’édition.  
Dans ce cas, la recherche approfondie de la copie la plus proche de l’original est indispensable.  
Les différentes copies doivent être comparées entre elles.

### 7.3 Évaluation de la transmission

Jusqu’où doit-on aller dans l’évaluation des copies et des copies de copies ?  
Par exemple, les copies beaucoup plus tardives ou modernes sont-elles tacitement omises ?

Certaines pièces ont été copiées des dizaines de fois, par exemple les actes enregistrés dans 
la guilde de pêche et régulièrement recopiés avec celle-ci. L’enregistrement de ces 
« transmissions tertiaires » est extrêmement chronophage.

En règle générale, si un original est disponible, seules les copies contemporaines doivent 
surtout être enregistrées. Il est impossible et non pertinent de retrouver et d’enregistrer 
toutes les copies d’un acte important. La règle pratique « copies jusqu’à environ 100 ans après 
l’original » peut être suivie.

Selon l’importance d’une pièce, l’histoire de sa réception doit être décrite dans un commentaire.

### 7.4 Déviations des copies par rapport à l’original

Quand les déviations des copies par rapport à l’original doivent-elles être signalées, 
et quand sont-elles tacitement ignorées ?

Dans le système d’information archivistique, les copies sont simplement enregistrées comme « copie »,  
indépendamment de l’existence de variantes textuelles.  
Il serait trop fastidieux de les qualifier de « fautives » ou « avec variante de texte ».

Si un original contient des passages incompréhensibles ou illisibles, il est utile de consulter 
les copies ultérieures et de les enregistrer sous forme d’entrées d’apparat 
(voir [`<app>`](app.fr.md)) dans la transcription. Elles peuvent éventuellement 
aider à comprendre le passage.

Exemples :

    Le renouvellement d’une guilde de pêche de 1574 a repris quelques paragraphes 
    de l’ancienne guilde de 1428/1519, mais dans un ordre différent et mêlés à de 
    nombreuses autres dispositions.  
    Dans de tels cas, le renouvellement est mieux transcrit comme une pièce distincte.

    Une copie contient des ratures, ajouts ou autres écarts par rapport à l’original.  
    L’original constitue la base du texte édité, et les déviations intéressantes sur 
    le plan du contenu sont enregistrées dans les entrées d’apparat.
