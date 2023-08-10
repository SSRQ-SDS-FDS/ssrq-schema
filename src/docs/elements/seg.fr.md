---
title: seg
---



# `<seg/>` (segment quelconque)

## Description

Paragraphes insérés par l'éditeur pour structurer le texte source. 

## Explication

Utilisé à l'intérieur de [`<p/>`](p.md). D'autre part,[`<div/>`](div.md)  et[`<p/>`](p.md)  ne sont utilisés que pour les paragraphes originaux.

Avec des textes originaux plus longs tels que des ouvertures ou des urbaria, il peut être judicieux de numéroter des articles, des paragraphes ou des paragraphes avec [`<seg/>`](seg.md)  avec[@n](#n). Mais pas d'"hyperstructuration" s'il vous plait: numéroter seulement là où la structure du texte le permet (cf. exemples dans les volumes imprimés du SSRQ). Pour la structuration des formules de clôture, voir les exemples sur la page Formules de clôture.

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

### @n

Donne un nombre (ou une autre étiquette) pour un élément, qui n'est pas nécessairement unique dans le document TEI.

*Valeurs possibles*

- Chaîne de caractères

### @resp

Indique l'agent responsable de l'intervention ou de l'interprétation, par exemple un éditeur ou un transcripteur.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

## Exemples

### Exemple 1

Exemple de paragraphes introduits par l'éditeur

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seg n="1" resp="CS">
        <lb />Item wann man den raut bu̍ttet an ain  unnd welcher dann nit
        <lb />kompt, der gitt zuͦ buͦß ain schilling haller
    </seg>
    <seg n="2" resp="CS">
        <lb />Item so man den raut bu̍ttet an ain marck silbers unnd welcher dann
        <lb />nit kompt, der gitt zuͦ buͦß ii .
    </seg>
    <seg n="3" resp="CS">
        <lb />Item wann man den raut bu̍tet by dem ayd unnd weder von der statt
        <lb />ze ritten noch zuͤ gon, welcher dann nit kompt, der gitt zuͦ buͦß
        <lb />v  haller.
    </seg>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [16.3. Blocks, Segments, and Anchors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SASE)
- [6.2. Components of the Verse Line](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/VE.html#VESE)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)