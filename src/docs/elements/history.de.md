---
title: history
---



# `<history/>`

## Beschreibung

Enthält Informationen zur Geschichte eines Dokuments. Dazu zählen beispielsweise Datierung oder der Ausstellungsort. 

## Inhaltsmodell

- **msdescription**: [origin](origin.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau inklusive Datierung und Ausstellungsort

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

## Abschnitte in den Guidelines der TEI

- [10.8. History](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mshy)