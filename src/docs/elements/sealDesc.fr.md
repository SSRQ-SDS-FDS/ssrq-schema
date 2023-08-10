---
title: sealDesc
---



# `<sealDesc/>` (description des sceaux)

## Description

Contient des éléments décrivant les sceaux.

## Explication

Un certificat délivré sans sceau ne contient pas non plus de [`<sealDesc/>`](sealDesc.md). Documents dans lesquels des sceaux individuels manquent, mais déjà cf.[`<seal/>`](seal.md),[@condition](#condition). Dans le cas de découvertes extraordinaires (par exemple, des reproductions), un commentaire doit être écrit.

## Modèle de contenu

- **msdescription**: [seal](seal.md)

## Exemples

### Exemple 1

Exemple de structure

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sealDesc>
        <seal n="1" material="..." shape="..." extent="..." attachment="..." condition="...">
            <persName role="sigillant" ref="perNNNNNN">NN</persName>
        </seal>
    </sealDesc>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.3.2. Seals](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphse)