---
title: hi
---



# `<hi/>` (mis en évidence)

## Description

Décrit la mise en surbrillance graphique du texte.

## Explication

La Legal Sources Foundation ne fait pas de transcriptions en fac-similé, c'est pourquoi les majuscules, les indentations, etc. ne sont pas indiquées. Les points devant les lettres en exposant dans les énumérations, les dates, les abréviations, etc. ne sont pas pris en compte. 

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

### @rend

Indique à quoi ressemble un caractère en question dans le texte original. 

*Valeurs possibles*

- center – *centré*
- framed – *encadré*
- font_change – *changement de police*
- italic – *cursif*
- left – *aligné à gauche*
- outdent – *dans la marge*
- right – *aligné à droite*
- rubricated – *rubriqué*
- sup – *suscrit*
- underline – *souligné*

## Exemples

### Exemple 1

Distinction des lettres en exposant

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">deß 1729<hi rend="sup">ten</hi> jahrs
        </egXML>
               
```

### Exemple 2

Exemples de soulignement par une main ultérieure - l'attribut hand est une référence à une handNote

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <hi rend="underline" hand="laterHand">unterstrichener Text mit anderer Tinte</hi>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.3.2.2. Emphatic Words and Phrases](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQHE)
- [3.3.2. Emphasis, Foreign Words, and Unusual Language](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHQH)