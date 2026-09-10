---
title: Page d’accueil
---

# Directives de transcription et documentation

![SSRQ Logo](ssrq-logo.svg)

Bienvenue sur la page de documentation des sources du droit suisse (SDS)
de la Fondation des sources du droit de la Société suisse des juristes.

Sur cette page, vous trouverez une description détaillée des bases philologiques,
sur lesquelles les unités d’édition des SDS sont basées, ainsi qu’une documentation
relative à l’usage des schémas TEI-XML sous la forme d’une « bibliothèque de balises ».
Ces pages peuvent ainsi servir d’introduction à la méthode de travail des éditions
numériques de la Fondation et font également office de « rapport éditorial ».

- Les éditions numériques des SDS, avec toutes les données au format TEI-XML,
  sont accessibles sur notre portail d’édition [Editio](https://editio.ssrq-online.ch/).
- La [collection rétronumérisée](https://www.ssrq-sds-fds.ch/online/cantons.html) donne accès aux volumes parus sous forme imprimée,
  disponibles en PDF-OCR.
- Le [site Web du projet](https://ssrq-sds-fds.ch/) réunit des informations sur les éditions en cours et
  donne un aperçu de l’histoire de la collection depuis les années 1890.

## Technologie et standardisation

En raison des changements de médias et des possibilités de l’ère numérique,
les éditions des SDS utilisent le langage XML (*Extensible Markup Language*),
conformément aux recommandations de la TEI (*Text Encoding Initiative*).

## XML

> L’Extensible Markup Language, généralement appelé XML, « langage de balisage extensible »
> en français, est un métalangage informatique de balisage conçu pour représenter les
> données de manière hiérarchique sous forme de texte.
> XML est notamment utilisé pour l’échange de données entre systèmes informatiques,
> en particulier via Internet.[^2]

L’objectif de XML est la structuration des données, et non leur présentation graphique,
à la différence des logiciels de traitement de texte classiques.

Grâce à sa souplesse, XML offre un nombre infini d’opportunités pour saisir et
exploiter les données.

## TEI

C’est pourquoi la Fondation des sources du droit suit les recommandations de la
Text Encoding Initiative (TEI), une organisation internationale reconnue, pour
l’encodage de ses éditions numériques.

> « The Text Encoding Initiative » (TEI) is a consortium which collectively
> develops and maintains a standard for the representation of texts in digital
> form.
> Its chief deliverable is a set of Guidelines which specify encoding methods
> for machine-readable texts, chiefly in the humanities, social sciences and
> linguistics.[^3]

L’avantage des recommandations de la TEI est qu’elle propose des définitions et des solutions
d’encodage pour la plupart des phénomènes que l’on peut rencontrer dans l’édition de textes
historiques.

Cela permet d’éviter d’avoir à modéliser individuellement ces phénomènes à chaque nouveau projet,
tout en assurant de pouvoir comparer entre de nombreuses éditions.

Cette standardisation rend les données produites facilement accessibles, tant pour le grand
public que pour la recherche scientifique.

Mais cela implique également que les recommandations de la TEI soient larges,
afin de pouvoir être appliquées au plus grand nombre de projets possible dans
différentes disciplines.

## Schéma

Pour cette raison, les directives du TEI ont été adaptées aux besoins spécifiques
de la SDS dans un schéma propre[^4], en constante évolution, qui prend en compte la
diversité des textes sources et la tradition éditoriale propre à la collection.

Le [schéma complet et compilé](https://schema.ssrq-sds-fds.ch/latest/TEI_Schema.rng) peut être téléchargé librement et réutilisé.
Son développement est consultable sur la plate-forme [GitHub](https://github.com/SSRQ-SDS-FDS/ssrq-schema) et est publié
de manière durable sur [Zenodo](https://zenodo.org/records/13379935).

[^2]:
    [Extensible Markup Language]
    (https://fr.wikipedia.org/wiki/Extensible_Markup_Language).
    Voir aussi le site Web du World Wide Web Consortium (W3C) :
    [XML](https://www.w3.org/TR/xml/).
[^3]:
    [TEI](https://tei-c.org/).
[^4]:
    Un schéma XML est la description formelle d’un ensemble de documents XML
    à l’aide d’un langage de schéma. Une telle description permet la validation
    d’un document XML (c’est-à-dire vérifier s’il est conforme aux règles du schéma)
    garantissant l’homogénéité des données au sein de l’édition.
