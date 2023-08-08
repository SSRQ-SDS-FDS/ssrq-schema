---
title: measure
---



# `<measure/>` (mesure)

## Description

Contient une mesure de chaque type.

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

### @commodity

Indique ce qui est mesuré.

*Valeurs possibles*

- apple – *pommes*
- barley – *orge*
- bean – *haricots*
- bran – *son*
- bread – *pain*
- butter – *beurre*
- cheese – *fromage*
- coal – *charbon*
- denim – *coutil*
- drapery – *étoffe*
- dried fruit – *fruit sec*
- dung – *fumier*
- electuary – *électuaire*
- field – *champ*
- fish – *poisson*
- flax – *lin*
- flour – *farine*
- forest – *forêt*
- gold – *or*
- grain – *grain*
- grain_spelt – *grain non-décortiqué et épeautre égrugé*
- grain_wheat – *grain et blé*
- grassland – *pré*
- hay – *foin*
- hemp – *chanvre*
- herring – *hareng*
- honey – *miel*
- land – *pays*
- lard – *saindoux*
- lead – *plomb*
- lentils – *lentilles*
- lime – *chaux*
- marsh – *marais*
- meat – *viande*
- merchandise – *marchandise*
- milk – *lait*
- millet – *millet*
- mush – *purée*
- mushflour – *farine pour la purée*
- must – *cidre*
- nuts – *noix*
- oat – *avoine*
- pea – *pois*
- pear – *poires*
- picket – *échalas*
- potatoes – *pommes de terre*
- pulses – *légumineuses*
- rice – *riz*
- rye – *seigel*
- salt – *sel*
- silk – *soie*
- silver – *argent*
- spelt – *épeautre*
- steel – *acier*
- straw – *paille*
- tallow – *suif*
- tin – *étain*
- vegetables – *légume*
- vineyard – *vigne*
- wax – *cire*
- wheat – *blé (froment)*
- wine – *vin*
- wood – *bois*
- wool – *laine*
- ziger – *ziger*

### @origin



*Valeurs possibles*

- BE – *de Berne*
- Breisgau – *de Brisgau*
- Chur – *de Coire*
- Diessenhofen – *de Diessenhofen*
- Elsass – *de l’Alsace*
- Etsch – *de l’Adige*
- Feldkirch – *de Feldkirch*
- Florenz – *de Florence*
- FR – *français/e*
- GE – *de Genève*
- HU – *de Hongrie*
- Konstanz – *de Constance*
- Lausanne – *Laus.*
- Lothringen – *de la Lorraine*
- LU – *de Lucerne*
- Montfort – *de Montfort*
- NE – *de Neuchâtel*
- Österreich – *d’Autriche*
- Rh – *de la Rhénanie*
- Rheintaler – *de Rheintal*
- Sargans – *de Sargans*
- Savoie – *de la Savoie*
- SG – *de Saint-Gall*
- SH – *de Schaffhouse*
- Stein – *de Stein am Rhein*
- SZ – *de Schwyz*
- Utrecht – *d’Utrecht*
- Werdenberg – *de Werdenberg*
- Winterthur – *de Winterthour*
- ZH – *de Zurich*

### @quantity

Dans le cas des dimensions, spécifie l'expansion. 

*Valeurs possibles*

- Nombre à virgule flottante
- Chaîne de caractères – Restriction: expression régulière `(\-?[\d]+/\-?[\d]+)`
- Nombre à virgule flottante

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- age – *âge*
- area – *mesure de superficie*
- currency – *unité monétaire*
- length – *mesure de longueur*
- text_scope – *Taille du texte*
- undefined – *mesure/poid approximatif*
- volume – *mesure de volume*
- weight – *poid*

### @unit

Unité de mesure ou devise

*Valeurs possibles*

