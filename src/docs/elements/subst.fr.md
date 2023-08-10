---
title: subst
---



# `<subst/>` ( substitution)

## Description

Contient un remplacement.

## Explication

Regroupe une suppression avec un ajout lorsque la combinaison doit être considérée comme une seule intrusion dans le texte. 

## Modèle de contenu

- **core**: [add](add.md) [del](del.md)

## Exemples

### Exemple 1

Exemple de remplacement

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <subst>
        <del>zugeschafft</del>
        <add place="above">angethan</add>
    </subst>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [11.3.1.5. Substitutions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHSU)