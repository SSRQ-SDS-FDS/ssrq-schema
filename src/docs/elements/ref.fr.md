---
title: ref
---



# `<ref/>` (référence)

## Description



## Explication

La référence peut pointer vers un autre document, l'introduction, l'index d'un volume rétronumérisé, une entrée dans l'HLS, une littérature citée, etc. Il est logique de placer des liens dans [`<ref/>`](ref.md)  vers d'autres éléments sources qui ne sont pas édités mais qui sont répertoriés individuellement dans un système d'information d'archives. Cela n'a pas de sens qu'un seul certificat soit lié à l'ensemble du stock de certificats parce que le certificat individuel n'est pas répertorié. Dans le cas d'entrées d'un livre que l'on ne souhaite pas répertorier individuellement dans un système d'information d'archives (si cela est possible), un lien peut être établi vers le livre (entier) répertorié dans le catalogue d'archives. Si des liens sont établis vers d'autres éditions, la cote de la source est indiquée en premier si le matériel d'archives a été consulté (autopsie) ou si la cote peut être vérifiée et liée par requête. Si un document d'archives a été évalué sur la base d'une édition, seule l'édition doit être spécifiée. Si vous voulez faire référence à une source qui est éditée dans une unité d'édition du SSRQ, il n'est pas nécessaire de répéter la référence archivistique, mais il suffit de faire le lien avec le numéro d'item de l'unité d'édition (voir exemple ci-dessous). Il est également possible de référencer d'une pièce à l'autre au sein de votre propre unité d'édition. Nous utilisons le[`<idno/>`](idno.md)  pour cela.

## Modèle de contenu

- **core**: [hi](hi.md)
- Contenu de texte au choix

## Attributs

### @target

Lien hypertexte, DOI ou référence interne.

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `doi:10\.\d{4}/.*`
- anyURI – Restriction: expression régulière `(https?|ftp)://[^\s/$.?#].[^\s]*`
- Chaîne de caractères – Restriction: expression régulière `urn:ssrq:(SSRQ|SDS|FDS)-([A-Z]{2})-([A-Za-z0-9_]+)(-((([A-Za-z0-9]+\.)*)([0-9]+)-([0-9]+)))?(#[A-Za-z0-9_]+)?`

## Exemples

### Exemple 1

Référence aux sources imprimées

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <bibl>
        <ref target="https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858">SSRQ SG
                    III/2, Nr. 231
                </ref>
    </bibl>
</egXML>
               
```

### Exemple 2

Référence à un autre document

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <ref target="urn:ssrq:SSRQ-ZH-NF_I_2_1-4-1">SSRQ ZH NF I/2/1 4-1</ref>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [3.7. Simple Links and Cross-References](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#COXR)
- [16.1. Links](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html#SAPT)