---
title: seal
---



# `<seal/>` (sceau)

## Description

Décrit un sceau.

## Explication

Les sceaux sont décrits de gauche à droite. Voir également la description du sceau sous le sceau des métadonnées. S'il s'agit d'une personne, le scelleur est marqué par [`<persName/>`](persName.md)  et l'attribut[@role](#role)  =`sigillant`  ou, s'il s'agit d'une institution, par [`<orgName/>`](orgName.md)  et le même attribut. Si les noms des scelleurs figurent sur le plica ou la bande de parchemin, dans[`<persName/>`](persName.md)  un[`<orig/>`](orig.md)  doit inclure le nom manuscrit.

En cas d'identifications incertaines des sceaux, si par ex. Par exemple, si le scelleur n'est pas nommé dans le certificat, aucun [`<orgName/>`](orgName.md)  ou[`<persName/>`](persName.md)  n'est donné. Si les scellés ne peuvent pas être attribués avec certitude dans le cas de plusieurs scellés, l'identification du scellé est laissée ouverte.

Les sceaux sont numérotés avec [@n](#n). Il serait souhaitable que l'édition comprenne non seulement un fac-similé du texte, mais également une photo du sceau, y compris l'échelle. Si tel était le cas pour tous les sceaux,[@extent](#extent)  pourrait être omis.

L. S. = Locus sigilli est enregistré avec [`<figure/>`](figure.md). Si un document a été délivré sans sceau, aucun sceau n'est enregistré. Un commentaire sur les sceaux peut être écrit au besoin.

Il est important de comparer l'annonce du sceau dans le texte et le sceau lui-même. 

- Tous les scelleurs annoncés ont-ils apposé leurs sceaux sur l'acte ?
- Existe-t-il un sceau d'un scellant non annoncé ?
- Un sceau a-t-il pu être forgé ou apposé plus tard ?[@condition](#condition)  avec`absent`. De plus, une note ([`<note/>`](note.md) ) doit décrire pourquoi le sceau est manquant ou pourquoi le document est resté descellé.

Sur les sceaux impériaux: Posse Otto: Die Siegel der deutschen Kaiser und Könige von 751-1806 und 1871-1913, 5 Bde. Dresden 1909–1913 (http://de.wikisource.org/wiki/Die_Siegel_der_Deutschen_Kaiser_und_K%C3%B6nige). 

## Modèle de contenu

- **core**: [p](p.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md)

## Attributs

### @attachment

Décrit le mode de fixation du sceau

*Valeurs possibles*

- applied – *pressé*
- sealed_on_a_cord – *attaché à un cordo*
- sealed_on_a_lace – *attaché à un cordon*
- sealed_on_a_leather_tag – *attaché à une lanière en cuir*
- sealed_on_a_parchment_tag – *attaché à une lanière en parchemin*
- sealed_on_a_ribbon – *attaché à un ruban*
- sealed_on_laces – *attaché à un fil*
- slit – *il n’existe qu’une fente pour le sceau*
- wrapping-tie – *sceau de clôture*

### @condition

Décrit l'état de conservation et les dommages d'un sceau. 

*Valeurs possibles*

- absent – *absent*
- bound_in_linen – *lié dans un sachet de lin*
- chamfered – *écorné*
- damaged – *endommagé*
- ex_and_enclosed – *détaché et joint*
- fragmentary – *fragmentaire*
- in_a_box – *dans une boîte en bois*
- in_a_capsule – *dans une boîte en métal*
- polished – *poli*
- well-preserved – *bien conservé*

### @facs

Associe une page de texte à un fac-similé ou à un extrait de fac-similé. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `[A-Za-z_\-\.0-9]+([1-9]|[rv])`

### @material

Décrit le matériau d'un sceau

*Valeurs possibles*

- bulle – *bulle*
- papered_seal – *sceau sous papier*
- sealing_wax – *cire pour le scellement*
- wafer – *sceau hostie*
- wax – *cire*
- wax_in_a_box – *cire dans une boîte en bois*
- wax_in_a_capsule – *cire dans une boîte en métal*
- wax_with_margin – *cire avec un bord*

### @n

Comptage consécutif des sceaux de gauche à droite (en fonction des fentes de sceaux ou des sceaux réellement présents) 

*Valeurs possibles*

- Nombre

### @place

Décrit l'emplacement du sceau

*Valeurs possibles*

- end – *en bas de l’acte*
- overleaf – *sur l’autre page de la feuille*

### @shape

Décrit la forme du sceau

*Valeurs possibles*

- heart-shaped – *en forme de cœur*
- octangular – *octongonal*
- oval – *ovale pointu*
- peltade – *en forme de bouclier*
- round – *rond*
- triangular – *triangulaire*

## Exemples

### Exemple 1

Exemple de saisie d'un sceau

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
        <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
    </seal>
</egXML>
               
```

### Exemple 2

Saisie d'un moment

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
        <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
    </seal>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [10.7.3.2. Seals](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#msphse)