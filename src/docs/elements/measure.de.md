---
title: measure
---



# `<measure/>`

## Beschreibung

Enthält eine Massangabe jeder Art.

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @commodity



*Mögliche Werte*

- apple – *Äpfel*
- barley – *Gerste*
- bean – *Bohnen*
- bran – *Kleie*
- bread – *Brot*
- butter – *Butter*
- cheese – *Käse*
- coal – *Kohle*
- denim – *Zwillich*
- drapery – *Tuch*
- dried fruit – *Dörrobst*
- dung – *Mist*
- electuary – *Latwerge*
- field – *Acker*
- fish – *Fisch*
- flax – *Flachs*
- flour – *Mehl*
- forest – *Wald*
- gold – *Gold*
- grain – *Korn*
- grain_spelt – *Fesen und Kernen*
- grain_wheat – *Korn und Weizen*
- grassland – *Wiese*
- hay – *Heu*
- hemp – *Hanf*
- herring – *Hering*
- honey – *Honig*
- land – *Land*
- lard – *Schmalz*
- lead – *Blei*
- lentils – *Linsen*
- lime – *Kalk*
- marsh – *Ried*
- meat – *Fleisch*
- merchandise – *Kaufmannsgut*
- milk – *Milch*
- millet – *Hirse*
- mush – *Mus*
- mushflour – *Musmehl*
- must – *Most*
- nuts – *Nüsse*
- oat – *Hafer*
- pea – *Erbsen*
- pear – *Birnen*
- picket – *Stickel*
- potatoes – *Kartoffeln*
- pulses – *Hülsenfrüchte*
- rice – *Reis*
- rye – *Roggen*
- salt – *Salz*
- silk – *Seide*
- silver – *Silber*
- spelt – *Dinkel*
- steel – *Stahl*
- straw – *Stroh*
- tallow – *Unschlitt*
- tin – *Zinn*
- vegetables – *Gemüse*
- vineyard – *Reben*
- wax – *Wachs*
- wheat – *Weizen*
- wine – *Wein*
- wood – *Holz*
- wool – *Wolle*
- ziger – *Ziger*

### @origin



*Mögliche Werte*

- BE – *Berner*
- Breisgau – *Breisgauer*
- Chur – *Churer*
- Diessenhofen – *Diessenhofer*
- Elsass – *Elsässer*
- Etsch – *Etsch*
- Feldkirch – *Feldkircher*
- Florenz – *Florentiner*
- FR – *französisch/e*
- GE – *Genfer*
- HU – *Ungarischer*
- Konstanz – *Konstanzer*
- Lausanne – *Lausanner*
- Lothringen – *lothringische*
- LU – *Luzerner*
- Montfort – *Montforter*
- NE – *Neuenburger*
- Österreich – *Österreicher*
- Rh – *Rheinischer*
- Rheintaler – *Rheintaler*
- Sargans – *Sarganser*
- Savoie – *Savoyer*
- SG – *St. Galler*
- SH – *Schaffhauser*
- Stein – *Steiner*
- SZ – *Schwyzer*
- Utrecht – *utrischer*
- Werdenberg – *Werdenberger*
- Winterthur – *Winterthurer*
- ZH – *Zürcher*

### @quantity

Gibt bei Abmessungen die Ausdehnung an.

*Mögliche Werte*

- Gleitkommazahl
- Zeichenkette – Einschränkung: regulärer Ausdruck `(\-?[\d]+/\-?[\d]+)`
- Gleitkommazahl

### @type



*Mögliche Werte*

- age – *Alter*
- area – *Flächenmass*
- currency – *Währung*
- length – *Längenmass*
- text_scope – *Textumfang*
- undefined – *Ungefähres Mass/Gewicht*
- volume – *Volumenmass*
- weight – *Gewicht*

### @unit

Masseinheit oder Währung

*Mögliche Werte*

