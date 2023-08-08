---
title: ref
---



# `<ref/>` (Referenz)

## Beschreibung

Enthält einen Verweis.

## Erläuterung

Der Verweis kann auf ein anderes Dokument, die Einleitung, das Register eines retrodigitalisierten Bandes, einen Eintrag im HLS, zitierte Literatur etc. zeigen. Es ist sinnvoll, Links auf weitere, nicht edierte, aber in einem Archivinformationssystem einzeln verzeichnete Quellenstücke innerhalb von [`<ref/>`](ref.md)  zu setzen. Nicht sinnvoll ist es, wenn bei einer einzelnen Urkunde auf den ganzen Urkundenbestand verlinkt wird, weil die Einzelurkunde nicht verzeichnet ist. Bei Einträgen aus einem Buch, die man nicht einzeln in einem Archivinformationssystem verzeichnen will (wenn das überhaupt möglich ist), kann auf das (ganze) Buch, das im Archivkatalog verzeichnet ist, verlinkt werden. Wird auf andere Editionen verlinkt, wird zuerst die Signatur der Quelle angegeben, wenn die Archivalie konsultiert wurde (Autopsie) oder wenn sich die Signatur via Query verifizieren und verlinken lässt. Hat man eine Archivalie anhand einer Edition beurteilt, ist nur die Edition anzugeben. Wenn man auf eine Quelle, die in einer Editionseinheit der SSRQ ediert wird, verweisen möchte, ist es nicht notwendig, die Archivsignatur zu wiederholen, sondern es reicht, auf die Stücknummer der Editionseinheit zu verlinken (vgl. Beispiel unten). Ebenso ist es möglich, innerhalb der eigenen Editionseinheit von einem Stück auf ein anderes zu referenzieren. Wir verwenden dafür die[`<idno/>`](idno.md).

## Inhaltsmodell

- **core**: [hi](hi.md)
- Beliebiger Textinhalt

## Attribute

### @target

Hyperlink, DOI oder interner Verweis.

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `doi:10\.\d{4}/.*`
- anyURI – Einschränkung: regulärer Ausdruck `(https?|ftp)://[^\s/$.?#].[^\s]*`
- Zeichenkette – Einschränkung: regulärer Ausdruck `urn:ssrq:(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)(-((([A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)))?(#[A-Za-z0-9_]+)?`

## Beispiele

### Beispiel 1

Verweis auf gedruckte Quellen

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858">SSRQ SG
                    III/2, Nr. 231
                </ref>
    </bibl>
</egXML>
               
```

### Beispiel 2

Verweis auf anderes Dokument

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <ref target="urn:ssrq:SSRQ-ZH-NF_I_2_1-4-1">SSRQ ZH NF I/2/1 4-1</ref>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [3.7. Simple Links and Cross-References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COXR)
- [16.1. Links](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SAPT)