- fauchée – *fauchée*
- Gertel – *gertel*
- Hube – *manse*
- Juchart – *pose*
- Kammer – *kammer*
- Kuhsömmerung – *kuhsömmerung (valeur d’un alpage selon le nombre de vaches qui peuvent y paître en été)*
- Kuhwinterung – *kuhwinterung (valeur d’un alpage selon le nombre de vaches qui peuvent y paître en hiver)*
- Mal – *mal*
- Mannmad – *mad*
- Mannwerk – *seiteur*
- Mitmal – *mal/metmal*
- Rute – *perche*
- Schuppose – *schuppose*
- Staffel – *staffel*
- Tagwen – *tagwen*
- Becher – *pinte*
- Brenten – *brante*
- Eimer – *setier*
- Fass – *tonneau*
- Garbe – *gerbe*
- Immi – *émine*
- Kanne – *kanne (pot)*
- Kopf – *kopf*
- Kratten – *kratten*
- Kröttli – *kröttli*
- Ledi – *ledi*
- Legel – *legel*
- Linie – *ligne*
- Mass – *mass*
- Mäss – *bichet*
- Mässli – *mässli*
- Malter – *malter*
- Mütt – *muid*
- Quart – *quart*
- Quartane – *quartanée*
- Röhrchen – *tube*
- Sack – *sac*
- Saum – *saum*
- Schaffen – *schaffen*
- Scheffel – *boisseau*
- Scheibe – *tranche*
- Sechzehner – *sechzehner*
- Sester – *setier*
- Ster – *staro*
- Tonne – *tonneau*
- Trinken – *trinken*
- Vierdung – *vierdung*
- Viertel – *un quart*
- Zuber – *baquet*
- Angster – *angster*
- Böhmischer_Groschen – *gros bohêmien*
- bz – *batz/bache*
- d – *denier*
- Dicken – *dicken*
- Doubloon – *Doublon*
- ducatoon – *ducaton*
- Dukat – *ducat*
- écu – *écu*
- écu_blanc – *écu blanc*
- écu_dor – *écu d’or*
- écu_petit – *écu petit*
- Engrogne – *Engrogne*
- fl – *florin*
- franc – *franc*
- Gros – *gros*
- Grossi – *grosso*
- h – *maille*
- Halbgulden – *demi-gulden*
- Halbtaler – *halbtaler*
- k – *écu/couronne*
- Kronentaler – *kronentaler*
- L – *livre Suisse*
- lb – *livre*
- liard – *liard*
- livre_faible – *livre faible*
- Louis_dor – *Louis d’or*
- Louistaler – *Louis blanc*
- M – *marc*
- Mirliton – *Lous d’or Mirliton*
- Ort – *un quart d’un florin*
- Pistole – *pistole*
- plp – *plappart*
- S – *sol*
- sol_faible – *sol faible*
- Sonnendublone – *Sonnendublone*
- Spagürli – *spagürli*
- ß – *sou/sol*
- Taler – *thaler*
- teston – *teston*
- Vierer – *vierer*
- xr – *kreuzer*
- zecchino – *zecchino*
- cm – *cm*
- Klafter – *brasses*
- Daumen – *pouce*
- Elle – *coudée*
- Finger – *doigt*
- Fuss – *pied*
- Meile – *mille*
- Schritt – *pas*
- Schuh – *chaussure*
- Stab – *aune*
- Zoll – *pouce*
- Ballen – *ballot*
- Bürde – *bürde*
- carriage – *charretée*
- Dutzend – *douzaine*
- Fuder – *char*
- Gaden – *gaden*
- Kloben – *kloben*
- Laib – *miche*
- Loden – *loden*
- Maschen – *maschen*
- Paar – *paire*
- Riste – *riste*
- Schoch – *Schoch*
- Schubkarre – *brouette*
- Seil – *corde*
- Sester – *sester*
- Stock – *bâton*
- Stuck – *pièce*
- Zeine – *panier*
- Biner – *biner*
- denier – *denier (scrupule)*
- Gewäg – *gewäg*
- grain – *grain*
- Krinne – *krinne*
- Lot – *lot*
- Pfund – *livre*
- Pfefferpfund – *pfefferpfund*
- Rupp – *rupp*
- Quentli – *quentli*
- Unze – *once*
- Zentner – *quintal*
- Vierling – *un quart*
- leaf – *feuille*
- page – *page*
- month – *mois*
- week – *semaine*
- year – *an*

## Exemples

### Exemple 1

Indication de monnaie:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">umb
            <measure type="currency" origin="ZH" unit="lb" quantity="2">zwai phunt nuwer Zuricher
            </measure>
</egXML>
               
```

### Exemple 2

Unité de mesure:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            ... item oben här
            <measure type="area" unit="Juchart" quantity="8" commodity="field">acht juchart acher</measure>
            aneinanderen, genannt
            ....
        </egXML>
               
```

### Exemple 3

Unité de mesure:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Item <measure type="weight" unit="Zentner" quantity="1" commodity="wool">ein zentner landtwull
        </measure> git <measure type="currency" unit="ß" quantity="2">ij ß</measure>.
        </egXML>
               
```

### Exemple 4

Indication d'âge:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">... wan das jeman unser lannttluͤtten, er
            sye jung oder alltt,
            <measure type="age" unit="year" quantity="14">ob vierzechen jarenn</measure>
            von ainem paner endrunne ...
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [3.6.3. Numbers and Measures](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONANU)