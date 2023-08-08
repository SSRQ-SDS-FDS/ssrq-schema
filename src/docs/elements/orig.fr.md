---
title: orig
---



# `<orig/>` (forme originale)

## Description

Contient des parties de texte écrites dans la langue originale dans les introductions, les commentaires et les notes. 

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

Exemple d'expression de la langue d'origine dans une annotation.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <note>Am Beispiel von Seebach lässt sich beobachten, wie Nachträge aus Beschlüssen
                der <orig>bursamy</orig> [...] zustande kommen.
            </note>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5.2. Regularization and Normalization](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDREG)
- [12. Critical Apparatus](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TC)