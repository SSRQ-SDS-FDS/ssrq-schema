---
title: term
---



# `<term/>` (Fachbegriff)

## Beschreibung

Enthält ein Stichwort oder Schlagwort.

## Erläuterung

Über das Attribut [@ref](#ref)  werden die Einträge mit den Registerdatenbanken verknüpft.

## Inhaltsmodell

- **core**: [add](add.md) [choice](choice.md) [del](del.md) [gap](gap.md) [hi](hi.md) [lb](lb.md) [note](note.md) [p](p.md) [pb](pb.md) [sic](sic.md) [unclear](unclear.md)
- **namesdates**: [persName](persName.md)
- **transcr**: [damage](damage.md) [subst](subst.md)
- Beliebiger Textinhalt

## Attribute

### @ref

Referenz auf Lemma- und Schlagwortdatenbank.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `key\d{6}$?`
- Zeichenkette – Einschränkung: regulärer Ausdruck `lem\d{6}(\.1?\d{2})?`

## Beispiele

### Beispiel 1

Glossareinträge des Sarganserländer Bandes in TEI

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">Item alz aber beid <term ref="lem001301.09">
            partyen
        </term> der
            <term ref="lem005912.01">richtung</term>
    <term ref="lem006058.01">gichtig
                sind</term>, wie die beschehen ist,
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.4.1. Terms and Glosses](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COHTG)