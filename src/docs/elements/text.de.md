---
title: text
---



# `<text/>`

## Beschreibung

Beinhaltet alle physisch auf einem Quellenstück oder in einem Buch vorhandenen Zeichen (Transkription / Edition, d. h. Primärdaten) sowie die Kommentierung eines edierten Stücks. 

## Inhaltsmodell

- **textstructure**: [back](back.md) [body](body.md)

## Attribute

### @type



*Mögliche Werte*

- summary – *Regest des Quellstücks*
- transcript – *Transkript des Quellstücks*

## Beispiele

### Beispiel 1

Beispiel für ein Transkript mit optionalem Kommentarbereich

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <text type="transcript">
        <body>
                ...
            </body>
        <back>
                ...
            </back>
    </text>
</egXML>
               
```

### Beispiel 2

Beispiel für ein Regest ohne Kommentarbereich

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <text type="summary">
        <body>
                ...
            </body>
    </text>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)
- [15.1. Varieties of Composite Text](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CC.html#CCDEF)