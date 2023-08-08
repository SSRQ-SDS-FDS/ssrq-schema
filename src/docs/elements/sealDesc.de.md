---
title: sealDesc
---



# `<sealDesc/>`

## Beschreibung

Enthält Elemente zur Beschreibung der Siegel.

## Erläuterung

Eine Urkunde, die ohne Siegel ausgestellt wurde, enthält auch keine [`<sealDesc/>`](sealDesc.md). Urkunden, bei denen einzelne Siegel fehlen, jedoch schon vgl.[`<seal/>`](seal.md),[@condition](#condition). Bei ausserordentlichen Befunden (z. B. Nachherstellungen) sollte ein Kommentar geschrieben werden.

## Inhaltsmodell

- **msdescription**: [seal](seal.md)

## Beispiele

### Beispiel 1

Beispielhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sealDesc>
        <seal n="1" material="..." shape="..." extent="..." attachment="..." condition="...">
            <persName role="sigillant" ref="perNNNNNN">NN</persName>
        </seal>
    </sealDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.3.2. Seals](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphse)