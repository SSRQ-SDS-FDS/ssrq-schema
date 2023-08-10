---
title: extent
---



# `<extent/>` (étendue)

## Description

Décrit les dimensions d'une source.

## Modèle de contenu

- **core**: [measure](measure.md)
- **msdescription**: [dimensions](dimensions.md)

## Exemples

### Exemple 1

Structure modèle

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <extent>
        <dimensions type="leaves">
            <height unit="cm" quantity="16.0" />
            <width unit="cm" quantity="23.0" />
        </dimensions>
        <dimensions type="plica">
            <width unit="cm" quantity="4.0" />
        </dimensions>
        <measure type="text_scope" unit="leaf" quantity="2" />
        <measure type="text_scope" unit="page" quantity="4" />
    </extent>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [2.2.3. Type and Extent of File](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD23)
- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)
- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)
- [10.7.1. Object Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph1)