---
title: msContents
---



# `<msContents/>` (contenu du manuscrit)

## Description

Contient le registre et la langue du texte de la source.

## Modèle de contenu

- **msdescription**: [msItem](msItem.md) [summary](summary.md)

## Exemples

### Exemple 1

Structure exemplaire à l'exemple de SSRQ-SG-III_4-14-1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msContents>
        <summary>
            <p>Graf Heinrich II. von Werdenberg-Heiligenberg(-Rheineck) verleiht den Brüdern
                        Konrad, Heinz und Hans Grafer den Zoll von St. Ulrich und die Schenke in
                        Sevelen.
                    </p>
        </summary>
        <msItem>
            <textLang xml:lang="de" />
        </msItem>
    </msContents>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.6. Intellectual Content](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msco)