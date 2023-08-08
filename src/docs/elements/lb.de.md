---
title: lb
---



# `<lb/>` (Zeilenanfang)

## Beschreibung

Beschreibt Beginn einer Zeile.

## Erläuterung

Wird vor jeder Zeile an den Anfang der Zeile gesetzt, auch vor der ersten Zeile des Textes und wenn ein neuer Abschnitt beginnt. Wird auch bei Texten mit nur einer Zeile verwendet. Einrückungen werden nicht berücksichtigt. 

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @break

Zeigt an, ob ein Zeilenumbruch innerhalb eines Wortes vorliegt – auch wenn der Zeilenumbruch mit dem Seitenumbruch zusammenfällt. Bei gedruckten Texten werden analog zu den handschriftlichen Texten Trennstriche mit eben hiermit und Bindestrichen bzw. Ergänzungsstriche mit '-' transkribiert. 

*Mögliche Werte*

- no

### @facs

Ordnet eine Textseite einem Faksimile oder einem faksimilierten Ausschnitt zu. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

## Beispiele

### Beispiel 1

Modellhafte Benutzung – Achtung: immer leerer Tag

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />
</egXML>
               
```

### Beispiel 2

Worttrennung über den Zeilenwechsel

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">geschri<lb break="no" />ben
        </egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)