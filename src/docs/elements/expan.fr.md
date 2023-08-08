---
title: expan
---



# `<expan/>` (Expansion)

## Description

Contient l'expansion d'une abréviation.

## Explication

Lors de la résolution des abréviations, utilisez l'orthographe historique plutôt que moderne lorsqu'il n'y a pas d'indice d'orthographe clair, par ex. B.: egen = egenante (non egenannte), schulth = schultheis (pas schultheiss). Ao est tacitement dissous dans anno. 

## Modèle de contenu

- **core**: [term](term.md)
- **msdescription**: [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- Contenu de texte au choix

## Attributs

### @resp

Indique l'agent responsable de l'intervention ou de l'interprétation, par exemple un éditeur ou un transcripteur.

*Valeurs possibles*

- anyURI – Restriction: expression régulière `\S+`

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