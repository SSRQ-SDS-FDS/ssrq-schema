---
title: sourceDesc
---



# `<sourceDesc/>` (Beschreibung der Quellen)

## Beschreibung

Enthält Elemente zur Beschreibung der Quelle bzw. der Quellen.

## Erläuterung

Beschrieben werden Inhalt (Regest), Aufbewahrungsort, Material, Layout, Schreiber, Siegel und bibliographische Bezüge. Da die meisten dieser Metadaten aus einem AIS oder einer Datenbank des Bearbeitenden exportiert und ins Portal importiert werden, werden hier nur noch die Siegel in [`<sealDesc/>`](sealDesc.md)  bzw.[`<seal/>`](seal.md)  genauer erfasst.

## Inhaltsmodell

- **msdescription**: [msDesc](msDesc.md)
- **textcrit**: [listWit](listWit.md)

## Beispiele

### Beispiel 1

Beispiel für eine Quellenbeschreibung mit einem Textzeugen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sourceDesc>
        <msDesc>
                ...
            </msDesc>
    </sourceDesc>
</egXML>
               
```

### Beispiel 2

Beispiel für eine Quellenbeschreibung mit einer Liste von Textzeugen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sourceDesc>
        <listWit>
                ...
            </listWit>
    </sourceDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.2.7. The Source Description](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD3)