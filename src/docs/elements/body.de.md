---
title: body
---



# `<body/>` (Textbereich)

## Beschreibung

Enthält den transkribierten Quellentext sowie die zeitgleichen Dorsualnotizen in [`<ab/>`](ab.md).

## Inhaltsmodell

- **core**: [gap](gap.md) [pb](pb.md)
- **textstructure**: [div](div.md) [signed](signed.md)

## Beispiele

### Beispiel 1

Beispiel für einen Textbereich mit allen möglichen Kindelementen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <body>
        <div>
            <p>
                <lb />...
            </p>
        </div>
        <pb />
        <gap />
        <div>
            <ab type="dorsal" place="verso">
                <lb />...
            </ab>
        </div>
        <signed>
            <lb />...
        </signed>
    </body>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)