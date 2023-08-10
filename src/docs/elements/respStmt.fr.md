---
title: respStmt
---



# `<respStmt/>` (Informations sur la responsabilité)

## Description

Contient des éléments pour décrire la responsabilité de l'édition. 

## Modèle de contenu

- **core**: [resp](resp.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md)

## Exemples

### Exemple 1

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

### Exemple 2

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <respStmt>
        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
        <resp key="publisher" />
    </respStmt>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.12.2.2. Titles, Authors, and Editors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOR)
- [2.2.1. The Title Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD21)
- [2.2.2. The Edition Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD22)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)