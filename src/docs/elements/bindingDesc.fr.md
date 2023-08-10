---
title: bindingDesc
---



# `<bindingDesc/>` (description de la reliure)

## Description

Contient des informations sur la structure physique ou la reliure d'un texte. 

## Explication

Cette balise permet d'indiquer des détails tels que le type de reliure (par exemple, reliure de livre, brochage). La description est donnée en texte libre dans [`<p/>`](p.md).

## Modèle de contenu

- **core**: [p](p.md)

## Exemples

### Exemple 1

Description d'une reliure en cuir cartonnée

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bindingDesc>
        <p xml:lang="fr">Livre avec couverture en cuir cartonnée</p>
    </bindingDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.3.1. Binding Descriptions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphbi)