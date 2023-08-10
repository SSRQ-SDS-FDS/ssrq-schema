---
title: settlement
---



# `<settlement/>` (lieu de peuplement)

## Description

Saisie d'un nom d'établissement (localisation des archives) au sein de [`<msIdentifier/>`](msIdentifier.md).

## Modèle de contenu

- Contenu de texte au choix

## Attributs

### @ref

Relier le lieu à l'ID de la base de données des lieux. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `loc\d{6}(\.\d{2})?`

## Exemples

### Exemple 1

Exemple de saisie du nom de la ville d'une archive

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <msIdentifier>
        <repository xml:lang="fr">Archives de l’État de
                    <settlement ref="loc000284">Fribourg</settlement>
        </repository>
        <idno xml:lang="de">StAFR, Thurnrodel 2, fol. 15r–16v</idno>
    </msIdentifier>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [13.2.3. Place Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDPLAC)