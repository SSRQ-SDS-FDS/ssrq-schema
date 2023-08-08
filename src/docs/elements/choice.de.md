---
title: choice
---



# `<choice/>` (Alternative)

## Beschreibung

Enthält zwei Elemente zur alternativen Auszeichnung einer Textpassage. 

## Erläuterung

Der Tag enthält Elemente zur Auflösung von Abkürzungen oder zur Korrektur von Verschreibern. Die Auflösung der Abkürzung bzw. die Korrekturen stehen nach dem originalen Text. 

## Inhaltsmodell

- **core**: [abbr](abbr.md) [corr](corr.md) [expan](expan.md) [sic](sic.md)

## Beispiele

### Beispiel 1

Beispiel für eine Abkürzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <abbr>sabbo</abbr>
        <expan>sabbato</expan>
    </choice>
</egXML>
               
```

### Beispiel 2

Beispiel für eine Korrektur

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <sic>offensiche</sic>
        <corr resp="anh">offenliche</corr>
    </choice>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5. Simple Editorial Changes](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COED)