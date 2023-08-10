---
title: expan
---



# `<expan/>` (Auflösung)

## Beschreibung

Enthält die Auflösung einer Abkürzung.

## Erläuterung

Bei der Auflösung von Abkürzungen besser historische als moderne Schreibweise verwenden, wenn keine eindeutigen Anhaltspunkte für die Schreibweise vorhanden sind, z. B.: egen = egenante (nicht egenannte), schulth = schultheis (nicht schultheiss). Ao wird stillschweigend aufgelöst in anno. 

## Inhaltsmodell

- **core**: [term](term.md)
- **msdescription**: [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- Beliebiger Textinhalt

## Attribute

### @resp



*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `\S+`

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

## Abschnitte in den Guidelines der TEI

- [3.6.5. Abbreviations and Their Expansions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONAAB)