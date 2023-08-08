---
title: history
---



# `<history/>` (histoire)

## Description

Contient des informations sur l'historique d'un document. Ceux-ci incluent, par exemple, la datation ou le lieu d'émission. 

## Modèle de contenu

- **msdescription**: [origin](origin.md)

## Exemples

### Exemple 1

Modèle de construction, y compris la datation et le lieu d'exposition

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <history>
        <origin>
            <origDate from-custo="1532-05-20" to-custom="1532-12-31" calendar="unknown" />
            <origPlace ref="loc000701">Schaffhausen</origPlace>
        </origin>
    </history>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.8. History](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mshy)