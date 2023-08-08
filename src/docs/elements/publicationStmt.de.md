---
title: publicationStmt
---



# `<publicationStmt/>` (Angaben zur Publikation)

## Beschreibung

Enthält Elemente zur Beschreibung der Publikation und Verbreitung des bearbeiteten Stücks. 

## Inhaltsmodell

- **core**: [date](date.md) [date](date.md) [publisher](publisher.md)
- **header**: [availability](availability.md)

## Beispiele

### Beispiel 1

Angaben zur Publikation mit Datum

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <publicationStmt>
        <publisher>SSRQ-SDS-FDS</publisher>
        <date type="electronic" when-custom="2019-08-15" />
        <date type="print" when-custom="2020-11-20" />
        <availability>
            <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">
                        Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA
                        4.0)
                    </licence>
        </availability>
    </publicationStmt>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)
- [2.2. The File Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD2)