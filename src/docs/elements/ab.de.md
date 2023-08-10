---
title: ab
---



# `<ab/>` (Anonymer Textblock)

## Beschreibung

Enthält eine beliebige Textebene ohne klar definierte Zuordnung.

## Erläuterung

Wir verwenden den Tag immer zusammen mit [@type](#type)  und[@place](#place)  für Vermerke, Dorsualnotizen, Kanzleivermerke und Registraturvermerke sowie für Marginalien.

Bei Papsturkunden erfolgt die Angabe der Vermerke in folgender Reihenfolge: Zuerst die Vermerke unter der Plica, dann die Vermerke auf der Plica von links nach rechts und zum Schluss die Vermerke auf der Rückseite der Urkunde von links nach rechts. 

Die Vermerke und Dorsualnotizen werden in chronologischer Reihenfolge aufgenommen. Zeitgleich entstandene Vermerke werden aufgrund der chronologischen Reihenfolge immer an erster Stelle aufgeführt. Zeitgleiche Vermerke werden in Leserichtung von oben nach unten und von links nach rechts erfasst. Wenn z. B. bei einem Missiv auf der Rückseite ein Dorsualvermerk an erster Stelle steht, dann die Adresse folgt und schliesslich zwei weitere Dorsualvermerke, dann steht die Adresse trotzdem an erster Stelle. Falls die Leserichtung, an der man sich orientieren soll, nicht einheitlich ist, also ein Dorsualvermerk auf den Kopf steht, ist ein Kommentar notwendig. 

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

### @hand

Enthält einen Verweis auf die ID eines [`<handNote/>`](handNote.md)-Element, das im[`<teiHeader/>`](teiHeader.md)  deklariert wurde.

*Mögliche Werte*

- Verweis auf Identifikator

### @place

Ort einer Dorsualnotiz, eines Vermerks, eines Registraturvermerks oder eines Kanzleivermerks 

*Mögliche Werte*

- above – *oberhalb der Zeile*
- below – *unterhalb der Zeile*
- bottom – *am unteren Rand*
- cover – *auf dem Umschlag*
- cover_above – *auf dem Umschlag oben*
- cover_bottom – *auf dem Umschlag unten*
- cover_middle – *auf dem Umschlag in der Mitte*
- left_margin – *am linken Rand*
- next_page – *auf der nächsten Seite*
- right_margin – *am rechten Rand*
- verso – *auf der Rückseite*
- left_plica – *auf der linken Seite der Plica*
- parchment_tag – *auf dem Pergamentstreifen*
- plica – *auf der Plica*
- plica_verso – *auf der Rückseite der Plica*
- right_plica – *auf der rechten Seite der Plica*
- sub_plica – *unter der Plica*
- verso_above – *auf der Rückseite oben*
- verso_above_left – *auf der Rückseite oben links*
- verso_above_middle – *auf der Rückseite oben in der Mitte*
- verso_above_right – *auf der Rückseite oben rechts*
- verso_bottom – *auf der Rückseite unten*
- verso_bottom_left – *auf der Rückseite unten links*
- verso_bottom_middle – *auf der Rückseite unten in der Mitte*
- verso_bottom_right – *auf der Rückseite unten rechts*
- verso_middle – *auf der Rückseite in der Mitte*

### @type

Klassifikation des Elements

*Mögliche Werte*

- address – *Anschrift*
- archiving_reference – *Registraturvermerk*
- chancery_notation – *Kanzleivermerk*
- computatio – *Komputierungsvermerk*
- dorsal – *Vermerk*
- marginal_note – *Marginalie*
- sigillant – *Sieglervermerk*
- tax – *Taxvermerk*

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

Beispiel für einen Kanzleivermerk

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <ab type="chancery_notation" place="right_plica" xml:lang="la">
        Ad mandatum domini regis
        <persName>Ulricus de Albeck</persName>
        <note>Ulrich von Albeck (1431 gestorben, ab 1401 Angehöriger der Kanzlei
            König Ruprechts, später Bischof), vgl. Ruoff, Hochgerichtsbarkeit, S. 365.
        </note>
        decretorum doctor.
    </ab>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [16.3. Blocks, Segments, and Anchors](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SASE)