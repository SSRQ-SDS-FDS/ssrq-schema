---
title: unclear
---



# `<unclear/>` (incertain)

## Description

Contient une lecture incertaine.

## Explication

Si la cause est un dommage, cela est indiqué par [`<damage/>`](damage.md).[@cert](#cert)  peut être utilisé pour spécifier le degré de sécurité de la lecture. Si un passage s'avère absolument illisible, il est marqué d'un[`<gap/>`](gap.md).

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

### @cert

Indication du degré de certitude

*Valeurs possibles*

- high – *élevé*
- medium – *moyen*
- low – *faible*

## Exemples

### Exemple 1

Exemple de passage endommagé dont la lecture est incertaine

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damage agent="ink_blot">
        <unclear>die</unclear>
    </damage>
</egXML>
               
```

### Exemple 2

Lecture non sécurisée sans dommage

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">ve<unclear cert="high">stik</unclear>lich
        </egXML>
               
```

### Exemple 3

Lecture incertaine qui n'est pas due à un dommage, mais à l'encre faible. L'éditeur utilise unclear avec damage pour indiquer son incertitude sur ce passage

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">und sol och der w
            <damage agent="faded_ink">
        <unclear>eib</unclear>
    </damage>
            el
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.3.1. Damage, Illegibility, and Supplied Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHDA)
- [3.5.3. Additions, Deletions, and Omissions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDADD)