---
title: pb
---



# `<pb/>` (Seitenanfang)

## Beschreibung

Beschreibt einen Seitenanfang im Original.

## Erläuterung

 [`<pb/>`](pb.md)  wird am Anfang der Seite aufgeführt und enthält in der Regel die Foliierung [z. B. n="109v"] oder Paginierung [z. B. n="22"] in[@n](#n). Eine Originalpaginierung oder Originalfoliierung wird mit[@type](#type)  =`original`  gekennzeichnet. Es wird bei einer Quelle mit Originalfoliierung auch die Versoseite mit [@type](#type)  =`original`  ausgezeichnet. 

Wenn ein Quellentext lediglich eine Seite umfasst (z. B. Urkunde), wird [`<pb/>`](pb.md)  nur fürs Verlinken mit den Faksimiles benötigt. Wenn ein Text über Vorderseite und Rückseite eines Einzelblatts verläuft (2 Seiten), wird[`<pb/>`](pb.md)  ohne Attribute auf der ersten und zweiten Seite gesetzt. Ab drei Seiten wird mit[@n](#n)  nummeriert. Bei einem Rodel wird an der Stelle, an der ein neues Pergament angenäht wurde, der Seitenwechsel angemerkt. Bei mehreren Titelblättern oder Vorsatzblätter vor Beginn des eigentlichen Inhalts und der eigentlichen Paginierung empfiehlt sich eine Blattzählung[@n](#n)  mit römischen +Ziffern (I, II, III, IV etc.), wie bei Handschriften üblich. Bei Drucken beginnt die Blattzählung (Foliierung) mit dem Titelblatt. Das Titelblatt wird nicht speziell ausgezeichnet. Eine vorhandene Seiten- oder Blattzählung wird übernommen und mit[@type](#type)  =`original`  versehen. Leere Blätter oder leere Seiten werden mitgezählt. Besteht keine originale Seitenzählung, wird eine Blattzählung eingeführt. Bogensignaturen werden nicht transkribiert. 

## Inhaltsmodell

Enhält keine Elemente oder Text.

## Attribute

### @facs

Ordnet eine Textseite einem Faksimile oder einem faksimilierten Ausschnitt zu. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

### @n

Angabe der originalen Paginierung, Foliierung oder Abschnittszählung. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `((\d+)|([IVXLC]+))[rv]`
- Zeichenkette – Einschränkung: regulärer Ausdruck `(\d+)|([IVXLC]+)`
- Zeichenkette – Einschränkung: regulärer Ausdruck `s(\d+)`

### @type

Typ des Seitenfangs

*Mögliche Werte*

- original – *Originalseitenwechsel*

### @xml:id



*Mögliche Werte*

- Identifikator

## Beispiele

### Beispiel 1

Beispiel für eine Originalfoliierung:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="1r" type="original" />
    <lb />
</egXML>
               
```

### Beispiel 2

ACHTUNG: Wortteile ohne Leerschlag oder Drücken der Return- oder Eingabetaste direkt nach anhängen:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            geschri
            <pb />
    <lb break="no" />ben
        </egXML>
               
```

### Beispiel 3

Blattzählung von Vorsatz- und Titelblättern mit römischen Ziffern:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="Ir" />
    <head>Urbar oder libell der
                <orgName>burgern zue
                    <placeName>Werdenberg</placeName>
        </orgName>
                er, vidimiert und
                renoviert anno salutis
                <origDate when="1640">1640</origDate>
    </head>
    <pb n="1" />
    <p>
        <lb />Ich, <persName>Jacob Felldtmann</persName>, der junger, der zeith der hochgeachten
                woledlen gestrengen frommen ehren
                ...
            </p>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)