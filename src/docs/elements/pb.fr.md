---
title: pb
---



# `<pb/>` (début de page)

## Description

Décrit le début d'une page dans l'original.

## Explication

 [`<pb/>`](pb.md)  est répertorié en haut de la page et contient généralement la foliation [par ex. n="109v"] ou la pagination [par ex. n="22"] dans[@n](#n). Une pagination originale ou une foliation originale est marquée par[@type](#type)  =`original`. Dans le cas d'une source avec feuille d'origine, le verso est également marqué avec [@type](#type)  =`original`. 

Si un texte source ne fait qu'une page (par exemple, un certificat), [`<pb/>`](pb.md)  n'est requis que pour le lien vers les facsimilés. Si un texte s'étend sur le recto et le verso d'une seule feuille (2 pages),[`<pb/>`](pb.md)  est défini sans attributs sur la première et la deuxième page. Les pages de trois ou plus sont numérotées avec[@n](#n). Sur un toboggan, le changement de côté est noté à l'endroit où un nouveau morceau de parchemin a été cousu. S'il y a plusieurs pages de titre ou pages de garde avant le début du contenu proprement dit et la pagination proprement dite, il est conseillé de numéroter les pages[@n](#n)  avec des chiffres romains + (I, II, III, IV etc.), comme il est d'usage pour les manuscrits. Lors de l'impression, le comptage des feuilles (foliation) commence par la feuille de titre. La page de titre n'est pas spécialement marquée. Un numéro de page ou de feuille existant est adopté et fourni avec[@type](#type)  =`original`. Les feuilles blanches ou les pages blanches sont comptées. S'il n'y a pas de numéro de page d'origine, un numéro de page est introduit. Les signatures de feuille ne sont pas transcrites. 

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @facs

Associe une page de texte à un fac-similé ou à un extrait de fac-similé. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

### @n

Spécification de la pagination originale, de la foliation ou de la numérotation des sections. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `((\d+)|([IVXLC]+))[rv]`
- Chaîne de caractères – Restriction: expression régulière `(\d+)|([IVXLC]+)`
- Chaîne de caractères – Restriction: expression régulière `s(\d+)`

### @type

Type d'appendice latéral

*Valeurs possibles*

- original – *Saut de page original*

### @xml:id

Fournit un identifiant unique pour l'élément qui porte l'attribut

*Valeurs possibles*

- Identificateur

## Exemples

### Exemple 1

Exemple pour des folios originaux:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="1r" type="original" />
    <lb />
</egXML>
               
```

### Exemple 2

ATTENTION: Ces parties de mot suivent directement, sans espace ou touche entrée/return:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
            geschri
            <pb />
    <lb break="no" />ben
        </egXML>
               
```

### Exemple 3

Pagination de plusieurs pages de titre ou pages de garde avec des chiffres romains:

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <pb n="Ir" />
    <head>Urbar oder libell der
                <orgName>burgern zue
                    <placeName>Werdenberg</placeName>
        </orgName>
                er, vidimiert und
                renoviert anno salutis
                <origDate when="1640">1640</origDate>
    </head>
    <pb n="1" />
    <p>
        <lb />Ich, <persName>Jacob Felldtmann</persName>, der junger, der zeith der hochgeachten
                woledlen gestrengen frommen ehren
                ...
            </p>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)