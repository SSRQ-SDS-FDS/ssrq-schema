---
title: date
---



# `<date/>` (date)

## Description

Contient une date dans le texte de l'éditeur.

## Explication

La datation dans les textes sources (données originales) est marquée par [`<origDate/>`](origDate.md). Les règles de datation doivent être respectées.

## Modèle de contenu

- **certainty**: [precision](precision.md)
- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

### @datingMethod

Calendrier utilisé (dans les attributes de la classe att.datable.custom) 

*Valeurs possibles*

- annunciation – *le style de l’Annonciation*
- circumcision – *le style de la Circoncision*
- gregorian – *le calendrier grégorien*
- julian – *le calendrier julien*
- natal – *le style de la Nativité*
- unknown – *inconnu*

### @dur-iso

Saisie Période selon [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen). Commence par l'abréviation P (période) suivie de chiffres arabes. Les périodes répétitives sont exprimées au format complet et commencent par l'abréviation R (Repeated). Sinon, les valeurs suivantes sont attribuées

- Y = year
- M = month
- W = week
- D = day
- H = hour

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(R/)?P(\d+(\.\d+)?[YMWDH])+`

### @from-custom

Indique le point de départ d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @notAfter-custom

Indique le point final d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @notBefore-custom

Indique le point de départ d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @period

Fait référence à une période nommée, comme les saisons ou les jours de la semaine. En revanche, l'attribut [@dur-iso](#dur-iso)  est utilisé pour des périodes telles que "quatre semaines".

*Valeurs possibles*

- P1WD – *dimanche*
- P2WD – *lundi*
- P3WD – *mardi*
- P4WD – *mercredi*
- P5WD – *jeudi*
- P6WD – *vendredi*
- P7WD – *samedi*
- spring – *printemps*
- summer – *été*
- fall – *automne*
- winter – *hiver*

### @to-custom

Indique le point final d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

### @type

Caractérisation plus détaillée d'une datation - utilisée pour les dates et les délais ainsi que pour le type de publication 

*Valeurs possibles*

- deadline – *délai*
- deadline_floating_holiday – *des fêtes sans date fixe comme délai*
- deadline_holiday – *des fêtes religieuses comme délai*
- electronic – *publication numérique*
- floating_holiday – *des fêtes sans date fixe*
- holiday – *des fêtes religieuses*
- print – *imprimé*

### @when-custom

Spécifie une date conformément à la norme ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

## Exemples

### Exemple 1

Exemple de datation au 03 mars 1631

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="gregorian" when-custom="1631-03-03">März, 03, 1631</date>
</egXML>
               
```

### Exemple 2

Exemple de distinction vers 1510

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" notBefore-custom="1510-01-01" to-custom="1515-12-31">ca. 1510
            </date>
</egXML>
               
```

### Exemple 3

Exemple de distinction de la période allant de la Pentecôte 1583 à la Pentecôte 1584

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" from-custom="1583-05-30" to-custom="1584-05-21">von Pfingstmontag 1583 bis Pfingstmontag 1584
            </date>
</egXML>
               
```

### Exemple 4

Exemple d'une double datation. Pour les textes qui sont doublement datés, c'est-à-dire selon l'ancien et le nouveau style, la datation est effectuée selon le nouveau style ou le calendrier grégorien.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date when-custom="1590-10-25" datingMethod="#Gregorian">25/15. octobris anno 90</date>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.6.4. Dates and Times](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONADA)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)
- [2.6. The Revision Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD6)
- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [15.2.3. The Setting Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAHSE)
- [13.4. Dates](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDDATE)