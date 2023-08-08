---
title: idno
---



# `<idno/>` (Identifikationsnummer)

## Beschreibung

Enthält im [`<seriesStmt/>`](seriesStmt.md)  eine UUID (mit[@type](#type)  =`UUID` ), das Bandkürzel (Kanton, Teil, Stücknummer) der Sammlung Schweizerischer Rechtsquellen oder enthält im [`<msIdentifier/>`](msIdentifier.md)  die Archivsignatur einer Quelle.

## Erläuterung

Enthält [`<idno/>`](idno.md)  die Signatur eines Archivs hat sich diese nach dem System des jeweiligen Archivs zu richten.

Enthält [`<idno/>`](idno.md)  eine UUID, dann muss diese dem folgenden regulären Ausdruck entsprechen:`^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[4][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$`. Die UUID ist wie folgt aufgebaut: 

- Genau acht Zeichen aus folgendem Set: die Ziffern "0-9", die Grossbuchstaben "A-F" oder die Kleinbuchstaben "a-f". 
- Ein Bindestrich.
- Genau vier Zeichen aus dem oben genannten Set.
- Ein Bindestrich.
- Die Ziffer "4", gefolgt von drei Zeichen aus dem oben genannten Set.
- Ein Bindestrich.
- Genau einmal ein Zeichen aus folgendem Set: "8", "9", "A", "B", "a", "b" gefolgt von genau drei Zeichen aus dem oben genannten Set. 
- Ein Bindestrich.
- Genau zwölf Zeichen aus dem oben genannten Set.

Enthält [`<idno/>`](idno.md)  ein Bandkürzel der SSRQ, dann muss dies dem folgenden regulären Ausdruck entsprechen:`^(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)-(?:((?:[A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)|([a-z]{3,}))$"`. Die Bandkürzel sind wie folgt aufgebaut: 

- Das Präfix "SSRQ" oder "SDS" oder "FDS".
- Ein Bindestrich.
- Das Kürzel des Kantons bestehend aus zwei Grossbuchstaben.
- Ein Bindestrich.
- Ein Kürzel des Bandes bestehend aus beliebig vielen Grossbuchstaben, Kleinbuchstaben, Ziffern und Unterstrichen. 
- Ein Bindestrich.
- Die Kapiteleinteilung des Bandes (optional) bestehend aus beliebig vielen Grossbuchstaben, Kleinbuchstaben, Ziffern und Punkten. 
- Ein Kürzel des Stücks bestehend aus beliebig vielen Ziffern.
- Ein Bindestrich.
- Eine abschliessende Kennung bestehend entweder aus beliebig vielen Ziffern oder mindestens drei Kleinbuchstaben (z. B. zur Bennenung einnes speziellen Stücks wie "lit", "intro" oder "bailiff"). 

## Inhaltsmodell

- Beliebiger Textinhalt

## Attribute

### @source

Verweis auf ein anderes Stück (bspw. im Falle der Mehrfachüberlieferung) oder auf ein Archivinformationssystem. 

*Mögliche Werte*

- anyURI – Einschränkung: regulärer Ausdruck `(https?|ftp)://[^\s/$.?#].[^\s]*`

### @type



*Mögliche Werte*

- uuid – *Universally Unique Identifier*

### @xml:lang

ISO-639-1-Sprachkürzel

*Mögliche Werte*

- de – *Deutsch*
- fr – *Französisch*
- he – *Hebräisch*
- it – *Italienisch*
- la – *Latein*
- rm – *Bündnerromanisch*

## Beispiele

### Beispiel 1

Definition der Identifikationsnummer eines Stücks:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seriesStmt>
        <title>Sammlung Schweizerischer Rechtsquellen</title>
        <respStmt>
            <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
            <resp>Herausgabe</resp>
        </respStmt>
        <idno>SSRQ-FR-I_2_8-1-1</idno>
        <idno type="uuid">ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
    </seriesStmt>
</egXML>
               
```

### Beispiel 2

Verweis auf eine Signatur mit Link ins Archivinformationssystem:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <idno xml:lang="de" source="http://scope.stiftsarchiv.sg.ch/detail.aspx?id=30146">StiASG Urk. GG2 T2
                </idno>
    </msIdentifier>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [13.3.1. Basic Principles](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPERSbp)
- [2.2.4. Publication, Distribution, Licensing, etc.](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD24)
- [2.2.5. The Series Statement](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD26)
- [3.12.2.4. Imprint, Size of a Document, and Reprint Information](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COBICOI)