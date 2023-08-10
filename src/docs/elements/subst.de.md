---
title: subst
---



# `<subst/>`

## Beschreibung

Enthält eine Ersetzung.

## Erläuterung

Gruppiert eine oder mehrere Tilgungen (oder überschüssigen Text) mit einer oder mehreren Hinzufügungen, wenn die Kombination als einzelner Eingriff in den Text zu betrachten ist. 

## Inhaltsmodell

- **core**: [add](add.md) [del](del.md)

## Beispiele

### Beispiel 1

Beispiel für eine Ersetzung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <subst>
        <del>zugeschafft</del>
        <add place="above">angethan</add>
    </subst>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.1.5. Substitutions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHSU)