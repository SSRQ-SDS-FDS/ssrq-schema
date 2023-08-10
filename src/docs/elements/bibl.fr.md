---
title: bibl
---



# `<bibl/>` (référence bibliographique.)

## Description

Contient une référence bibliographique avec des références de pages. 

## Explication

L'élément enfant [`<ref/>`](ref.md)  renvoie à des sites Web externes, à d'autres articles édités ou à la base de données de littérature Zotero.

## Modèle de contenu

- **core**: [ref](ref.md)
- Contenu de texte au choix

## Exemples

### Exemple 1

Saisie avec référence à la base de données bibliographiques

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="http://zotero.org/groups/5048222/items/M8D9EG5B" />, S. 93
            </bibl>
</egXML>
               
```

### Exemple 2

Saisie avec référence à une autre pièce

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="urn:ssrq:SSRQ-ZH-NF_II_11-74-1">SSRQ ZH NF II/11, Nr. 74</ref>
    </bibl>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.1. Methods of Encoding Bibliographic References and Lists of References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBITY)
- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)
- [15.3.2. Declarable Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAS2)