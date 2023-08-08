---
title: sic
---



# `<sic/>` (Lateinisch für 'auf diese Weise', 'so')

## Beschreibung

Enthält offensichtlich fehlerhaften Text.

## Erläuterung

Offensichtliche Schreibfehler können mit [`<corr/>`](corr.md)  korrigiert werden. Auf die Verwendung von "[!]" wird verzichtet.

## Inhaltsmodell

- **core**: [add](add.md) [del](del.md) [lb](lb.md) [note](note.md) [pb](pb.md) [term](term.md)
- **msdescription**: [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **transcr**: [subst](subst.md)
- Beliebiger Textinhalt

## Beispiele

### Beispiel 1

Einfache Verwendung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <sic>ernschlich</sic>
</egXML>
               
```

### Beispiel 2

Verwendung mit term

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />der
            <sic>
        <term ref="lem014672.11">hexenry</term>
    </sic>
            anzenemmen.
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.5.1. Apparent Errors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COEDCOR)