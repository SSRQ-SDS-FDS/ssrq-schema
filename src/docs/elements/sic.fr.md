---
title: sic
---



# `<sic/>` (du latin, ainsi)

## Description

Contient un texte manifestement incorrect.

## Explication

Les fautes d'orthographe évidentes peuvent être corrigées avec [`<corr/>`](corr.md). "[!]" N'est pas utilisé.

## Modèle de contenu

- **core**: [add](add.md) [del](del.md) [lb](lb.md) [note](note.md) [pb](pb.md) [term](term.md)
- **msdescription**: [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **transcr**: [subst](subst.md)
- Contenu de texte au choix

## Exemples

### Exemple 1

Facile à utiliser

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sic>ernschlich</sic>
</egXML>
               
```

### Exemple 2

Utilisation avec term

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />der
            <sic>
        <term ref="lem014672.11">hexenry</term>
    </sic>
            anzenemmen.
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5.1. Apparent Errors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDCOR)