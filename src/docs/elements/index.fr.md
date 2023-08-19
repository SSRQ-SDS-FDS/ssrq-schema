# Aperçu des balises principales

## Balises de critique textuelle

- [`<abbr/>`](../elements/abbr.fr.md) [`<expan/>`](../elements/expan.fr.md) (abréviation) indique une abréviation.

Pour les abréviations françaises, on consultera avec profit
[[http://theleme.enc.sorbonne.fr/dico]](http://theleme.enc.sorbonne.fr/dico).
Pour les abréviations latines, l'ouvrage de base demeure: Adriano Cappelli, Dizionario de Abbreviature latine ed
italiani, Milan, 1912. Celui-ci est accessible en ligne:
[[http://www.hist.msu.ru/Departments/Medieval/Cappelli/]](http://www.hist.msu.ru/Departments/Medieval/Cappelli/).

- [`<add/>`](../elements/add.fr.md) [`<addSpan/>`](../elements/add.fr.md) (ajout) indique des lettres, des mots ou des
  phrases (ajouts, compléments, éléments suscrits, notes marginales) qui ont été insérés à leur place dans le texte
  édité.
- [`<app/>`](../elements/app.fr.md) (entrée d'apparat critique) indique une différence de lecture ou une variation
  textuelle par rapport à d'éventuels autres états du texte (un deuxième original, une copie).
- [`<corr/>`](../elements/corr.fr.md) (correction) indique la correction (par l'éditeur) d'un mot ou d'un passage, qui,
  dans le texte source, comporte manifestement une erreur (accord, orthographe, sens), et qui pourrait, par ailleurs,
  être assorti du tag [`<sic/>`](../elements/sic.fr.md).
- [`<damage/>`](../elements/damage.fr.md) [`<damageSpan/>`](../elements/damageSpan.fr.md) (dommage) indique la présence et
  la nature d'un dommage à cet endroit du texte source.
- [`<del/>`](../elements/del.fr.md) [`<delSpan/>`](../elements/del.fr.md) (suppression) indique une lettre, un mot ou un
  passage cancellé et/ou une rature.
- [`<foreign/>`](../elements/foreign.fr.md) (étranger) indique la présence d'un mot (ou plusieurs) exprimé(s) dans une
  autre langue que celle du texte source.
- [`<gap/>`](../elements/gap.fr.md) (omission) indique l'omission volontaire par l'éditeur d'un mot ou d'un passage pour
  des raisons éditoriales - qu'il convient alors d'expliquer (échantillonnage ou passage illisible par exemple).
- [`<sic/>`](../elements/sic.fr.md) (sic) indique que l'éditeur a reproduit tel quel un mot ou un passage du texte source,
  mais dont la graphie ou le sens peut paraître étrange ou surprendre le lecteur.
- [`<space/>`](../elements/space.fr.md) (espace) passage volontairement laissé vide (dans le texte source) par le scribe
  (par exemple pour un éventuel complément plus tardif, mais qui ne s'est pas fait).
- [`<subst/>`](../elements/subst.fr.md) (substitution) indique un passage comportant de multiples et complexes ratures,
  corrections, ajouts rendant la lecture et la compréhension difficile, mais que l'éditeur a composé ou recomposé au
  mieux, en fonction d'un choix, qu'il convient d'expliquer.
- [`<supplied/>`](../elements/supplied.fr.md) (texte restitué) indique une ou des explications donnée(s) par l'éditeur pour
  une raison quelconque: par exemple, lorsque celui-ci a dû composer ou recomposer un passage (voir ci-dessus) parce que
  le scribe du texte source a sauté une ligne ou parce que, à cet endroit du texte, le document original comporte un
  trou ou est endommagé.
- [`<unclear/>`](../elements/unclear.fr.md) (incertain) indique une lecture demeurée incertaine (proposition de
  transcription).
- [`<note/>`](../elements/note.fr.md) indique la présence d'une note renvoyant à l'apparat.

## Balises utiles à la présentation de l'édition de texte

- [`<ab/>`](../elements/ab.fr.md) indique la présence d'une zone de texte sans affectation claire au sein du texte source,
  s'agissant de notices dorsales, de remarques issues de la chancellerie, des Archives ou de la Registratur.
- [`<div/>`](../elements/div.fr.md) ou [`<p/>`](../elements/p.fr.md) indique une subdivision dans le texte.
- [`<seg/>`](../elements/seg.fr.md) indique des paragraphes fait par l'éditeur pour structurer le contenu d'un texte.
- [`<figure/>`](../elements/figure.fr.md) indique des éléments représentant ou contenant une information graphique, comme
  le seing manuel d'un notaire, des essais de plume, une croix, un chrismon. Il n'est donc plus nécessaire, pour une
  édition digitale, de faire figurer ces informations dans le texte, comme cela est le cas pour une édition analogique,
  selon ce principe: (Chrismon.) In nomine etc... (avec Chrismon en italique).
- [`<head/>`](../elements/head.fr.md) indique un titre, un sous-titre, etc.
- [`<hi/>`](../elements/hi.fr.md)    lettres suscrites.
- [`<lb/>`](../elements/lb.fr.md)         indique le début d'une nouvelle ligne (saut de ligne).
- [`<orig/>`](../elements/orig.fr.md)              indique un mot ou un passage repris tel quel (littéralement par rapport
  à la langue du
  texte source) dans un commentaire, un titre ou une note de bas de page par exemple.
- [`<pb/>`](../elements/pb.fr.md)     indique le début d'une page de texte (saut de page).
- [`<q/>`](../elements/q.fr.md)               indique un discours direct, introduit et clos par des guillemets.
- [`<quote/>`](../elements/quote.fr.md)             indique une citation.
- [`<signed/>`](../elements/signed.fr.md)            indique une signature.
- [`<table/>`](../elements/table.fr.md) avec [`<row/>`](../elements/row.fr.md) et [`<cell/>`](../elements/cell.fr.md) indique la
  présence d'un tableau (voir ci-dessous).

## Balises de contenu

- [`<date/>`](../elements/date.fr.md)        indique les éléments d'une date.
- [`<origDate/>`](../elements/origDate.fr.md)            indique la date originale exprimée dans le texte source.
- [`<measure/>`](../elements/measure.fr.md)            indique les unités monétaires, de poids et de mesures.
- [`<measureGrp/>`](../elements/measureGrp.fr.md)        indique un groupe de mesures dont la conversion n'est pas
  possible.
- [`<num/>`](../elements/num.fr.md)        indique les chiffres romains, les nombres, etc.
- [`<time/>`](../elements/time.fr.md)        indique un délai ou un moment de la journée par exemple (indication
  temporelle/chronologique).

## Indexation

- [`<persName/>`](../elements/persName.fr.md) personnes
- [`<orgName/>`](../elements/orgName.fr.md) organisations
- [`<placeName/>`](../elements/placeName.fr.md)            lieux, lieux-dits
- [`<origPlace/>`](../elements/origPlace.fr.md)            date de lieu ou date topographique
- [`<term/>`](../elements/term.fr.md)            lemmes, keywords
