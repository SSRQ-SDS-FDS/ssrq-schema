---
title: lb
---



# `<lb/>` (début de ligne)

## Description

Décrit le début d'une ligne.

## Explication

Placé au début de la ligne avant chaque ligne, y compris avant la première ligne de texte et au début d'un nouveau paragraphe. Également utilisé pour les textes d'une seule ligne. Les indentations sont ignorées. 

## Modèle de contenu

Ne contient aucun élément ou texte.

## Attributs

### @break

Indique s'il y a un saut de ligne dans un mot - même si le saut de ligne coïncide avec le saut de page. Dans les textes imprimés, les traits d'union sont transcrits avec juste ici et les traits d'union ou tirets supplémentaires avec '-', analogues aux textes manuscrits. 

*Valeurs possibles*

- no

### @facs

Associe une page de texte à un fac-similé ou à un extrait de fac-similé. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

## Exemples

### Exemple 1

Utilisation comme modèle - Attention: jour toujours vide

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <lb />
</egXML>
               
```

### Exemple 2

Séparation des mots via le saut de ligne

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">geschri<lb break="no" />ben
        </egXML>
               
```

## Sections des Guidelines de la TEI

- [3.11.3. Milestone Elements](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CORS5)
- [7.2.5. Speech Contents](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DR.html#DRPAL)