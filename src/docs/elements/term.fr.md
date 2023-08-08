---
title: term
---



# `<term/>` (terme)

## Description

Contient un lemme ou un mot-clé.

## Explication

Les entrées sont liées aux bases de données du registre via l'attribut [@ref](#ref).

## Modèle de contenu

- **core**: [add](add.md) [choice](choice.md) [del](del.md) [gap](gap.md) [hi](hi.md) [lb](lb.md) [note](note.md) [p](p.md) [pb](pb.md) [sic](sic.md) [unclear](unclear.md)
- **namesdates**: [persName](persName.md)
- **transcr**: [damage](damage.md) [subst](subst.md)
- Contenu de texte au choix

## Attributs

### @ref

Référence aux bases de données de lemmes et de mots-clés. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `key\d{6}$?`
- Chaîne de caractères – Restriction: expression régulière `lem\d{6}(\.1?\d{2})?`

## Exemples

### Exemple 1

Une entrée dans le glossaire sur le Sarganserländer Band dans TEI

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Item alz aber beid <term ref="lem001301.09">
            partyen
        </term> der
            <term ref="lem005912.01">richtung</term>
    <term ref="lem006058.01">gichtig
                sind</term>, wie die beschehen ist,
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [3.4.1. Terms and Glosses](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHTG)