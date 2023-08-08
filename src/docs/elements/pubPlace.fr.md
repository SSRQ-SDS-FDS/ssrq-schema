---
title: pubPlace
---



# `<pubPlace/>` (lieu de publication)

## Description

Contient le lieu de publication.

## Explication

Il peut s'agir à la fois du lieu de publication de l'édition électronique et du lieu de publication de l'article ou du livre répertorié dans la bibliographie. Dans le cas des publications, le lieu d'impression est nommé avec [`<pubPlace/>`](pubPlace.md)  dans[`<docImprint/>`](docImprint.md).

## Modèle de contenu

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

Exemple d'empreinte avec lieu d'impression et imprimeur

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher>Johann Heinrich Hamberger</publisher>
    </docImprint>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)