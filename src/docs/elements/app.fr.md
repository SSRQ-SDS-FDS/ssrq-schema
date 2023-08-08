---
title: app
---



# `<app/>` (entrée d'apparat critique)

## Description

Contient une entrée d'appareil.

## Explication

Permet d'afficher différentes lectures d'un mot ou d'un passage de texte en référence à un ou plusieurs autres documents. Doit suivre immédiatement le mot sans espaces. 

S'il existe plusieurs témoins de texte (originaux, copies) d'un morceau, l'autre témoin de texte peut être consulté en cas de lacune. Les écarts de contenu des autres originaux ou copies par rapport au modèle d'édition doivent être notés. Les écarts peuvent également être marqués avec deux originaux, de sorte que les deux versions ne doivent pas être transcrites. 

Pour les suppléments courts, par ex. B. une demi-phrase, vous pouvez vous débrouiller avec un [`<lem/>`](lem.md)  vide (voir exemple ci-dessous). Dans le cas de suppléments plus longs ou d'ajouts provenant d'autres sources textuelles, il est toutefois conseillé de créer une pièce distincte pour eux. Les textes déjà édités d'un témoin de texte antérieur peuvent être omis avec[`<gap/>`](gap.md). Cependant, il doit être référencé avec[@source](#source)  au texte édité qui est omis. Une remarque (commentaire en[`<back/>`](back.md) ) est requise. Un[`<lem/>`](lem.md)  vide peut également être utilisé lorsqu'un original a omis un mot ou une phrase qui était inclus dans un brouillon.

Si un doublon ou une transcription comporte une omission importante (c'est-à-dire qu'un mot ou une phrase a été omis), un [`<rdg/>`](rdg.md)  vide peut être remplacé (voir l'exemple ci-dessous). Pour les lectures alternatives d'autres éditions ou de la littérature moderne, en revanche,[`<note/>`](note.md)  avec[`<quote/>`](quote.md)  est utilisé. En règle générale, les écarts de transcription par rapport aux pièces sources déjà éditées ne sont pas signalés. Si la nouvelle édition diffère sensiblement en termes de contenu ou de lecture, une[`<note/>`](note.md)  est requise. Les écarts dans l'orthographe d'un autre original ou de copies ne doivent également être notés que s'ils fournissent des informations supplémentaires.

S'il existe plusieurs originaux, les critères ayant contribué au choix du modèle d'édition doivent être précisés dans un commentaire en [`<back/>`](back.md)  si possible. Il en va de même pour les copies. Attention: les revers sont considérés comme des traditions indépendantes.

Si une partie d'un original n'est plus lisible en raison d'un dommage, la perte de texte peut être complétée à l'aide d'un autre témoin de texte. Au lieu d'utiliser [`<app/>`](app.md)  et[`<rdg/>`](rdg.md), nous utilisons[`<damage/>`](damage.md)  avec[`<supplied/>`](supplied.md).

## Modèle de contenu

- **textcrit**: [lem](lem.md) [rdg](rdg.md)

## Exemples

### Exemple 1

Exemple d'entrée d'appareil

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

## Sections des Guidelines de la TEI

- [12.1.1. The Apparatus Entry](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/TC.html#TCAPEN)