---
title: precision
---



# `<precision/>`

## Description

Indique une incertitude dans la datation.

## Explication

 [@match](#match)  est utilisé pour faire référence à un ou plusieurs attributs de[`<date/>`](date.md).[@precision](#precision)  spécifie le degré d'incertitude.

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @match

Indique la partie incertaine - l'attribut incertain - d'une datation à l'aide d'une simple expression XPath. 

*Valeurs possibles*

- Chaîne de caractères

### @precision



*Valeurs possibles*

- high
- medium
- low
- unknown

## Exemples

### Exemple 1

Exemple de date incertaine

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <date datingMethod="julian" notBefore-custom="1341-01-01" notAfter-custom="1355-12-31">
        Um 1346 und um 1350
        <precision precision="low" match="@notBefore-custom @notAfter-custom" />
    </date>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [21.2. Indications of Precision](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html#CEPREC)