---
title: listBibl
---



# `<listBibl/>` (liste de références bibliographiques)

## Description

Contient des informations bibliographiques encodées avec [`<bibl/>`](bibl.md).

## Modèle de contenu

- **core**: [bibl](bibl.md)

## Attributs

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- edition – *édition*
- literature – *littérature*
- summary – *résumé*
- translation – *la traduction*
- url – *URL*

## Exemples

### Exemple 1

Références à Regsten

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <listBibl type="summary">
        <bibl>Rigendinger 2007, S. 221–223</bibl>
    </listBibl>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.1. Methods of Encoding Bibliographic References and Lists of References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBITY)
- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)
- [15.3.2. Declarable Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCAS2)