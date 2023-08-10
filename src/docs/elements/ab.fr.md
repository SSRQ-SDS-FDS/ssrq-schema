---
title: ab
---



# `<ab/>` (bloc anonyme)

## Description

Contient un niveau de texte quelconque sans affectation clairement définie. 

## Explication

Nous utilisons toujours cette balise avec [@type](#type)  et[@place](#place)  pour les mentions, les notes dorsales, les mentions de chancellerie et les mentions de registre ainsi que pour les marginalia.

Pour les documents pontificaux, les mentions sont indiquées dans l'ordre suivant: d'abord les mentions sous le plica, ensuite les mentions sur le plica de gauche à droite et enfin les mentions au verso du document de gauche à droite. 

Les annotations et les notes dorsales sont enregistrées dans l'ordre chronologique. En raison de l'ordre chronologique, les mentions contemporaines sont toujours mentionnées en premier lieu. Les notes simultanées sont enregistrées dans le sens de lecture de haut en bas et de gauche à droite. Si, par exemple, une mention dorsale figure au verso d'un missile, suivie de l'adresse et de deux autres mentions dorsales, l'adresse figure tout de même en premier lieu. Si le sens de lecture auquel on doit se référer n'est pas uniforme, c'est-à-dire si une mention dorsale est à l'envers, un commentaire est nécessaire. 

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

### @hand

Contient une référence à l'ID d'un élément [`<handNote/>`](handNote.md)  déclaré dans le[`<teiHeader/>`](teiHeader.md).

*Valeurs possibles*

- Référence à l'identifiant

### @place

Lieu d'une note dorsale, d'une note, d'une note d'enregistrement ou d'une note de chancellerie 

*Valeurs possibles*

- above – *au-dessus de la ligne*
- below – *au-dessous de la ligne*
- bottom – *en bas de page*
- cover – *sur la couverture*
- cover_above – *en haut de la couverture*
- cover_bottom – *en bas de la couverture*
- cover_middle – *au milieu de la couverture*
- left_margin – *dans la marge de gauche*
- next_page – *sur la page suivante*
- right_margin – *dans la marge de droite*
- verso – *au verso*
- left_plica – *du côté gauche de la plica*
- parchment_tag – *à une lanière en parchemin*
- plica – *sur la plica*
- plica_verso – *au verso de la plica*
- right_plica – *du côté droit de la plica*
- sub_plica – *au-dessous de la plica*
- verso_above – *au verso en haut*
- verso_above_left – *au verso en haut à gauche*
- verso_above_middle – *au verso en haut au milieu*
- verso_above_right – *au verso en haut à droite*
- verso_bottom – *au verso en bas*
- verso_bottom_left – *au verso en bas à gauche*
- verso_bottom_middle – *au verso en bas au milieu*
- verso_bottom_right – *au verso en bas à droite*
- verso_middle – *au centre du verso de la page*

### @type

Classification de l'élément

*Valeurs possibles*

- address – *Adresse*
- archiving_reference – *Note d’archives*
- chancery_notation – *Annotation issue d’une chancellerie*
- computatio – *Annotation du computeur*
- dorsal – *Note dorsale*
- marginal_note – *Note*
- sigillant – *Annotation d’un sceau*
- tax – *Annotation de taxation*

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

Exemple de note de service

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <ab type="chancery_notation" place="right_plica" xml:lang="la">
        Ad mandatum domini regis
        <persName>Ulricus de Albeck</persName>
        <note>Ulrich von Albeck (1431 gestorben, ab 1401 Angehöriger der Kanzlei
            König Ruprechts, später Bischof), vgl. Ruoff, Hochgerichtsbarkeit, S. 365.
        </note>
        decretorum doctor.
    </ab>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [16.3. Blocks, Segments, and Anchors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SASE)