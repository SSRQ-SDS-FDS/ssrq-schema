---
title: back
---



# `<back/>` (Kommentarbereich)

## Beschreibung

Der Kommentar enthält weiterführende Informationen zu einem edierten Quellenstück, ordnet das Stück historisch ein und gibt Auskunft, warum ein Stück für die Edition ausgewählt wurde. 

## Erläuterung

Mehrere Bemerkungen lassen sich mit [`<div/>`](div.md)  strukturieren. Mit[`<ref/>`](ref.md)-Elementen lassen sich Literatur (RI-Opac-Shorttitle) und Internetlinks (z. B. verzeichnete Archivstücke etc.) referenzieren. Im Kommentar werden sicher Personen, Orte und Institutionen ausgezeichnet, die über die Registersuche gefunden werden sollten. Weitere Auszeichnungen wie[`<date/>`](date.md)  oder[`<measure/>`](measure.md)  werden weglassen, zumal diese in heutiger, standardisierter Form leicht nachträglich automatisch getaggt werden können.

## Inhaltsmodell

- **textstructure**: [div](div.md)

## Beispiele

### Beispiel 1

Beispiel für einen Kommentarbereich mit zwei Abschnitten

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <back>
        <div n="1">
            <p>Zum Verkauf der Burg <placeName ref="loc007559.01">Wildenburg</placeName> sowie zu den
                nachfolgenden Verkäufen an die Grafen
                <orgName ref="org000144">von Toggenburg</orgName>
                vgl. den Kommentar zum edierten Stück
                <bibl>
                    <ref target="http://permalink.snl.ch/bib/chbsg000056393">ChSG</ref>,
                    <ref target="http://monasterium.net/mom/CH-StiASG/Urkunden/CC.2.B.1/charter">Bd. 5,
                        Nr. 2839
                    </ref>
                </bibl>
                sowie
                <bibl>
                    <ref target="http://permalink.snl.ch/bib/chbsg000118351">Gabathuler
                        2009c</ref>, S. 235–239
                </bibl>
                .
            </p>
        </div>
        <div n="2">
            <p>Zum Verkauf von Boden durch die Hohensaxer an die <orgName ref="org000425">Appenzeller
            </orgName> in der <placeName ref="loc007565">Saxerlücke</placeName>,
                der einzigen direkten Verbindung zwischen der Freiherrschaft Sax-Hohensax und Appenzell,
                zum Bau einer Letzi am <date datingMethod="julian" when-custom="1346-01-20">20. Januar 1346</date> (vgl.
                <bibl>
                    <ref target="http://permalink.snl.ch/bib/chbsg000080293">Deplazes-Haefliger 1976</ref>,
                    S. 10
                </bibl>
                , gedruckt in
                <bibl>
                    <ref target="http://permalink.snl.ch/bib/chbsg000056393">ChSG</ref>,
                    <ref target="http://monasterium.net/mom/CSGVI/1346_I_20.1/charter">Bd. 6,
                        Nr. 3966
                    </ref>
                </bibl>
                ).
            </p>
        </div>
    </back>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4.7. Back Matter](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSBACK)
- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)