- fauchée – *fauchée (Mahd)*
- Gertel – *Gertel*
- Hube – *Hube*
- Juchart – *Juchart*
- Kammer – *Kammer*
- Kuhsömmerung – *Kuhsömmerung*
- Kuhwinterung – *Kuhwinterung*
- Mal – *Mal*
- Mannmad – *Mannmad*
- Mannwerk – *Mannwerk*
- Mitmal – *Mitmal*
- Rute – *Rute*
- Schuppose – *Schuppose*
- Staffel – *Staffel*
- Tagwen – *Tagwen*
- Becher – *Becher*
- Brenten – *Brente*
- Eimer – *Eimer*
- Fass – *Fass*
- Garbe – *Garbe*
- Immi – *Immi*
- Kanne – *Kanne*
- Kopf – *Kopf*
- Kratten – *Kratten*
- Kröttli – *Kröttli*
- Ledi – *Ledi*
- Legel – *Legel*
- Linie – *Linie*
- Mass – *Mass*
- Mäss – *Mäss*
- Mässli – *Mässli*
- Malter – *Malter*
- Mütt – *Mütt*
- Quart – *Quart*
- Quartane – *Quartane*
- Röhrchen – *Röhrchen*
- Sack – *Sack*
- Saum – *Saum*
- Schaffen – *Schaffen*
- Scheffel – *Scheffel*
- Scheibe – *Scheibe*
- Sechzehner – *Sechzehner*
- Sester – *Sester*
- Ster – *Ster*
- Tonne – *Tonne*
- Trinken – *Trinken*
- Vierdung – *Vierdung*
- Viertel – *Viertel*
- Zuber – *Zuber*
- Angster – *Angster*
- Böhmischer_Groschen – *Böhmischer Groschen*
- bz – *Batzen*
- d – *Pfennig*
- Dicken – *Dicken*
- Doubloon – *Dublone*
- ducatoon – *Dukaton*
- Dukat – *Dukat*
- écu – *écu*
- écu_blanc – *écu blanc*
- écu_dor – *écu d’or*
- écu_petit – *écu petit*
- Engrogne – *Engrogne*
- fl – *Gulden*
- franc – *Franken*
- Gros – *Groschen*
- Grossi – *Grosso*
- h – *Haller*
- Halbgulden – *Halbgulden*
- Halbtaler – *Halbtaler*
- k – *Krone*
- Kronentaler – *Kronentaler*
- L – *Schweizer Franken*
- lb – *Pfund*
- liard – *liard*
- livre_faible – *livre faible*
- Louis_dor – *Louis d’or*
- Louistaler – *Louistaler*
- M – *Mark*
- Mirliton – *Lous d’or Mirliton*
- Ort – *Ort*
- Pistole – *Pistole*
- plp – *Plappart*
- S – *Sol*
- sol_faible – *sol faible*
- Sonnendublone – *Sonnendublone*
- Spagürli – *Spagürli*
- ß – *Schilling*
- Taler – *Taler*
- teston – *Testone*
- Vierer – *Vierer*
- xr – *Kreuzer*
- zecchino – *Zechine*
- cm – *cm*
- Klafter – *Klafter*
- Daumen – *Daumen*
- Elle – *Elle*
- Finger – *Finger*
- Fuss – *Fuss*
- Meile – *Meile*
- Schritt – *Schritt*
- Schuh – *Schuh*
- Stab – *Stab*
- Zoll – *Zoll*
- Ballen – *Ballen*
- Bürde – *Bürde*
- carriage – *Wagen*
- Dutzend – *Dutzend*
- Fuder – *Fuder*
- Gaden – *Gaden*
- Kloben – *Kloben*
- Laib – *Laib*
- Loden – *Loden*
- Maschen – *Maschen*
- Paar – *Paar*
- Riste – *Riste*
- Schoch – *Schoch*
- Schubkarre – *Schubkarre*
- Seil – *Seil*
- Sester – *Sester*
- Stock – *Stock*
- Stuck – *Stuck*
- Zeine – *Zeine*
- Biner – *Biner*
- denier – *Denier (Skrupel)*
- Gewäg – *Gewäg*
- grain – *Gran*
- Krinne – *Krinne*
- Lot – *Lot*
- Pfund – *Pfund*
- Pfefferpfund – *Pfefferpfund*
- Rupp – *Rupp*
- Quentli – *Quentli*
- Unze – *Unze*
- Zentner – *Zentner*
- Vierling – *Vierling*
- leaf – *Blatt*
- page – *Seite*
- month – *Monat*
- week – *Woche*
- year – *Jahr*

## Beispiele

### Beispiel 1

Währungsbezeichnung:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">umb
            <measure type="currency" origin="ZH" unit="lb" quantity="2">zwai phunt nuwer Zuricher
            </measure>
</egXML>
               
```

### Beispiel 2

Masseinheit:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            ... item oben här
            <measure type="area" unit="Juchart" quantity="8" commodity="field">acht juchart acher</measure>
            aneinanderen, genannt
            ....
        </egXML>
               
```

### Beispiel 3

Masseinheit:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Item <measure type="weight" unit="Zentner" quantity="1" commodity="wool">ein zentner landtwull
        </measure> git <measure type="currency" unit="ß" quantity="2">ij ß</measure>.
        </egXML>
               
```

### Beispiel 4

Altersangabe:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">... wan das jeman unser lannttluͤtten, er
            sye jung oder alltt,
            <measure type="age" unit="year" quantity="14">ob vierzechen jarenn</measure>
            von ainem paner endrunne ...
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.6.3. Numbers and Measures](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONANU)