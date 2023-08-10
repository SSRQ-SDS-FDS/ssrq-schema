---
title: choice
---



# `<choice/>` (choix)

## Description

Contient deux éléments pour le marquage alternatif d'un passage de texte. 

## Explication

La balise contient des éléments permettant de décomposer les abréviations ou de corriger les fautes d'orthographe. La résolution de l'abréviation et les corrections sont données après le texte original. 

## Modèle de contenu

- **core**: [abbr](abbr.md) [corr](corr.md) [expan](expan.md) [sic](sic.md)

## Exemples

### Exemple 1

Exemple d'abréviation

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <abbr>sabbo</abbr>
        <expan>sabbato</expan>
    </choice>
</egXML>
               
```

### Exemple 2

Exemple de correction

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <choice>
        <sic>offensiche</sic>
        <corr resp="anh">offenliche</corr>
    </choice>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.5. Simple Editorial Changes](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COED)