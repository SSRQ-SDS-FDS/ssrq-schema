---
title: delSpan
---



# `<delSpan/>`

## Beschreibung

Bezeichnet größere Abschnitte, die aus dem Text getilgt wurden.

## Erläuterung

Mit [@spanTo](#spanTo)  wird zwingend auf den Endpunkt der Tilgung verwiesen, der mit[`<anchor/>`](anchor.md)  markiert wird.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @hand

Enthält einen Verweis auf die ID eines [`<handNote/>`](handNote.md)-Element, das im[`<teiHeader/>`](teiHeader.md)  deklariert wurde.

*Mögliche Werte*

- Verweis auf Identifikator

### @rend



*Mögliche Werte*

- blackened – *Streichung durch Schwärzen*
- bracketed – *Streichung durch Verwendung von Klammern*
- crossout – *Streichung durch gekreuzte Linien*
- overwritten – *Streichung durch direkte Überschreibung*
- rubbing – *Streichung durch Textlöschung/Rasur*
- strikethrough – *Streichung durch einfache Durchstreichung*
- subpunction – *Streichung durch Unterpunktung*
- underline – *Streichung mit Unterstreichen*

### @spanTo

Verweist auf die [@xml:id](#xml:id)  eines Endpunktes

*Mögliche Werte*

- Verweis auf Identifikator

## Beispiele

### Beispiel 1

Beispiel für eine umfangreichere Tilgung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <delSpan spanTo="del1" hand="otherHand" rend="crossout" />
    <lb />Wir der Burgermeyster
    <lb />Radt und der groß Radt. Embietend
    <lb />allen und yeden unsern Burgeren
    <lb />unsern günstlichen gruͦß / geneygten
    <lb />willen / unnd alles guͦts zuͦvor / unnd thuͦnd üch sampt unnd sunders
    <lb />zuͦ vernemmen.
    <anchor xml:id="del1" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [11.3.1.4. Additions and Deletions](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHAD)