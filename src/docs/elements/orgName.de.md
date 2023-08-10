---
title: orgName
---



# `<orgName/>`

## Beschreibung

Zeichnet eine Organisation bzw. Institution, wie Klöster, Zünfte, Räte, Nachbarschaft etc., aus. 

## Erläuterung

Innerhalb der Sammlung Schweizerischer Rechtsquellen werden folgende Entitäten als Organisationen gekennzeichnet: 

- Bevölkerungsgruppe (z.B. Juden)
- Bruderschaft
- Bürgermeister und Rat
- Bürgerschaft
- Eidgenossenschaft bzw. Gruppe von eidgenössischen Orten (z.B. VII Orte) (wenn es sich nicht um den Ort, sondern die Organisation handelt) 
- Eigentümerschaft
- Familie (z.B. die Grafen von Toggenburg, die Herren von Landenberg)
- Heiligenverband/Heiligengruppe (z.B. Zehntausend Ritter, Elftausend Jungfrauen, Peter und Paul) 
- Herrschaftsverband
- Kirchgenossenschaft/Pfarrei (Achtung: eine Kirchhöre oder ein Kirchspiel kann auch eine Ortsbezeichnung sein) 
- Klosterkonvent; hier: Konvent (Achtung: ein Kloster kann auch eine Ortsbezeichnung sein) 
- Knabenschaft
- Kommission (z. B. Baukommission etc.)
- Handelsgesellschaft
- Nachbarschaft
- Nutzungsgemeinschaft
- Orden
- Rat
- Schützengesellschaft
- Stiftung
- Steuergenossenschaft
- Zunft

Der Herausgeber der Reihe, hier immer die Rechtsquellenstiftung, wird im [`<respStmt/>`](respStmt.md)  mit[`<orgName/>`](orgName.md)  ausgezeichnet.

## Inhaltsmodell

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Beliebiger Textinhalt

## Attribute

### @ref

Verknüpfung der Organisation mit der ID der Personen- und Organisationsdatenbank. 

*Mögliche Werte*

- Zeichenkette – Einschränkung: regulärer Ausdruck `org\d{6}(\.\d{2})?`

### @role

Auszeichnung der Rolle einer Institution im Quellentext. 

*Mögliche Werte*

- issuer – *Aussteller*
- recipient – *Empfänger*
- sigillant – *Siegelinhaber*
- testis – *Zeuge*

## Beispiele

### Beispiel 1

Als Organisation werden stets die Instituionen / Funktionen gekennzeichnet – jedoch nicht die Personen. Dies gilt, wie nachfolgend zeigt, auch für die namentliche Nennung des Bürgermeisters.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    presentibus
    <lb />herr <persName ref="per001921">Bernhart von Chaam</persName>,
    <orgName ref="org002406">burgermeister, und beid
        <lb />räth
    </orgName>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [13.2.2. Organizational Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDORG)