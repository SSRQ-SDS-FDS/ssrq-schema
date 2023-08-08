---
title: handDesc
---



# `<handDesc/>`

## Beschreibung

Beschreibt die Hände und alle Handwechsel.

## Erläuterung

Marginalien, Streichungen, Korrekturen usw. werden direkt an der Stelle im Text ausgezeichnet. Es werden nur "wichtige" Schreiber eingetragen. 

## Inhaltsmodell

- **header**: [handNote](handNote.md)

## Beispiele

### Beispiel 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <physDesc>
        <handDesc>
            <handNote xml:id="hand1" n="firstHand" scribe="per123456">
                <date from-custom="1001-01-01" to-custom="1100-12-31">
                    <precision precision="low" match="@from-custom" />
                </date>
            </handNote>
            <handNote xml:id="hand2" n="secondHand" />
            <handNote xml:id="hand3" n="otherHand" />
            <handNote xml:id="hand4" n="laterHand" />
        </handDesc>
    </physDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.2. Writing, Decoration, and Other Notations](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph2)