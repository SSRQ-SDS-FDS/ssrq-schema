---
title: respStmt
---



# `<respStmt/>` (Angaben zur Verantwortlichkeit)

## Beschreibung

Enthält Elemente zur Beschreibung der Verantwortlichkeit an der Edition. 

## Inhaltsmodell

- **core**: [resp](resp.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md)

## Beispiele

### Beispiel 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <respStmt>
        <persName>Rainer Hugener</persName>
        <resp key="transcript" />
    </respStmt>
    <respStmt>
        <persName>Rainer Hugener</persName>
        <resp key="tagging" />
    </respStmt>
    <respStmt>
        <persName>Werner Meier</persName>
        <resp key="facs" />
    </respStmt>
    <respStmt>
        <persName>Pascale Sutter</persName>
        <resp key="qualitycheck" />
    </respStmt>
</egXML>
               
```

### Beispiel 2

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <respStmt>
        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
        <resp key="publisher" />
    </respStmt>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2.2. The Edition Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD22)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)