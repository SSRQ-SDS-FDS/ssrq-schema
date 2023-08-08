---
title: div
---



# `<div/>` (Textabschnitt)

## Beschreibung

Gliedert Quellentexte innerhalb von [`<body/>`](body.md)  oder Bemerkungen innnerhalb von[`<back/>`](back.md)  zusammen mit[`<p/>`](p.md)  in Abschnitte.

## Erläuterung

Originale Absätze werden nur mit [`<p/>`](p.md)  (ohne zusätzliches[`<div/>`](div.md) ) gekennzeichnet. Sofern das Original stärker gegliedert oder strukturiert ist, kann man beides verwenden, gegebenenfalls zusammen mit[@type](#type). Abschnitte, die der Bearbeitende zur inhaltlichen Strukturierung (lesbarer Text) einfügt, werden hingegen mit[`<seg/>`](seg.md)  ausgezeichnet. Zur Strukturierung von Schlussformeln vgl. die Beispiele auf der Seite Schlussformeln.

Bei längeren Paratexten (Einleitung, Kommentar) können Kapitel durch [`<div/>`](div.md)  mit[@n](#n)  nummeriert und gegebenenfalls mit[@type](#type)  näher bezeichnet werden. Vgl. dazu auch die Ausführungen "Strukturierung der Texte" in den SSRQ-Transkriptionsrichtlinien.

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)

## Attribute

### @n



*Mögliche Werte*

- Zeichenkette

### @type



*Mögliche Werte*

- part
- chapter
- collection
- section
- subsection

## Beispiele

### Beispiel 1

Beispiel für nummerierte Abschnitte innerhalb von [`<back/>`](back.md)

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

### Beispiel 2

Beispiel für einen Abschnitt innerhalb von [`<body/>`](body.md)

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <div>
        <pb n="23" facs="STAW_B_2_a_1_II_23" />
        <p>
            <lb />Item dehein fleischß ze koffen, da der sterbet
        <lb />des vehs ist, da die weiden zuͦ samen stoßent,
        <lb />da daz vaͤch zuͦ samen gaut,
        <lb />
            <del>und</del> die wil und der gebraͤst waͤret
        <lb />und <date dur-iso="P2M">zwen manot</date> dar nach.
    </p>
        <p>
            <lb />Item dehein kalb koffen noch
        <lb />metzgen, es sye denn <measure type="age" unit="week" quantity="3">dry wochen</measure>
            <lb />alt oder elter.
    </p>
        <p>
            <lb />Item si sont oͧch dehein beynnbrüchel
        <lb />in der metzt <add place="above">nit</add> verkoffen denn under
        <lb />den toren, alz daz von alter her
        <lb />komen ist.
    </p>
    </div>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [4.1. Divisions of the Body](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSDIV)