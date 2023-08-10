---
title: back
---



# `<back/>` (Rubrique commentaire)

## Description

Le commentaire contient des informations complémentaires sur une pièce éditée, place la pièce dans son contexte historique et donne des informations sur les raisons pour lesquelles une pièce a été choisie pour l'édition. 

## Explication

Plusieurs commentaires peuvent être structurés avec [`<div/>`](div.md). La littérature (RI-Opac-Shorttitle) et les liens Internet (par exemple, les pièces d'archives répertoriées, etc.) peuvent être référencés avec des éléments[`<ref/>`](ref.md). Dans le commentaire, les personnes, les lieux et les institutions qui doivent être trouvés via la recherche d'index seront marqués. D'autres balises telles que[`<date/>`](date.md)  ou[`<measure/>`](measure.md)  sont omises, d'autant plus qu'elles peuvent facilement être automatiquement étiquetées ultérieurement dans leur forme actuelle et normalisée.

## Modèle de contenu

- **textstructure**: [div](div.md)

## Exemples

### Exemple 1

Exemple d'une section de commentaires avec deux divisions

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

## Sections des Guidelines de la TEI

- [4.7. Back Matter](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSBACK)
- [4. Default Text Structure](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DS)