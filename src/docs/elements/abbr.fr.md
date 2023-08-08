---
title: abbr
---



# `<abbr/>` (Abréviation)

## Description

Contient une abréviation.

## Explication

Aucun point d'abréviation n'est utilisé, car les abréviations sont déjà marquées comme telles par le balisage. 

Les conventions orthographiques du rédacteur sont prises en compte sans identification particulière. L'évidence est tacitement résolue, par ex. B. traits nasaux, affixes («-er», «con-», «per-»). Xsti est implicitement résolu en Christ, tout comme Ao = anno, wz = was ou dz = das. 

Les abréviations dans le modèle de texte sont développées à l'aide de [`<choice/>`](choice.md)  et[`<expan/>`](expan.md)  si cela est possible et utile.

Les abréviations de dimensions et les désignations de pièces ne sont pas résolues sauf en texte continu (commentaires, remarques). Les caractères spéciaux correspondants sont utilisés. 

## Modèle de contenu

- **core**: [hi](hi.md) [lb](lb.md) [sic](sic.md) [unclear](unclear.md)
- Contenu de texte au choix

## Exemples

### Exemple 1

Exemple d'abréviation

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <abbr>sabbo</abbr>
        <expan>sabbato</expan>
    </choice>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.6.5. Abbreviations and Their Expansions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONAAB)