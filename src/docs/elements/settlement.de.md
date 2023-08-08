---
title: settlement
---



# `<settlement/>`

## Beschreibung

Erfassung eines Siedlungsnamens (Standort des Archivs) innerhalb von [`<msIdentifier/>`](msIdentifier.md).

## Inhaltsmodell

- Beliebiger Textinhalt

## Attribute

### @ref

Verknüpfung des Ortes mit der ID der Ortsdatenbank. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `loc\d{6}(\.\d{2})?`

## Beispiele

### Beispiel 1

Beispielhafte Erfassung des Städtenamens eines Archivs

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <repository xml:lang="de">Staatsarchiv
                    <settlement ref="loc000082">St. Gallen</settlement>
        </repository>
        <idno xml:lang="de">StASG AA 2 B 001a, fol. 1r–5r</idno>
    </msIdentifier>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [13.2.3. Place Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPLAC)