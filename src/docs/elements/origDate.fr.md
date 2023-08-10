---
title: origDate
---



# `<origDate/>` (date de la création)

## Description

Contient les données originales des textes sources édités (date d'édition). 

## Explication

Il peut également y avoir plusieurs dates originales dans un modèle d'édition. Avec [@when-custom](#when-custom)  et[@datingMethod](#datingMethod)  la date est enregistrée conformément aux directives de datation. Pour savoir comment gérer les jours saints et autres fêtes religieuses, voir[`<date/>`](date.md).[`<date/>`](date.md)  est utilisé dans les commentaires et les annotations. La date normalisée d'un morceau édité est enregistrée dans les métadonnées. Le jour est utilisé dans la rétro-numérisation pour la date d'origine normalisée d'un document conformément aux directives de datation. Dans le cas de regesta, la date dans la langue d'origine doit être ajoutée avec[`<orig/>`](orig.md)  après la date normalisée.

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

### @calendar

Calendrier utilisé (dans le contenu de l'élément) 

*Valeurs possibles*

- annunciation – *le style de l’Annonciation*
- circumcision – *le style de la Circoncision*
- gregorian – *le calendrier grégorien*
- julian – *le calendrier julien*
- natal – *le style de la Nativité*
- unknown – *inconnu*

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

### @when-custom

Spécifie une date conformément à la norme ISO 8601. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `(\d{4}|-)-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])`

## Exemples

### Exemple 1

Datation originale des actes

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <origDate when-custom="1448-05-25" calendar="gregorian">uf sant Urbans tag in dem jár,
                do man zalt nach Cristi unsers herren gepurt tusend vierhundert und im acht und
                viertzigosten jâr
            </origDate>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.3.1. Origination](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msdates)