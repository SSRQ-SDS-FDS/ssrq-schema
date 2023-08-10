---
title: bindingDesc
---



# `<bindingDesc/>`

## Beschreibung

Enthält Informationen über die physische Struktur oder Bindung eines Textes. 

## Erläuterung

Mit diesem Tag können Details wie die Art der Bindung (z. B. Buchbindung, Broschur) angegeben werden. Die Beschreibung wird als Freitext in [`<p/>`](p.md)  angegeben.

## Inhaltsmodell

- **core**: [p](p.md)

## Beispiele

### Beispiel 1

Beschreibung eines kartonierten Ledereinbanes

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bindingDesc>
        <p xml:lang="de">Buch mit kartoniertem Ledereinband</p>
    </bindingDesc>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.3.1. Binding Descriptions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphbi)