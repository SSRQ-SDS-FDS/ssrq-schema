---
title: time
---



# `<time/>` (temps)

## Description

Contient une spécification de temps.

## Explication

A l'aide des attributs autorisés, les informations peuvent être exprimées dans un format normalisé lisible par machine. Le format est le sous-ensemble de la norme ISO 8601 défini par le W3C. Les moments dans le temps sont spécifiés avec [@when-custom](#when-custom)  ou[@notBefore-custom](#notBefore-custom)  et[@notAfter-custom](#notAfter-custom), les périodes de temps avec[@from-custom](#from-custom)  et[@to-custom](#to-custom). Des périodes de temps sans début ni fin peuvent être spécifiées avec[@dur-iso](#dur-iso). Moments indéterminés de la journée, par ex. la nuit, sont étiquetés avec[@period](#period).

## Modèle de contenu

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

### @dur-iso

Saisie Période selon [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen). Commence par l'abréviation P (période) suivie de T (temps) et de chiffres arabes. Les périodes de temps répétitives sont exprimées dans un format complet et commencent par l'abréviation R (Repeated). Sinon, les valeurs suivantes sont attribuées

- H = hour
- M = minute
- S = second

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(R/)?PT(\d+(\.\d+)?[HMS])+`

### @from-custom

Indique le point de départ d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @notAfter-custom

Indique le point final d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @notBefore-custom

Indique le point de départ d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @period

Fait référence à une période nommée, comme les saisons ou les jours de la semaine. En revanche, l'attribut [@dur-iso](#dur-iso)  est utilisé pour des périodes telles que "quatre semaines".

*Valeurs possibles*

- afternoon – *l’après-midi*
- byNight – *la nuit*
- byDay – *le jour*
- evening – *le soir*
- morning – *le matin*
- noon – *à midi*

### @to-custom

Indique le point final d'une période selon ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

### @when-custom

Spécifie une date conformément à la norme ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]`

## Exemples

### Exemple 1

Saisie d'un moment

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <time when-custom="08:48:00">8 Uhr 48</time>
</egXML>
               
```

### Exemple 2

Saisie de périodes de temps qui ne peuvent pas être décrites avec ISO 8601

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            ...
            <time period="byNight">nachtz</time>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.6.4. Dates and Times](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONADA)