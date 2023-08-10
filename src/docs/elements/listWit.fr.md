---
title: listWit
---



# `<listWit/>` (Liste des témoins textuelle)

## Description

Contient les descriptions des pièces des sources.

## Explication

Un [`<witness/>`](witness.md)  est créé pour chaque source.

## Modèle de contenu

- **textcrit**: [witness](witness.md)

## Exemples

### Exemple 1

Exemple de liste de témoins texte

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