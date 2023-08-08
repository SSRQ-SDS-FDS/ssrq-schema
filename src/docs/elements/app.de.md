---
title: app
---



# `<app/>`

## Beschreibung

Enthält einen Apparateintrag.

## Erläuterung

Ermöglicht verschiedene Lesarten eines Wortes oder eines Textabschnittes anzuzeigen unter Bezugnahme auf ein anderes Dokument oder mehrere andere Dokumente. Muss sich unmittelbar, ohne Leerschlag, an das Wort anschliessen. 

Existieren von einem Stück mehrere Textzeugen (Originale, Kopien) kann bei einer Fehlstelle der andere Textzeuge hinzugezogen werden. Inhaltliche Abweichungen der anderen Originale oder Abschriften von der Editionsvorlage müssen zwingend angemerkt werden. Ebenso lassen sich bei zwei Originalen hiermit die Abweichungen auszeichnen, sodass nicht beide Versionen transkribiert werden müssen. 

Bei kurzen Nachträgen, z. B. einem halben Satz, kann man sich mit einem leeren [`<lem/>`](lem.md)  behelfen (vgl. Beispiel unten). Bei längeren Nachträgen oder Zusätzen aus anderen Textzeugen empfiehlt es sich indessen, ein eigenes Stück dafür zu erstellen. Die bereits edierten Texte eines früheren Textzeugen können mit[`<gap/>`](gap.md)  weggelassen werden. Es muss jedoch mit[@source](#source)  auf den edierten Text, der weggelassen wird, referenziert werden. Eine Bemerkung (Kommentar in[`<back/>`](back.md) ) ist notwendig. Ein leeres[`<lem/>`](lem.md)  kann auch verwendet werden, wenn bei einem Original ein Wort oder Satzteil weggelassen wurde, der in einem Entwurf noch gewesen enthalten ist.

Wenn eine Zweitausfertigung oder Abschrift eine signifikante Auslassung aufweist (dass also ein Wort oder Satzteil weggelassen wurde), so kann dafür ein leeres [`<rdg/>`](rdg.md)  gesetzt werden (vgl. Beispiel unten). Für alternative Lesungen aus anderen Editionen bzw. moderner Literatur verwendet man hingegen[`<note/>`](note.md)  mit[`<quote/>`](quote.md). Abweichungen der Transkription von bereits edierten Quellenstücken werden in der Regel nicht angegeben. Wenn die Neuedition sich in einem inhaltlichen Punkt bzw. einer Lesung wesentlich unterscheidet, ist eine[`<note/>`](note.md)  notwendig. Abweichungen der Schreibung eines weiteren Originals oder Abschriften sind ebenfalls nur anzumerken, wenn sie weitere Erkenntnisse liefern.

Bei mehreren vorhandenen Originalen sollten wenn möglich die Kriterien, die zur Wahl der Editionsvorlage beitrugen, in einem Kommentar in [`<back/>`](back.md)  dargelegt werden. Dasselbe gilt im Falle von Abschriften. Achtung: Reverse gelten als eigenständige Überlieferung.

Wenn eine Stelle eines Originals wegen einer Beschädigung nicht mehr lesbar ist, kann der Textverlust mit Hilfe eines anderen Textzeugen ergänzt werden. Dafür verwenden wir nicht [`<app/>`](app.md)  und[`<rdg/>`](rdg.md), sondern[`<damage/>`](damage.md)  zusammen mit[`<supplied/>`](supplied.md).

## Inhaltsmodell

- **textcrit**: [lem](lem.md) [rdg](rdg.md)

## Beispiele

### Beispiel 1

Beispiel für einen Apparateintrag

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <app>
        <lem>lxxxvij</lem>
        <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810e">
            quadringentesimo
        </rdg>
        <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810f">lxxxiiij</rdg>
    </app>
</egXML>
               
```

## Abschnitte in den Guidelines der TEI

- [12.1.1. The Apparatus Entry](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TCAPEN)