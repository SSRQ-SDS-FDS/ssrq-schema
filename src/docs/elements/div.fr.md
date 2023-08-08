---
title: div
---



# `<div/>` (division du texte)

## Description

Sections le texte source dans [`<body/>`](body.md)  ou les commentaires dans[`<back/>`](back.md)  avec[`<p/>`](p.md).

## Explication

Les paragraphes originaux ne sont marqués que par [`<p/>`](p.md)  (sans un[`<div/>`](div.md)  supplémentaire). Si l'original est plus articulé ou structuré, vous pouvez utiliser les deux, éventuellement avec[@type](#type). Les sections que l'éditeur insère pour structurer le contenu (texte lisible), en revanche, sont marquées par[`<seg/>`](seg.md). Pour la structuration des formules de clôture, voir les exemples sur la page Formules de clôture.

Dans le cas de paratextes plus longs (introduction, commentaire), les chapitres peuvent être numérotés avec [`<div/>`](div.md)  et[@n](#n)  et, si nécessaire, avec[@type](#type). Voir aussi les explications « Structuration des textes » dans les consignes de transcription SDS.

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)

## Attributs

### @n

Donne un nombre (ou une autre étiquette) pour un élément, qui n'est pas nécessairement unique dans le document TEI.

*Valeurs possibles*

- Chaîne de caractères

### @type

Caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.

*Valeurs possibles*

- part
- chapter
- collection
- section
- subsection

## Exemples

### Exemple 1

Exemple de divisions numérotées dans [`<back/>`](back.md)

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

### Exemple 2

Exemple de division à l'intérieur du [`<body/>`](body.md)

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

## Sections des Guidelines de la TEI

- [4.1. Divisions of the Body](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html#DSDIV)