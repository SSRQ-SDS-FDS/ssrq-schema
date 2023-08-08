---
title: publisher
---



# `<publisher/>` (éditeur)

## Description

Dans le cas de publications, contient le nom de l'imprimeur dans le cadre de [`<docImprint/>`](docImprint.md)  et les détails de l'institution émettrice dans le cadre de[`<publicationStmt/>`](publicationStmt.md).

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

### Exemple 2

Exemple pour tei:publisher avec @cert

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <docImprint>
        <pubPlace>Zürich</pubPlace>
        <publisher cert="low">Heidegger und Rahn</publisher>
    </docImprint>
</egXML>
               
```

### Exemple 3

Exemple de tei:publisher au sein de tei:publicationStmt

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <publicationStmt>
        <publisher>SSRQ-SDS-FDS</publisher>
    </publicationStmt>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)