---
title: foreign
---



# `<foreign/>` (étranger)

## Description

Contient du texte dans une langue différente de celle du texte principal. 

## Explication

"Actum", "datum" ou "etc." ne sont pas marqués avec [`<foreign/>`](foreign.md). Les passages de texte plus longs en langue étrangère sont également notés dans les métadonnées sous[`<textLang/>`](textLang.md). S'il s'agit d'une partie de la phrase qui peut être identifiée par un élément TEI, l'élément correspondant doit être fourni avec[@xml:lang](#xml:lang). Par exemple,[`<title/>`](title.md)  avec[@xml:lang](#xml:lang)  est utilisé pour un titre de livre en langue étrangère.

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

### @xml:lang

ISO-639-1-Abréviation de la langue

*Valeurs possibles*

- de – *Allemand*
- fr – *Français*
- he – *Hébreu*
- it – *Italien*
- la – *Latin*
- rm – *Romanche*

## Exemples

### Exemple 1

Paragraphe avec insertions en langues étrangères

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>Versigleter <foreign xml:lang="rm">scütt</foreign> entzwischen der gmeindt Langnetz
                und der gmeind Fallß <foreign xml:lang="la">ut jntus</foreign> zu sechen.
            </p>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.3.2.1. Foreign Words or Expressions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQHF)