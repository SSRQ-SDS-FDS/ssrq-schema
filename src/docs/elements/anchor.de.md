---
title: anchor
---



# `<anchor/>` (Ankerpunkt)

## Beschreibung

Endpunkt einer umfangreichen Ergänzung ([`<addSpan/>`](addSpan.md) ), Streichung ([`<delSpan/>`](delSpan.md) ), oder Beschädigung ([`<damageSpan/>`](damageSpan.md) ).

## Erläuterung

Als Wert des Attributs [@xml:id](#xml:id)  ist der erste Teil des Namens der entsprechenden Elemente ([`<addSpan/>`](addSpan.md),[`<delSpan/>`](delSpan.md)  bzw.[`<damageSpan/>`](damageSpan.md) ) sowie eine fortlaufende Nummer zu wählen: z. B. add1, add2, usw. oder del1, del2, usw. oder damage1, damage2, usw.

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @xml:id



*Mögliche Werte*

- Identifikator – Einschränkung: regulärer Ausdruck `(del|damage|add)[1-9]+`

## Beispiele

### Beispiel 1

Beispiel für eine umfangreichere Hinzufügung

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <addSpan spanTo="add1" hand="otherHand" place="bottom" rend="pencil" />
    <lb />Presentibus
    <lb />Antonio nepote domini officialis, fratre Germano ordinis Predicatorum; dominus
    <lb />officialis prefatus monuit dictam Jordanam pro secunda dilatione
    <lb />et assignata est ad cras pro tertia.
    <lb />Delayens
    <anchor xml:id="add1" />
</egXML>
               
```

### Beispiel 2

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

### Beispiel 3

Beispiel für einen umfangreicheren Schaden

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <damageSpan agent="faded_ink" spanTo="damage1" />
    <lb />geschwüsterige, einandern erben und im fahl die
    <lb />mutter im leben wär, soll die mutter den dritten
    <lb />theil und die geschwüsterte die zwenn theil erben.
    <anchor xml:id="damage1" />
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [8.4.2. Synchronization and Overlap](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TS.html#TSSAPA)
- [16.5. Correspondence and Alignment](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SACS)