---
title: p
---



# `<p/>` (paragraphe)

## Description

Décrit un paragraphe.

## Explication

Dans la transcription, ceci est utilisé pour marquer les paragraphes originaux. Le texte est structuré par l'éditeur avec [`<seg/>`](seg.md). Voir aussi les explications "Structuration des textes" dans les consignes de transcription SSRQ et la description de[`<div/>`](div.md). Si le texte d'un certificat est structuré par un espace ou une initiale, le paragraphe peut être marqué d'un[`<p/>`](p.md). Les signes de paragraphe, cependant, ne sont pas spécialement marqués.

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [bibl](bibl.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [list](list.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [ref](ref.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
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

Exemple d'utilisation en combinaison avec seg.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <p>
        <seg>
            <lb />Man sol ôch zuͦ den selben meyen oder herbst taͤding richten<lb />umb
                    eigen oder umb erb und von keiner sunderbaren sache,<lb />es sy denn beider teil
                    wille.
                </seg>
    </p>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.1. Paragraphs](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COPA)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)