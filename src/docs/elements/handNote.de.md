---
title: handNote
---



# `<handNote/>`

## Beschreibung

Beschreibt eine Hand und identifiziert sie gegebenenfalls mit einem Schreiber. 

## Inhaltsmodell

- **core**: [date](date.md) [p](p.md)

## Attribute

### @n



*Mögliche Werte*

- firstHand – *Anlagehand (A)*
- secondHand – *Nachtragshand (B)*
- thirdHand – *Nachtragshand (C)*
- fourthHand – *Nachtragshand (D)*
- fifthHand – *Nachtragshand (E)*
- sixthHand – *Nachtragshand (F)*
- seventhHand – *Nachtragshand (G)*
- eighthHand – *Nachtragshand (H)*
- ninthHand – *Nachtragshand (I)*
- laterHand – *von späterer Hand*
- otherHand – *von anderer Hand*

### @scribe

Bezeichnet den Schreiber mit der Identifikationsnummer der Person. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `per\d{6}[abc]?(\.\d{2})?`

### @xml:id



*Mögliche Werte*

- Identifikator

## Beispiele

### Beispiel 1

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <physDesc>
        <handDesc>
            <handNote xml:id="hand1" n="firstHand" scribe="per123456">
                <date from-custom="1001-01-01" to-custom="1100-12-31">
                    <precision precision="low" match="@from-custom" />
                </date>
            </handNote>
            <handNote xml:id="hand2" n="secondHand" />
            <handNote xml:id="hand3" n="otherHand" />
            <handNote xml:id="hand4" n="laterHand" />
        </handDesc>
    </physDesc>
    <delSpan rend="crossout" hand="hand1" spanTo="del1" />
            Item ein hoffstatt ...
            <anchor xml:id="del1" />
    <addSpan place="left_margin" spanTo="add1" hand="hand4" />
            Item ...
            <anchor xml:id="add1" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [10.7.2. Writing, Decoration, and Other Notations](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msph2)