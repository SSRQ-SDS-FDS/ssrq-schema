---
title: availability
---



# `<availability/>` (Verfügbarkeit)

## Beschreibung

Beschreibt die Verfügbarkeit eines Textes.

## Erläuterung

Gibt Einschränkungen bezüglich des Gebrauchs oder der Weitergabe, Lizensierungen usw. an. Wir benutzen den Tag, um die Institution, die uns Faksimiles zur Verfügung gestellt hat, zu erwähnen. Ein Faksimile kann von einem Drittanbieter (und nicht von der Institution, indem die Quelle archiviert ist) erstellt werden. Eine Quelle kann im AVN liegen, das Faksimile wurde aber von der BPUN zur Verfügung gestellt bzw. erstellt. 

## Inhaltsmodell

- **header**: [licence](licence.md)

## Beispiele

### Beispiel 1

Modellhafter Aufbau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <availability>
        <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">Attribution-NonCommercial-
                    ShareAlike 4.0 International (CC BY-NC-SA
                    4.0)
                </licence>
    </availability>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)