---
title: msItem
---



# `<msItem/>` (item de manuscrit)

## Description

Contient des informations sur chaque partie d'une source.

## Explication

Les langues de texte de la source sont spécifiées avec [`<textLang/>`](textLang.md). Dans le cas de manuscrits, les auteurs peuvent être spécifiés avec[`<author/>`](author.md), dans le cas de publications imprimées, le lieu d'impression et l'imprimeur peuvent être spécifiés dans[`<docImprint/>`](docImprint.md).

## Modèle de contenu

- **core**: [author](author.md) [textLang](textLang.md)
- **textstructure**: [docImprint](docImprint.md)

## Exemples

### Exemple 1

Structure modèle

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msItem>
        <textLang xml:lang="de" />
    </msItem>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.6.1. The msItem and msItemStruct Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mscoit)