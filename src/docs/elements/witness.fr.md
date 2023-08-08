---
title: witness
---



# `<witness/>` (témoin)

## Description

Contient la description d'un morceau d'une source.

## Modèle de contenu

- **msdescription**: [msDesc](msDesc.md)

## Attributs

### @n

Donne un nombre (ou une autre étiquette) pour un élément, qui n'est pas nécessairement unique dans le document TEI.

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[A-Z][0-9]?`

### @xml:id

Fournit un identifiant unique pour l'élément qui porte l'attribut

*Valeurs possibles*

- Identificateur – Restriction: expression régulière `id-ssrq-[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}`

## Exemples

### Exemple 1

Exemple de plusieurs descriptions de témoins textuels

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <listWit>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d" n="A">
            <msDesc>
                ...
            </msDesc>
        </witness>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e" n="B">
            <msDesc>
                ...
            </msDesc>
        </witness>
        <witness xml:id="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f" n="C">
            <msDesc>
                ...
            </msDesc>
        </witness>
    </listWit>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [12.1. The Apparatus Entry, Readings, and Witnesses](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TCAPLL)