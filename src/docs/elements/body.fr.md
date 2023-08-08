---
title: body
---



# `<body/>` (Rubrique de texte)

## Description

Contient le texte transcrit de la source ainsi que les notes dorsales dans [`<ab/>`](ab.md).

## Modèle de contenu

- **core**: [gap](gap.md) [pb](pb.md)
- **textstructure**: [div](div.md) [signed](signed.md)

## Exemples

### Exemple 1

Exemple d'une zone de texte avec tous les éléments enfants possibles

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <body>
        <div>
            <p>
                <lb />...
            </p>
        </div>
        <pb />
        <gap />
        <div>
            <ab type="dorsal" place="verso">
                <lb />...
            </ab>
        </div>
        <signed>
            <lb />...
        </signed>
    </body>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)