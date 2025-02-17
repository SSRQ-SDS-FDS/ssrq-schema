---
title: Page d'accueil
---

# Lignes directrices de transcription et documentation

![SSRQ Logo](ssrq-logo.svg)

Bienvenue sur la page de documentation des sources du droit suisse (SDS)
de la Fondation des sources du droit de la Société suisse des juristes.

Sur cette page, vous trouverez une description détaillée des fondations philologiques,
sur lequel les unités d'édition du SDS sont basées, ainsi qu'une documentation de l'usage
schémas TEI-XML sous la forme d'une « bibliothèque de balises ». Ces pages peuvent donc être une 
introduction sont vus dans la manière de travailler dans les éditions numériques de la Fondation.
En même temps, agissez comme un « rapport éditorial ».

- L'édition numérique du SDS avec tous les fichiers TEI-XML peut être trouvée dans notre portail 
d'édition [Editio](https://editio.ssrq-online.ch/).
- La [collection rétroditisée](https://www.ssrq-sds-fds.ch/online/cantons.html)
contenu les volumes analogues comme OCR-PDF.
- Le [site Web du projet](https://www.ssrq-sds-fds.ch/home/) informe de l'édition actuelle projette 
et donne un aperçu de l'histoire de SDS depuis les années 1890.

## Technologie et standardisation

En raison du changement des médias et des possibilités de l'ère numérique, les éditions de la
SDS en utilisant le langage de balisage extensible (XML) selon les recommandations de l'encodage 
de texte Initiative (TEI) implémentée.

## XML

> L'Extensible Markup Language, généralement appelé XML, « langage de balisage extensible » en 
> français, est un métalangage informatique de balisage générique qui est un sous-ensemble du 
> Standard Generalized Markup Language (SGML)[^2]

L'accent est mis sur un enregistrement structuré des données à XML et non
sur leur grande présentation, comme avec les programmes de bureau communs pour
Le traitement de texte est le cas.

En raison de son extensibilité, XML offre un nombre infini d'opportunités
Pour enregistrer et traiter les données.

## TEI

Par conséquent, la Fondation Legal Source suit les recommandations de l'international
Initiative de codage de texte reconnu (TEI) pour coder votre numérique
Éditions.

> « The Text Encoding Initiative » (TEI) is a consortium which collectively
> develops and maintains a standard for the representation of texts in digital
> form.
> Its chief deliverable is a set of Guidelines which specify encoding methods
> for machine-readable texts, chiefly in the humanities, social sciences and
> linguistics.[^3]

L'avantage des recommandations du TEI est que pour la plupart des phénomènes,
qui se produisent dans l'édition des textes historiques, des définitions et
offrez des suggestions de codage.

D'une part, cela garantit que l'édition individuelle projette
n'ont pas à les modéliser eux-mêmes et en revanche en l'utilisant
des recommandations comparables à de nombreuses éditions.

Cette normalisation permet de garantir que les données créées non seulement pour le
Public, mais aussi facilement accessible à d'autres fins scientifiques
sont.

En même temps, cependant, cela signifie que les recommandations du TEI
sont capturés de sorte qu'ils dans autant de projets possibles à partir de différents
Les sciences peuvent être utilisées.

## Schema

Pour cette raison, les directives du TEI ont été formées aux fins du SSRQ
adapté à vos propres schémas[^4], qui n'est pas seulement
les caractéristiques spéciales des divers textes source, mais aussi la tradition du
La collection prend un compte égal.

Le [schéma complet et compilé](https://schema.ssrq-sds-fds.ch/latest/TEI_Schema.rng) 
peut être téléchargé librement et continué. Son développement est rendu public
peut être visualisé sur la plate-forme [GitHub](https://github.com/SSRQ-SDS-FDS/ssrq-schema), 
il est publié de manière durable sur [Zenodo](https://zenodo.org/records/13379935).

[^2]:
    [Extensible Markup Language]
    (https://fr.wikipedia.org/wiki/Extensible_Markup_Language).
    Voir aussi le site Web du World Wide Web Consortium (W3C) :
    [XML](https://www.w3.org/TR/xml/).
[^3]:
    [TEI](http://www.tei-c.org/index.xml).
[^4]:
    Un schéma XML est la description formelle d'une quantité
    Des documents XML à l'aide d'un langage de schéma. Une telle description
    permet la validation d'un document XML (c'est-à-dire une revue de la question de savoir si
    Un document XML est structuré comme les règles du schéma fournissent)
    et place ainsi l'uniformité des documents XML dans une édition
    sécurisé.
